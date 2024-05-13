from django.shortcuts import render ,redirect
from .models import Produit , Fournisseur , Categorie , Commande , ModificationQuantiteStock
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from django.db.models import Sum
from datetime import date
from rest_framework import viewsets
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

#-----------------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categorie
from magasin.serializers import CategorySerializer , ProduitSerializer
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

#--------------------------------

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été   créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})
def Connexion(request):
    pass

def index(request):
    produits = Produit.objects.all()
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query:
            produits = Produit.objects.filter(libelle__icontains=search_query)
            
            if not produits.exists():
                produits = Produit.objects.filter(description__icontains=search_query)
            
            if not produits.exists():
                produits = Produit.objects.filter(prix__icontains=search_query)
            
        else:
            produits = Produit.objects.all()
    else:
        produits = Produit.objects.all()
    panier_ids = request.session.get('panier', [])
    panier_count = len(panier_ids)
    return render(request, 'magasin.html', {'produits': produits, 'panier_count': panier_count})

#-------------------------
def ajouterPanier(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        produit = Produit.objects.get(pk=produit_id)
        if 'panier' not in request.session:
            request.session['panier'] = {}
        panier = request.session['panier']
        panier[produit_id] = panier.get(produit_id, 0) + 1
        request.session['panier'] = panier
    return redirect('/magasin')

def RemoveProduit(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        if 'panier' in request.session:
            panier = request.session['panier']
            if produit_id in panier:
                panier.pop(produit_id) 
                request.session['panier'] = panier
    return redirect('panier')

def MoisQntProduit(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        if 'panier' in request.session:
            panier = request.session['panier']
            if produit_id in panier:
                panier[produit_id] -= 1  
                if panier[produit_id] <= 0:  
                    panier.pop(produit_id)
                request.session['panier'] = panier
    return redirect('panier')

def plusQntProduit(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        if 'panier' in request.session:
            panier = request.session['panier']
            panier[produit_id] = panier.get(produit_id, 0) + 1  
            request.session['panier'] = panier
    return redirect('panier')


@login_required
def confirmPanier(request):
    if request.method == 'POST':
        panier = request.session.get('panier', {})
        produits = Produit.objects.filter(pk__in=panier.keys())
        total_price = produits.aggregate(total=Sum('prix'))['total'] or 0
        
        commande = Commande.objects.create(totalCde=total_price , user = request.user)
        for produit in produits:
            quantite = panier[str(produit.id)]

            produit.quantite_en_stock -= quantite
            produit.save()

            commande.produits.add(produit)

            modification = ModificationQuantiteStock.objects.create(
                produit=produit,
                ancienne_quantite=produit.quantite_en_stock + quantite,
                nouvelle_quantite=produit.quantite_en_stock
            )

        if 'panier' in request.session:
            del request.session['panier']
        
    return redirect('/magasin')


@login_required
def compte(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = UserUpdateForm(instance=request.user)

    user = request.user
    command_history = Commande.objects.filter(user=user)
    context = {
        'user': user,
        'command_history': command_history,
        'form': form ,
    }
    return render(request, 'compte.html', context)


from django.db.models import Sum

@login_required
def stats(request):
    total_benefit = Commande.objects.aggregate(total_benefit=Sum('totalCde'))['total_benefit'] or 0
    orders = Commande.objects.all()

    product_quantities = {}

    for order in orders:
        for product in order.produits.all():
            if product not in product_quantities:
                product_quantities[product] = 0
            product_quantities[product] += 1

    top3_products = sorted(product_quantities.items(), key=lambda x: x[1], reverse=True)[:3]

    context = {
        'total_benefit': total_benefit,
        'top3_products': top3_products,
        'orders': orders,
    }
    return render(request, 'stats.html', context)


def removePanier(request):
    if request.method == 'POST':
        if 'panier' in request.session:
            del request.session['panier']
    return redirect('panier')


def panier(request):
    panier = request.session.get('panier', {})
    produit_ids = panier.keys()
    produits = Produit.objects.filter(pk__in=produit_ids)

    total_price = Decimal('0.00')
    panier_details = []
    for produit in produits:
        quantity = panier.get(str(produit.id), 0) #get بإرجاع 0 كقيمة افتراضية
        total_price += produit.prix * quantity
        panier_details.append({'produit': produit, 'qnt': quantity})


    return render(request, 'panier.html', {'produits': panier_details, 'total_price': total_price})


#------------------------

@login_required
def AjouterProduit(request):
    if request.method == 'POST':
        libelle = request.POST.get('libelle')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        type = request.POST.get('type')
        fournisseur_id = request.POST.get('fournisseur')
        categorie_id = request.POST.get('categorie')
        img = request.FILES.get('img') 

        produit = Produit(
            libelle=libelle,
            description=description,
            prix=prix,
            type=type,
            img=img,
            fournisseur_id=fournisseur_id,
            categorie_id=categorie_id
        )
        
        produit.save()
        
        return redirect('listProduit')  
    
    return redirect('listProduit')

@login_required
def searchProduit(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query:
            produits = Produit.objects.filter(libelle__icontains=search_query)
            
            if not produits.exists():
                produits = Produit.objects.filter(description__icontains=search_query)
            
            if not produits.exists():
                produits = Produit.objects.filter(prix__icontains=search_query)
            
        else:
            produits = Produit.objects.all()
    else:
        produits = Produit.objects.all()
       
    fournisseur = Fournisseur.objects.all() 
    categorie = Categorie.objects.all() 
    return render(request, 'listProduit.html', {'fournisseurs': fournisseur , 'produits' : produits , 'categories' :categorie})  

def listProduit(request):
    fournisseur = Fournisseur.objects.all() 
    categorie = Categorie.objects.all() 
    produits = Produit.objects.all()
    return render(request, 'listProduit.html', {'fournisseurs': fournisseur , 'produits' : produits , 'categories' :categorie})  

@login_required
def deleteProduit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        produit = Produit.objects.filter(id=id)
        produit.delete()
        return redirect('listProduit')  
    return redirect('listProduit')  
@login_required
def deleteFournisseur(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        fournisseur = Fournisseur.objects.filter(id=id)
        fournisseur.delete()
        return redirect('AjouterFournisseur')  
    return redirect('AjouterFournisseur')  

@login_required
def ProduitEdit(request):
    if request.method == 'POST':
        produit_id = request.POST.get('id')
        print(id)
        produit = Produit.objects.get(id=produit_id)
        produit.libelle = request.POST.get('libelle')
        produit.description = request.POST.get('description')
        produit.prix = request.POST.get('prix')
        produit.type = request.POST.get('type')
        """ produit.fournisseur = request.POST.get('fournisseur')
        produit.categorie = request.POST.get('categorie') """
        produit.img = request.FILES.get('img') 

        produit.save()
        
        return redirect('listProduit')  
    else:
        return redirect('listProduit')

@login_required
def FournisseurEdit(request):
    if request.method == 'POST':
        fournisseur_id = request.POST.get('id')
        print(fournisseur_id)
        fournisseur = Fournisseur.objects.get(id=fournisseur_id)
        
        fournisseur.nom = request.POST.get('nom')
        fournisseur.adresse = request.POST.get('adresse')
        fournisseur.email = request.POST.get('email')
        fournisseur.telephone = request.POST.get('telephone')
        
        fournisseur.save()
        
        return redirect('AjouterFournisseur')  
    return redirect('AjouterFournisseur') 
@login_required
def editProduit(request):

    produit = None
    if request.method == 'POST':
        id = request.POST.get('id')
        produit = Produit.objects.get(id=id)
    fournisseur = Fournisseur.objects.all() 
    categorie = Categorie.objects.all() 
    return render(request, 'editProduit.html', {'produit': produit , 'fournisseurs': fournisseur  , 'categories' :categorie})
@login_required
def editFournisseur(request):
    fournisseur = None
    if request.method == 'POST':
        id = request.POST.get('id')
        print(id)
        fournisseur = Fournisseur.objects.get(id=id)
        print(fournisseur.nom)
    
    return render(request, 'editFournisseur.html', {'fournisseur': fournisseur})


@login_required
def AjouterFournisseur(request):
    fournisseurs = Fournisseur.objects.all()
    if request.method == 'POST':
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        
        fournisseur = Fournisseur.objects.create(
            nom=nom,
            adresse=adresse,
            email=email,
            telephone=telephone
        )

        return redirect('/magasin')  
    else:
        
        return render(request, 'AjouterFournisseur.html', {'fournisseurs': fournisseurs})

@login_required
def searchFournisseur(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '').strip()

        # Perform the search based on the entered query
        if search_query:
            fournisseurs = Fournisseur.objects.filter(nom__icontains=search_query)
            
            if not fournisseurs.exists():
                fournisseurs = Fournisseur.objects.filter(adresse__icontains=search_query)
            
            if not fournisseurs.exists():
                fournisseurs = Fournisseur.objects.filter(email__icontains=search_query)
            
            if not fournisseurs.exists():
                fournisseurs = Fournisseur.objects.filter(telephone__icontains=search_query)
        else:
            fournisseurs = Fournisseur.objects.all()
    else:
        fournisseurs = Fournisseur.objects.all()

    return render(request, 'AjouterFournisseur.html', {'fournisseurs': fournisseurs})





from django.db import models
from datetime import date

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom
    


class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Alimentaire', 'Alimentaire'),
        ('Meuble', 'Meuble'),
        ('Sanitaire', 'Sanitaire'),
        ('Vaisselle', 'Vaisselle'),
        ('Vêtement', 'Vêtement'),
        ('Jouets', 'Jouets'),
        ('Linge de Maison', 'Linge de Maison'),
        ('Bijoux', 'Bijoux'),
        ('Décor', 'Décor'),
        ('Immobilier','Immobilier'),
        ('Linge', 'Linge'),
        ('Electroménager', 'Electroménager'),
        ('ParaPharmacie', 'ParaPharmacie'),
        ('Tapis', 'Tapis'),
        ('Frais', 'Frais')
    ]

    name = models.CharField(max_length=50, default='Alimentaire', choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
    


class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    TYPE_CHOICES = [('em', 'emballé'), ('fr', 'Frais'), ('cs', 'Conserve')]
    type = models.CharField(max_length=2, default='em', choices=TYPE_CHOICES)
    img = models.ImageField(blank=True)
    quantite_en_stock = models.IntegerField(default=0)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        return f"{self.libelle} {self.description} {self.prix} {self.type}"
    
#--------------------------------
class ModificationQuantiteStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    ancienne_quantite = models.IntegerField()
    nouvelle_quantite = models.IntegerField()
    date_modification = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id} {self.ancienne_quantite} {self.date_modification} {self.nouvelle_quantite}"
    
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=ModificationQuantiteStock)
def verifier_quantite_en_stock(sender, instance, **kwargs):
    if instance.nouvelle_quantite == 0:
        # Si la nouvelle quantité est égale à 0, supprimez le produit
        instance.produit.delete()
#------------------------

class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit)

    def __str__(self):
        return f"Commande du {self.dateCde} - Total : {self.totalCde} DT"
    
""" class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    def __str__(self):
        return f"Commande du {self.commande} - Total : {self.totalCde} DT" """

class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.libelle} - {self.prix} DT ({self.type}) - Garantie: {self.duree_garantie}"
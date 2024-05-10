from django.urls import path   #,include
#from django.conf.urls import url
from . import views
from . import views
from .views import CategoryAPIView , ProduitAPIView



urlpatterns = [
    path('', views.index, name='index'),
    path('AjouterFournisseur', views.AjouterFournisseur, name='AjouterFournisseur'),
    path('searchFournisseur', views.searchFournisseur, name='searchFournisseur'),
    path('deleteFournisseur', views.deleteFournisseur, name='deleteFournisseur'),
    path('editFournisseur', views.editFournisseur, name='editFournisseur'),
    path('listProduit', views.listProduit, name='listProduit'),
    path('FournisseurEdit', views.FournisseurEdit, name='FournisseurEdit'),
    path('AjouterProduit', views.AjouterProduit, name='AjouterProduit'),
    path('deleteProduit', views.deleteProduit, name='deleteProduit'),
    path('searchProduit', views.searchProduit, name='searchProduit'),
    path('editProduit', views.editProduit, name='editProduit'),
    path('ProduitEdit', views.ProduitEdit, name='ProduitEdit'),
    path('register/',views.register, name = 'register'), 
    path('Connexion/',views.Connexion, name = 'Connexion'),



    path('ajouterPanier',views.ajouterPanier, name = 'ajouterPanier'),
    path('panier',views.panier, name = 'panier'),
    path('panier',views.panier, name = 'removePanier'),
    path('RemoveProduit',views.RemoveProduit, name = 'RemoveProduit'),
    path('removePanier',views.removePanier, name = 'removePanier'),
    path('confirmPanier',views.confirmPanier, name = 'confirmPanier'),
    path('MoisQntProduit',views.MoisQntProduit, name = 'MoisQntProduit'),
    path('plusQntProduit',views.plusQntProduit, name = 'plusQntProduit'),




    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),


]

# http://127.0.0.1:8000/magasin/api/category
# http://127.0.0.1:8000/magasin/api/produits
# http://127.0.0.1:8000/api/produit/22
# 

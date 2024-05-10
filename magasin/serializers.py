from rest_framework.serializers import ModelSerializer
from .models import Categorie , Produit
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']


class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libelle', 'description', 'categorie' , 'img']

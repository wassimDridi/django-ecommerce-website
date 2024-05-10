from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Produit, ModificationQuantiteStock

# Créez un signal pour détecter les modifications de quantité en stock
@receiver(post_save, sender=ModificationQuantiteStock)
def verifier_quantite_en_stock(sender, instance, **kwargs):
    print("-----------------------------")
    if instance.nouvelle_quantite == 0:
        # Si la nouvelle quantité est égale à 0, supprimez le produit
        instance.produit.delete()

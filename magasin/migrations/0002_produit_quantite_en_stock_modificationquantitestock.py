# Generated by Django 5.0.4 on 2024-05-03 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='quantite_en_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ModificationQuantiteStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancienne_quantite', models.IntegerField()),
                ('nouvelle_quantite', models.IntegerField()),
                ('date_modification', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
            ],
        ),
    ]
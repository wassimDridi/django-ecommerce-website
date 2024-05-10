Projet Django - E-Commerce 
Introduction
Le projet Django E-Commerce Hub est une plateforme de commerce électronique permettant aux utilisateurs de découvrir, explorer et acheter une variété de produits en ligne. Ce projet est développé en utilisant le framework Django, ce qui offre une structure robuste et flexible pour la construction d'applications web.

Fonctionnalités :

1. Inscription et Connexion
Les visiteurs peuvent créer un compte sur la plateforme ou se connecter s'ils ont déjà un compte. L'authentification est gérée de manière sécurisée grâce à Django's authentication system.

2. Navigation et Recherche
Les visiteurs peuvent parcourir les différentes catégories de produits disponibles sur la plateforme, ainsi que rechercher des produits spécifiques en utilisant la fonction de recherche.

3. Affichage de Produits
Les produits sont présentés de manière attrayante avec des images, des descriptions et des informations de prix. Les visiteurs peuvent consulter les détails des produits avant de prendre une décision d'achat.

4. Ajout au Panier
Les visiteurs peuvent ajouter des produits à leur panier d'achat pour les acheter ultérieurement. Le panier conserve les produits sélectionnés par l'utilisateur jusqu'à ce qu'ils finalisent leur achat.

5. Gestion du Panier
Les visiteurs peuvent ajuster les quantités de produits dans leur panier, supprimer des produits ou vider complètement leur panier.

6. Passage de Commande
Après avoir finalisé leur sélection, les utilisateurs peuvent se connecter à leur compte ou créer un compte s'ils n'en ont pas encore, puis confirmer leur commande.

7. Gestion des Produits et Fournisseurs par l'Admin
L'administrateur du site dispose de fonctionnalités avancées pour gérer les produits et les fournisseurs. Cela comprend l'ajout, la modification et la suppression de produits, ainsi que la gestion des fournisseurs associés.

8. Création de la Page d'Accueil et Affichage de la Liste des Produits
La page d'accueil est créée pour présenter les produits disponibles sur la plateforme. La liste des produits est affichée en utilisant une requête Fetch JavaScript pour interroger l'API REST Django, offrant ainsi une expérience utilisateur dynamique.

9. Suppression Automatique des Produits
Les produits dont la quantité disponible atteint zéro sont automatiquement supprimés de la liste des produits disponibles sur la plateforme.

10. Application de Publication
Les utilisateurs peuvent créer, modifier et supprimer des publications sur la plateforme. Cette fonctionnalité leur permet de partager des informations, des avis ou des expériences avec la communauté.

Installation :

Pour installer et exécuter ce projet localement, suivez les étapes ci-dessous :

Clonez ce dépôt sur votre machine locale en utilisant la commande :
git clone < https://github.com/wassimDridi/django-ecommerce-website >

2. Accédez au répertoire du projet :
cd mysite

3. Créez un environnement virtuel pour isoler les dépendances du projet :
python -m venv env

4. Activez l'environnement virtuel :
Sur Windows :
.\env\Scripts\activate
Sur macOS et Linux :
source env/bin/activate

5. Effectuez les migrations de la base de données :
python manage.py migrate

6. Lancez le serveur de développement Django :
python manage.py runserver

7. Accédez à l'URL http://127.0.0.1:8000/ dans votre navigateur pour voir l'application en action.


Technologies Utilisées
Django : Framework web Python
HTML, CSS et JavaScript : Frontend
Bootstrap : Framework CSS pour la conception responsive
SQLite : Système de gestion de base de données relationnelle (utilisé pour le développement)

Auteur
Ce projet a été développé par Dridi Wassim dans le cadre d'un projet personnel ou académique. Pour toute question ou commentaire, vous pouvez me contacter à wassimdridi724@gmail.com .
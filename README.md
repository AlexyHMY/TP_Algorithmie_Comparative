# TP Algorithmie Comparative
## Gestion de Colis et Optimisation de Chargement (Livraison)

Projet (C ou Python) visant à gérer une collection de colis et à optimiser le chargement de camions sous contraintes de poids, de valeur et de priorité.

## Fonctionnalités
- **Gestion des colis :** Ajout, affichage global et recherche instantanée par identifiant.
- **Tris multicritères :** Affichage des colis selon leur poids, leur valeur ou leur priorité.
- **Optimisation du camion :** Sélection intelligente des colis (problème du sac à dos) via un score composite (Valeur × Priorité / Poids).
- **Statistiques :** Vue d'ensemble sur le volume, le poids et la valeur totale des colis.

## Structure du Projet
projet/
│
├── src/
│   └── code source (main.py)
│
├── README.md
│
└── rapport.pdf

## Prérequis et Lancement

Le projet est développé en **Python** (version 3.x recommandée). Aucune bibliothèque externe n'est nécessaire.

Pour lancer le programme :

```bash
python src/projet_livraison.py
```

## Choix Algorithmiques Clés

- **Recherche par ID :** Utilisation d'un dictionnaire (table de hachage) pour un accès en O(1).
- **Tris :** Utilisation de l'algorithme natif Timsort en O(N log N).
- **Chargement du camion :** Approche gloutonne basée sur un score d'attractivité pour traiter efficacement jusqu'à 100,000 colis.

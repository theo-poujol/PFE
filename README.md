# PFE

Procédure à suivre pour lancer le script qui calcule les masques des images en entrée et calcule l'harmonique sphérique

Lien du github du projet : https://github.com/theo-poujol/PFE

# Méthode de lancement

1. Se placer à la racine de projet

2. Executer la commande

{chemin_du_dossier} : Chemin du dossier qui contient les images

Dans le projet un dossier "images" contient 2 sous dossiers "cafe" et "voiture" contenant des images de test de machine à café et d'une voiture

$ python pfe.py {chemin_du_dossier}

ou si votre alias python pointe vers une version de python 2
$ python3 pfe.py {chemin_du_dossier}

3. Le script python produit un masque par image, qui sont ensuite sauvegardé dans le dossier "masks" du projet.
L'harmonique sphérique est sauvegardée dans le dossier "sphere"

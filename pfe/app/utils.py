import os
import matplotlib.pyplot as plt

def create_sex_pie_chart():
    # Supposons que vous ayez des données sur la répartition par sexe
    sexes = ['Homme', 'Femme']
    counts = [10, 40]  # Exemple de nombre de personnes par sexe

    # Création du graphique
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=sexes, autopct='%1.1f%%')
    plt.title('Répartition par sexe')

    # Sauvegarde du graphique dans le dossier 'static'
    static_dir = os.path.abspath('static')

    # Construction du chemin absolu du fichier
    image_path = os.path.join(static_dir, 'graphe1.png')
    
    # Sauvegarde réelle du graphique
    plt.savefig(image_path)

    plt.close()

def create_age_bar_chart():
    # Supposons que vous ayez des données sur la répartition par tranche d'âge
    age_groups = ['0-20', '21-40', '41-60', '61+']
    counts = [20, 35, 45, 25]  # Exemple de nombre de personnes par tranche d'âge

    # Création du graphique
    plt.figure(figsize=(8, 6))
    plt.bar(age_groups, counts)
    plt.xlabel('Tranche d\'âge')
    plt.ylabel('Nombre de personnes')
    plt.title('Répartition par tranche d\'âge')

    # Sauvegarde du graphique dans le dossier 'static'
    static_dir = os.path.abspath('static')

    # Construction du chemin absolu du fichier
    image_path = os.path.join(static_dir, 'graphe2.png')

    # Sauvegarde réelle du graphique
    plt.savefig(image_path)

    plt.close()
#RHALDOUNI Saad
#SABLE Laure

#Terminal NSI --------- Mini Projet

import json
import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import webbrowser
import requests


f = open("fr-parcoursup.json","rt", encoding='UTF8')
lecteurJSON = json.loads(f.read())
# print(lecteurJSON)
# Commentaire de Simon : si je ne commente pas la ligne du dessus mon pc rame à cause de la longueur du fichier json

"""
url = "https://data.enseignementsup-recherche.gouv.fr/api/records/1.0/search/?dataset=fr-esr-parcoursup&q=&sort=tri&facet=session&facet=contrat_etab&facet=cod_uai&facet=g_ea_lib_vx&facet=dep_lib&facet=region_etab_aff&facet=acad_mies&facet=select_form&facet=fili&facet=form_lib_voe_acc&facet=regr_forma&facet=fil_lib_voe_acc&facet=detail_forma&facet=tri&facet=cod_aff_form&timezone=Europe%2FBerlin"
reponse = requests.get(url)
lecteurJSON = json.loads(reponse.text)
"""

filiereRandom = ['Tourisme','Chimie','Animation-gestion de projets dans le secteur sportif','Droit','MPSI']
aleatoire = random.choice(filiereRandom)

def choixFiliere(filiere):
    """
    Fonction qui parcours l'open data en gardant seulement les données 
    en raccord avec la filiere choisis (en parametre)
    """
    
    listeFiliere = [] # Liste vide pour y classer les etab selon leur filiere proposée
    for objet in lecteurJSON:
        if objet['fields']['fil_lib_voe_acc'] == filiere:
            listeFiliere.append(objet)
    return listeFiliere

def choixDepartement(departement, listeFiliere):
    """
    Objectif: Parcourir la liste déjà trier en fonction des filieres,
    de façon a garder seulement celles en raccord avec le département choisis
    
    Parametre: departement, liste de filiere triée
    """
    
    listeDepartement = []    # Liste vide pour y classer les etab selon leur departement
    for objet in listeFiliere:     # Pour tous les objets de la liste
        if objet['fields']['dep_lib'] == departement:
            listeDepartement.append(objet)
    return listeDepartement
                        
def graphiqueEtablissement(etab):
    """
    Objectif: Générer un graphique avec le nombre d'élèves accepter
    selon leur bac
    
    Parametre: Un objet de l'open data "Parcoursup"
    """
    
    try:
        plt.ylabel("Nombres d'élèves") # Nom de l'axe des ordonnées
        plt.title(etab['fields']['g_ea_lib_vx'])
        names = ['General', 'Techno', 'Pro'] # Nom des barres
        values = [etab['fields']['taux_adm_psup_gen'], etab['fields']['taux_adm_psup_techno'],etab['fields']['taux_adm_psup_pro']]
        plt.bar(names, values) ; plt.show() # Tracer
    except KeyError:
        print('Impossible de générer le graphique')
    
    
    
    
if __name__ == "__main__":
    #print(choixFiliere('MPSI'))
    print(choixFiliere(aleatoire))
    print(choixDepartement('Loire-Atlantique'))
    for i in range(len(listeDepartement)):
        graphiqueEtablissement(listeDepartement[i])


 

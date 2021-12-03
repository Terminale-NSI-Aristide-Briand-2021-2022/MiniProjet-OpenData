#RHALDOUNI Saad
#SABLE Laure

#Terminal NSI --------- Mini Projet

import tkinter as tk
from tkinter import ttk
from main import *
import webbrowser

#Mise en page de la fenêtre Tkinter
fenetre= tk.Tk()
fenetre.geometry('800x800')
fenetre.configure(bg='white')
fenetre.title("ParcourSup") #Titre de la page 

#Insertion des images
logo1 = tk.PhotoImage(file='parcoursup.png')
labelimage1 = tk.Label(fenetre,image=logo1)
logo2 = tk.PhotoImage(file='parcoursup.png')
labelimage2 = tk.Label(fenetre,image=logo2)

#Position des images
labelimage1.place(x=500,y=10)
labelimage2.place(x=30,y=10)

#Texte de la page
labeltexte1 = tk.Label(fenetre, text="Bienvenue !",font=("Times", 20),foreground="red", bg="white")
labeltexte2 = tk.Label(fenetre, text="Veuillez choisir une filière",font=("Times",10),foreground="blue", bg="white")
labeltexte3=tk.Label(fenetre,text="Veuiller toujours selectionner : filière puis département",font=("Times",10),bg="white")
labeltexte4 = tk.Label(fenetre, text="Etablissement(s) possible: ",font=("Times",10),bg="white")

#Position des texte sur la page
labeltexte1.pack(padx=10,pady=5)
labeltexte2.pack(padx=10,pady=0)
labeltexte3.pack(padx=100,pady=70)
labeltexte4.place(x=325, y =170)

#Classe pour faire une liste déroulante
class Filiere:
    """Création du Class qui permet de faire la liste des filières pour les fenêtre déroulante"""
    def __init__(self,n):
        self.nom=n
        
listeFiliere=[]
filiere1=Filiere("Droit")
filiere2=Filiere("Tourisme")
filiere3=Filiere("MPSI")
filiere4=Filiere('Chimie')
filiere5=Filiere('Animation-gestion de projets dans le secteur sportif')
listeFiliere.append(filiere1.nom)
listeFiliere.append(filiere2.nom)
listeFiliere.append(filiere3.nom)
listeFiliere.append(filiere4.nom)
listeFiliere.append(filiere5.nom)

#Liste de département pour la deuxième fenêtre déroulante
listeDepartement = ['Loire-Atlantique','Paris','Gironde','Seine-Saint-Denis','Nord','Rhône','Bouches-du-Rhône','Haute-Garonne','Hauts-de-Seine','La Réunion','Finistère','Hérault','Pas-de-Calais','Morbihan','Loire']

#Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(fenetre,values=listeFiliere)
listeCombo2 = ttk.Combobox(fenetre,values=listeDepartement)

#Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)
listeCombo2.current(0)

#Gestion des actions pour le choix de la Filière et du département
a = []
b = []

def action(event):
    """
    Appelle la fonction choixFiliere selon
    la filiere choisis de la premiere liste 
    """
    global a
    select=listeCombo.get()
    a = choixFiliere(select)
    
    
def action2(event):
    """
    Foncton qui gere les evenements de la deuxieme combobox
    """
    select2=listeCombo2.get()
    b = choixDepartement(select2, a)
    
    #Espacer les boutons
    i = 200

    #Fond Blanc pour faire disparaitre le texte
    monCanvas = tk.Canvas(fenetre, width=800, height=800, bg='white', borderwidth=0, highlightthickness=0)
    monCanvas.place(x=5,y=190)

    #On parcourt la liste pour générer les boutons
    for objet in b:
        
        bat = objet['fields']['g_ea_lib_vx'] #Nom du batiment
        fiche = objet['fields']['lien_form_psup'] #Lien vers la fiche info
        
        #Nom du batiment sur l'IHM
        labeltexteTEST = tk.Label(fenetre, text="{}".format(bat),font=("Times",10),bg="white")
        labeltexteTEST.place(x=300, y = i)
        
        #Bouton graphique
        boutonGraphique = tk.Button(fenetre, text="Graphique", command= lambda: action3(objet))
        boutonGraphique.place(x=180, y = i)
        
        #Bouton info
        boutonInfo = tk.Button(fenetre, text="Info", command= lambda: action4(fiche))
        boutonInfo.place(x=260, y = i)
        
        #Espacer les boutons
        i = i + 30 
             
def action3(ecole):
    graphiqueEtablissement(ecole)

def action4(lien):
    lien = str(lien)
    webbrowser.open(lien)
  
#Gestion des actions pour le graphique et les liens
def action3(ecole):
    graphiqueEtablissement(ecole)

def action4(lien):
    lien = str(lien)
    webbrowser.open(lien)
     
#Insertion des liste déroulantes
listeCombo.bind("<<ComboboxSelected>>",action)
listeCombo2.bind("<<ComboboxSelected>>",action2)

#Position des listes déroulantes
listeCombo.place(x=300,y=80)
listeCombo2.place(x=300,y=110)

#Fin du Tkinter de la fenetre
fenetre.mainloop()

 

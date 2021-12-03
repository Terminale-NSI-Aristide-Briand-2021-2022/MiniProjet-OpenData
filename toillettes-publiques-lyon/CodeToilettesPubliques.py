# Mini-Projet POO+Tkinter+OpenData+JSON par ROUSSEAU Elouan et ORHON Kilian

# Importation des bibliothèques

import tkinter as tk
from tkinter import ttk
import json
import requests
import folium
from PIL import ImageTk, Image

# Définition de la fenêtre Tkinter

root= tk.Tk()
root.title('Les toilettes publiques de la métropole de Lyon')
root.geometry('1000x400')
root.resizable(width=False,height=False)
fen=tk.Canvas(root,width=1000,height=400,background="white")
fen.place(x=0,y=0)

# Création des fonctions


def importation_donnees():
    """importation_donnees() importe des donnees au format json depuis une URL"""
    reponse=requests.get('https://download.data.grandlyon.com/ws/grandlyon/adr_voie_lieu.adrtoilettepublique_latest/all.json')
    tabJSON=json.loads(reponse.text)
    Toilettes=[]
    l=len(tabJSON['values'])
    for i in range(l):
        if tabJSON['values'][i]['openinghoursspecification']!=None:
            ouv=tabJSON['values'][i]['openinghoursspecification'][0]['opens']
            ferm=tabJSON['values'][i]['openinghoursspecification'][0]['closes']
        else:
            ouv=None
            ferm=None       
        acces=tabJSON['values'][i]['acceshandi']
        cout=tabJSON['values'][i]['payant']
        #adresse=tabJSON['values'][i]['adresse']
        lat=tabJSON['values'][i]['lat']
        lon=tabJSON['values'][i]['lon']
        Toilettes.append([ouv,ferm,acces,cout,lat,lon])
    return Toilettes


def lancement_recherche():
    acces=Handi.get()
    cout=Cout.get()
    affichage=Recherche(acces,cout,Heure_select)
    affichage.nombreT_avec_acces()
    affichage.nombreT_avec_cout()
    affichage.nombreT_avec_horaires()
    affichage.localisation_T()
    reponse=tk.Label(fen,background='white',fg="red",font=('aral italic',12),
            text="Il y a {} toilettes correspondants, une carte de ces derniers a été enregistrée dans vos documents !".format(affichage.compteur))
    reponse.place(x=50,y=315)


def RecupValeur(event):
    global Heure_select
    Heure_select=""
    Heure_select=ListeDeroulante.get()
    

def quitter():
    root.quit()
    root.destroy()
                    
                    
# Création de la classe

class Recherche:
    def __init__(self,acces,cout,Heure_select):
        self.acces=acces
        self.cout=cout
        self.horaire=Heure_select
        self.compteur=0
        self.T=[]
        
    
    def nombreT_avec_acces(self):
        """ nombreT_avec_acces(self) calcule le nombre de
            toilettes de la liste correspondant au critère d'accès"""
        global Toilettes
        T=[]
        l=len(Toilettes)
        for i in range(l):
            if self.acces==0 and Toilettes[i][2]==None:
                T.append(Toilettes[i])
            if self.acces==1 and Toilettes[i][2]==True:
                T.append(Toilettes[i])
            if self.acces==2:
                T.append(Toilettes[i])
        self.T=T
                    
    
    def nombreT_avec_cout(self):
        """ nombreT_avec_cout(self) calcule le nombre de
            toilettes de la liste correspondant au critère de coût"""
        l=len(self.T)
        T=[]
        for i in range(l):
            if self.cout==0 and self.T[i][3]==None:
                T.append(self.T[i])
            if self.cout==1 and self.T[i][3]==True:
                T.append(self.T[i])
            if self.cout==2:
                T.append(self.T[i])
        self.T=T
    
    
    def nombreT_avec_horaires(self):
        """ nombreT_avec_horaires(self) calcule le nombre de
            toilettes de la liste correspondant au critère de temps"""
        global horaires
        l=len(self.T)
        T=[]
        indiceOuv=0
        indiceFerm=0
        for i in range(l):
            if self.T[i][0]==None and self.T[i][1]==None:
                T.append(self.T[i])
                self.compteur=self.compteur+1
            if self.T[i][0]!=None and self.T[i][1]!=None:
                L=len(horaires)
                for j in range(L):
                    if self.horaire==horaires[j]:
                        indiceSelect=j
                    if self.T[i][0]==horaires[j]:
                        indiceOuv=j
                    if self.T[i][1]==horaires[j]:
                        indiceFerm=j
                if indiceOuv!=0 and indiceFerm!=0 and indiceOuv<=indiceSelect<=indiceFerm:
                    T.append(self.T[i])
                    self.compteur=self.compteur+1
        self.T=T
                
    def localisation_T(self):
        """ localisation_T(self) crée des points de coordonnées qui seront
            ajoutés à la carte afin de voir où se trouvent les toilettes"""
        fmap =folium.Map(location=[45.764043,4.835659],zoom_start=10,tiles='OpenStreetMap')
        l=len(self.T)
        for i in range(l):
            folium.Marker((self.T[i][4],self.T[i][5]),popup='Toilette',icon=folium.Icon(color='blue')).add_to(fmap)    
        fmap.save('Carte_Toilettes.html')
        
# Programme principal

Toilettes=importation_donnees()

horaires=["05:00","05:30","06:00","06:30","07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30",
          "11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30",
          "17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30",
          "23:00","23:30","00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30","04:00","04:30"]


message1=tk.Label(fen,background='white',font=("arial italic",16),
                  text='Bienvenue sur le moteur de recherche\n des toilettes de la métropole de Lyon !')
message1.place(x=25,y=25)

message2=tk.Label(fen,background='white',font=("arial italic",12),
         text="Afin d'affiner votre recherche, sélectionner les critères qui correspondent aux votres ci-dessous :")
message2.place(x=25,y=150)

imagelogo=Image.open('logo-grand-lyon-la-metropole.png')
imagelogo=imagelogo.resize((427,88))
imagelogo=ImageTk.PhotoImage(imagelogo)
logo=tk.Label(fen,background='white',image=imagelogo)
logo.place(x=550,y=25)

imageR=Image.open('image_rechercher.png')
imageR=imageR.resize((183,72))
imageR=ImageTk.PhotoImage(imageR)
recherche=tk.Button(fen,image=imageR,command=lancement_recherche)
recherche.place(x=700,y=210)

Handi=tk.IntVar()
handi1=tk.Radiobutton(fen,text="Oui - Accès PMR*", width = 20,variable = Handi,value=1,bg="white")
handi1.place(x=25,y=200)

handi2=tk.Radiobutton(fen,text="Non - Accès PMR*", width = 20,variable = Handi,value=0,bg="white")
handi2.place(x=25,y=235)

handi3=tk.Radiobutton(fen,text="Oui ou non", width = 20,variable = Handi,value=2,bg="white")
handi3.place(x=25,y=270)

message3=tk.Label(fen,background='white',text="* Personne à Mobilité Réduite")
message3.place(x=25,y=370)

Cout=tk.IntVar()
cout1=tk.Radiobutton(fen,text="Uniquement gratuit", width = 20, variable = Cout,value=0,bg="white")
cout1.place(x=250,y=200)

cout2=tk.Radiobutton(fen,text="Uniquement payant", width = 20, variable = Cout,value=1,bg="white")
cout2.place(x=250,y=235)

cout3=tk.Radiobutton(fen,text="Gratuit ou payant", width = 20, variable = Cout,value=2,bg="white")
cout3.place(x=250,y=270)

Heure_select=tk.StringVar()
ListeDeroulante=tk.ttk.Combobox(fen, values=horaires)
ListeDeroulante.set("Sélectionnez l'heure")
ListeDeroulante['values']=horaires
ListeDeroulante.config(state='readonly')                         # met la zone de texte en lecture seule
ListeDeroulante.place(x=475,y=200)
ListeDeroulante.bind("<<ComboboxSelected>>",RecupValeur)
 
Quitter=tk.Button(master=fen, text='Quitter', command=quitter,bg='white',width=20)
Quitter.place(x=800,y=360)

root.mainloop()
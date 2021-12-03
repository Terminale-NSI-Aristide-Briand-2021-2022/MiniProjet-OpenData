################################################################################
    #Information :
################################################################################
"""
Auteur : Lebouvier Gaëtan & Le Gallic Gwilherm
Nom : LeGallic_Lebouvier_MiniProjet
Travail :
    Partie Gaëtan :
        - Partie Tkinter
        - Toute la recherche du jeu de données
        - Envoi de la requête vers l'API
        - Partie Fonctions

    Partie Gwilherm :
        - Création des classes POO
        - Partie Tkinter (Aide boutons)
        - Partie Fonctions
        - Toutes la partie commentaires et propreté du code
"""
################################################################################
    #Import :
################################################################################

import json
import requests
from tkinter import *

################################################################################
    #Envoi la requête au site pour avoir le jeu de données :
################################################################################
'''
reponse = requests.get('https://www.coronavirus-statistiques.com/corostats/openstats/open_stats_coronavirus.json')
print(reponse.text)

print("***********************************")
lecteurJSON = json.loads(reponse.text)
'''
f=open('open_stats_coronavirus.json','rt')
lecteurJSON=json.loads(f.read())

################################################################################
    #Programme Tkinter pour créer la fenêtre :
################################################################################

fenetre=Tk()                                                            #Créer la fenêtre
fenetre.attributes('-fullscreen', True)                                 #Met la fenêtre en fullscreen
fenetre.bind('<Escape>',lambda e: fenetre.destroy())                    #Sert à quitter en apuyant sur échappe en détruisant la fenêtre

canvas=Canvas(fenetre,width=800,height=400,background='white')          #Sert à avoir une zone pour le graphique
canvas.pack(fill="both",expand=True)

fenetre.title('Données Covid')                                          #Donne un nom à la fenêtre

################################################################################
    #Programme pour la création des 2 classes POO :
################################################################################

class Donnee:
    """
    Créer un objet avec comme attribut 'valeur' qui équivaut aux données qui nous intéressent qui sert pour les boutons Données
    """
    def __init__(self):
        self.val=''

    def quelleDonnee(self,don):
        self.val=don


class Pays:
    """
    Créer un objet avec comme attribut 'valeur' qui équivaut aux données qui nous intéressent et qui sert pour les butons Pays
    """
    def __init__(self):
        self.val=''

    def quelPays(self,don):
        self.val=don

################################################################################
    #Programme pour la création des fonctions pour créer le graphique en courbe :
################################################################################

def dessiner(pays):
    """
    Prend les valeurs et appelle la fonction graphique_courbe
    """
    try:
        assert pays!=''
        assert donnee.val!=''
    except:
        canvas.create_text(800,400,text="Sélectionnez un pays et une donnée avant d'appuyer sur le bouton !",font=('Arial',25))
        return None
    tab=[]                                                  #Met les valeurs dans la liste tab
    for objetJSON in lecteurJSON:                           #Regarde chaque objet dans le jeu de données
        if objetJSON['nom']==pays:                          #Si le nom du pays correspond :
            if objetJSON[donnee.val]!="":                   #Regarde si la donnée n'est pas vide
                tab.append(int(objetJSON[donnee.val]))      #Rajoute la valeur dans la liste tab
    graphique_courbe(tab)


def graphique_courbe(L):
    """
    Fonction qui sert à créer le graphique et l'échelle avec les valeurs prisent avec la fonction dessiner
    """
    mois=['02','03','04','05','06','07','08','09','10','11','12','01']
    canvas.delete("all")
    width=80
    height=730
    maxi=L[len(L)-1]
    echelle=maxi/(10**(len(str(maxi))))

    nbr=maxi//(10**(len(str(maxi))-1))
    print(nbr)
    print(echelle)
    print(maxi)
    canvas.create_line(80,maxi//100000,80,height)
    valEch=(echelle*10**(len(str(maxi))-1))
    valEch=int(valEch)
    texte=valEch
    i=1
    canvas.create_text(25,height,text=0)
    canvas.create_line(50,height,80,height)
    while texte<maxi:
        canvas.create_text(25,height-45*i,text=texte)
        canvas.create_line(50,height-45*i,80,height-45*i)
        texte=texte+valEch
        print(texte)
        i=i+1
    for i in range(23):
        if i<11:
            date=mois[i]+'/2020'
            canvas.create_text(70+i*(53),height+30,text=date)
        else:
            date=mois[i-12]+'/2021'
            canvas.create_text(70+i*(53),height+30,text=date)
    for n in L:
        canvas.create_rectangle(width,height,width-(1/(echelle*10**(len(str(maxi))-1))),height-(4.5/(echelle*10**(len(str(maxi))-2)))*n,fill="red")
        width=width+1.8
    print(maxi)


################################################################################
    #Programme Tkinter pour la création de boutons avec menu déroulant :
################################################################################

    #Instanciation des objets pays et donnee
pays=Pays()
donnee=Donnee()

    #Création du bouton pour afficher le graphique
bouton_courbe=Button(fenetre,text='Graphique en courbe',width=20,relief=RAISED,command=lambda: dessiner(pays.val))
bouton_courbe.pack(side=TOP,pady=10)

    #Création du bouton pour quitter en détruisant la fenêtre
bouton_quitter = Button(fenetre, text="Quitter ici",width=20,command=fenetre.destroy)
bouton_quitter.pack(side=BOTTOM,pady=10)

    #Création du bouton "Pays"
menuPays=Menubutton(canvas,text='Pays',width=20, relief=RAISED)
menuPays.grid(row=500,column=200)
    #Ouvre un menu déroulant avec 5 choix différents (5 pays : France / Italie / Royaume Uni / Espagne / Allemagne)
menuDeroulant=Menu(menuPays)
menuDeroulant.add_command(label='France',command=lambda: pays.quelPays('france'))
menuDeroulant.add_command(label='Italie',command=lambda: pays.quelPays('italie'))
menuDeroulant.add_command(label='Royaume Uni',command=lambda: pays.quelPays('uk'))
menuDeroulant.add_command(label='Espagne',command=lambda: pays.quelPays('espagne'))
menuDeroulant.add_command(label='Allemagne',command=lambda: pays.quelPays('allemagne'))

    #Création du bouton "Données"
menuDonnee=Menubutton(canvas, text='Données',width=20, relief=RAISED)
menuDonnee.grid(row=500,column=300)
    #Ouvre un menu déroulant avec 3 choix différents (3 données différentes : Cas totaux / Décès / Guérisons)
menuDeroulant1=Menu(menuDonnee)
menuDeroulant1.add_command(label='Cas totaux',command=lambda: donnee.quelleDonnee('cas'))
menuDeroulant1.add_command(label='Décès',command=lambda: donnee.quelleDonnee('deces'))
menuDeroulant1.add_command(label='Guérisons',command=lambda: donnee.quelleDonnee('guerisons'))

    #Sert à créer le menu déroulant
menuDonnee.configure(menu=menuDeroulant1)
menuPays.configure(menu=menuDeroulant)

    #Sert à maintenir la fenêtre et à vérifier chaque élément qui se passe à l'intérieur
fenetre.mainloop()
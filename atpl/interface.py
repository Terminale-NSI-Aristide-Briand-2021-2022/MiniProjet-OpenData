from tkinter import *
from random import *
from Recup_donnee_POO import *

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def graphique_secteurs(canvas,liste):
    """Graphique en camenbert"""
    canvas.delete("all")
    somme = sum(liste)
    debut_angle = 0
    hauteur=100
    r=0
    g=155
    b=194
    for x in liste:
        couleurc=_from_rgb((r,g,b))
        angle = x/somme*360 
        canvas.create_arc(200,100,550,450,start=debut_angle,extent=angle,style=PIESLICE,fill=couleurc)
        debut_angle = debut_angle + angle
        canvas.create_rectangle(560,hauteur,570,hauteur+10,width=1,fill=couleurc)
        hauteur= hauteur+20
        r=r+28
        g=g+8
        b=b-26
    canvas.create_text(650,105,text='Jeux pour enfants, soit '+ str(pourcentage(0))+" %",fill=_from_rgb((123,47,135)))
    canvas.create_text(660,125,text='Aires de pique-nique, soit '+ str(pourcentage(1))+" %",fill=_from_rgb((123,47,135)))
    canvas.create_text(620,145,text='Piscine, soit '+ str(pourcentage(2))+" %",fill=_from_rgb((123,47,135)))
    canvas.create_text(645,165,text='Centre equestre, soit '+ str(pourcentage(3))+" %",fill=_from_rgb((123,47,135)))
    canvas.create_text(625,185,text='Cinémas, soit '+ str(pourcentage(4))+" %",fill=_from_rgb((123,47,135)))
    canvas.create_text(675,205,text='Activité sportive et ludique, soit '+ str(pourcentage(5))+" %",fill=_from_rgb((123,47,135)))
        
    return

def action_bouton4(canvas,liste):
    canvas.delete("all")
    graphique_secteurs(canvas,liste)
    return

def graph(canvas,liste):
    """Graphique avec une barre par élément de la liste"""
    canvas.delete("all")
    echelle=2
    posx = 100
    r=0
    g=155
    b=194
    for x in liste:
        hauteur = x * echelle
        canvas.create_rectangle(posx,600,posx+10,600-hauteur,fill=_from_rgb((r,g,b)))
        posx = posx + 30
        r=r+42
        g=g+12
        b=b-40
    max_liste = max(liste)
    canvas.create_line(90,600,90,600-echelle*max_liste)   
    for j in range(0,max_liste+1,10):
        canvas.create_line(85,600-echelle*j,90,600-echelle*j,fill=_from_rgb((123,47,135)))
        canvas.create_text(80,600-echelle*j,text=str(j),fill=_from_rgb((123,47,135)))
    canvas.create_text(105,610,text="44",fill=_from_rgb((123,47,135)))
    canvas.create_text(135,610,text="49",fill=_from_rgb((123,47,135)))
    canvas.create_text(165,610,text="53",fill=_from_rgb((123,47,135)))
    canvas.create_text(195,610,text="72",fill=_from_rgb((123,47,135)))  
    return

""" Fichier principale
    Ce fichier gère tout les autres fichiers python"""

from tkinter import *
from DonneeTest import *
from Graphique import *
from PIL import ImageTk, Image
from Transition import Anim1
from random import *



root = Tk()
root.geometry("1200x850")
root.resizable(width=False, height=False)
root.config(background="grey")



#Variables Menu
Trans= BooleanVar(value=True)
Color = "blue"
ColorBg = "purple"

#Rechercher
Saisie = Entry(root,width=30)
Saisie.place(x=10,y=50)




#Label Nom du pays
NomPays = Label(text="Pays :",font=20)
NomPays.place(x=400,y=100)





#Boutons
frame = Frame(root,width = 50,height =25)
frame.place(x=10,y=140)

frameGraph = Canvas(root,width = 800,height =625,bg="purple")
frameGraph.place(x=200,y=140)

btn1 = Button(frame,text='1')
btn2 = Button(frame,text='2')
btn3 = Button(frame,text='3')
btn4 = Button(frame,text='4')
btn5 = Button(frame,text='5')
btn6 = Button(frame,text='6')
btn7 = Button(frame,text='7')
Bouton = [btn1,btn2,btn3,btn4,btn5,btn6,btn7]


#Fonctions lorsque l'on clique sur un bouton
def ClickBouton(Info,n):
    global DonneesActuel
    global Color
    global Trans
    DonneesActuel = (Info,n)

    donnees = []
    for i in range(4,65,5):
        donnees.append(Info[n][i])
    if Trans.get():
        if Info[n][0] == "France":
            a=randint(1,2)
            Anim = Anim1("Images/Poule"+str(a)+".png",frameGraph)
            Anim.transition()
        else:
            a=randint(1,3)
            Anim = Anim1("Images/Img"+str(a)+".png",frameGraph)
            Anim.transition()
    graphique_barres(donnees,frameGraph,Color)
    NomPays.config(text="Pays: "+Info[n][0])

#Fonction recherche
def RechercheBouton():
    """ Permet de récupérer le champs de saisie et afficher
         les boutons de pays correspondant à ce texte """
    for i in Bouton:
        i.pack_forget()
    a=Saisie.get().lower()
    if a == "":
        a="a"
    C=Pays(a) # Attribut à une variable C la liste des pays correspondant à la Recherche
    n=len(C)
    if n>7:
        n=7 #Si n est supérieur à 7 alors on attribut 7 à n afin que la boucle soit de 7 itération maximum ( Où 7 est le nombre de boutons total)
    for j in range(n):
        if j == 0:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,0))
        elif j == 1:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,1))
        elif j == 2:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,2))
        elif j == 3:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,3))
        elif j == 4:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,4))
        elif j == 5:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,5))
        elif j == 6:
            Bouton[j].config(text=C[j][0],command=lambda: ClickBouton(C,6))
        Bouton[j].pack()

#Nouvelle fenêtre Pour le graphique de la Population Mondiale
def top():
    t = Toplevel()
    t.title("graphique total")
    t.geometry("800x600")
    t.resizable(width=False, height=False)
    frameGrapht = Canvas(t,width = 800,height =600,bg="grey")
    frameGrapht.place(x=0,y=0)
    C=Pays("world")
    donnees=[]
    NomPays = Label(t,text="Population Mondiale ",font=20,bg="orange")
    NomPays.place(x=300,y=20)
    for i in range(4,65,5):
        donnees.append(C[0][i])
    graphique_barres(donnees,frameGrapht)


def SetColorRec(C="blue"):
    global Color
    global ColorBg
    global DonneesActuel
    global Trans
    if ColorBg != C:
        Color = C
    if DonneesActuel == 0:
        return False
    else:
        if Trans.get():
            Trans.set(False)
            ClickBouton(DonneesActuel[0],DonneesActuel[1])
            Trans.set(True)
        else:
            ClickBouton(DonneesActuel[0],DonneesActuel[1])

def SetColorBg(C="purple"):
    global ColorBg
    global Color
    if C != Color:
        ColorBg = C
    frameGraph.config(bg=ColorBg)

def CouleurOp():
    global Color
    C= Toplevel()
    C.title("Option Couleur")
    C.geometry("200x530")
    C.config(background="grey")
    C.resizable(width=False, height=False)
    TextRec = Label(C,text="Changer Couleur rectangles :")
    TextRec.place(x=10,y=30)
    TextRec.pack()

    ColorFrame = Frame(C,width = 500,height =10,bg="grey")
    ColorFrame.place(x=20,y=50)
    ColorFrame.pack()

    Blue = Button(ColorFrame,text="   ",bg="blue",command= lambda : SetColorRec("blue"))
    Red= Button(ColorFrame,text="   ",bg="red",command= lambda : SetColorRec("red") )
    Green= Button(ColorFrame,text="   ",bg="green",command= lambda : SetColorRec("green"))
    Purple= Button(ColorFrame,text="   ",bg="purple",command= lambda : SetColorRec("purple"))
    Pink= Button(ColorFrame,text="   ",bg="pink",command= lambda : SetColorRec("pink") )
    Brown= Button(ColorFrame,text="   ",bg="brown",command= lambda : SetColorRec("brown"))
    Orange= Button(ColorFrame,text="   ",bg="Orange",command= lambda : SetColorRec("Orange"))
    Yellow= Button(ColorFrame,text="   ",bg="Yellow",command= lambda : SetColorRec("Yellow"))
    Grey= Button(ColorFrame,text="   ",bg="grey",command= lambda : SetColorRec("grey"))
    Color=[Blue,Red,Green,Purple,Pink,Brown,Orange,Yellow,Grey]
    for element in Color:
        element.pack()
    TextBg = Label(ColorFrame,text="Changer Couleur Arrière plan :")
    TextBg.pack()

    BlueBg = Button(ColorFrame,text="   ",bg="blue",command= lambda : SetColorBg("blue"))
    RedBg= Button(ColorFrame,text="   ",bg="red",command= lambda : SetColorBg("red") )
    GreenBg= Button(ColorFrame,text="   ",bg="green",command= lambda : SetColorBg("green"))
    PurpleBg= Button(ColorFrame,text="   ",bg="purple",command= lambda : SetColorBg("purple"))
    PinkBg= Button(ColorFrame,text="   ",bg="pink",command= lambda : SetColorBg("pink") )
    BrownBg= Button(ColorFrame,text="   ",bg="brown",command= lambda : SetColorBg("brown"))
    OrangeBg= Button(ColorFrame,text="   ",bg="Orange",command= lambda : SetColorBg("Orange"))
    YellowBg= Button(ColorFrame,text="   ",bg="Yellow",command= lambda : SetColorBg("Yellow"))
    GreyBg= Button(ColorFrame,text="   ",bg="grey",command= lambda : SetColorBg("grey"))
    ColorBg=[BlueBg,RedBg,GreenBg,PurpleBg,PinkBg,BrownBg,OrangeBg,YellowBg,GreyBg]
    for element in ColorBg:
        element.pack()



#Menu
mainMenu = Menu(root)

menu1 = Menu(mainMenu,tearoff=0)
menu1.add_command(label="Changer couleur",command=CouleurOp) #Ouvre une nouvelle fenêtre pour choisir la couleur de changement
menu1.add_checkbutton(label="Transition", underline=0, variable=Trans, onvalue=True, offvalue=False)


mainMenu.add_cascade(label="Option", menu=menu1)


#Recherche
Recherche = Button(root,text="Rechercher",width=10,command=RechercheBouton)
Recherche.place(x=220,y=50)
ResultText = Label(root,text="Résultat :")
ResultText.place(x=10,y=120)
total = Button(root,text="graphique total",width=15,command=top)
total.place(x=1050,y=740)
DonneesActuel = 0
RechercheBouton()






root.config(menu=mainMenu)
root.mainloop()
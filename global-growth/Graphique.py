
from random import *
from tkinter import *





def maxi(liste):
    n=len(liste)
    a=0
    for i in range(n):
        if int(liste[i])>a:
            a=int(liste[i])
    return a


def graphique_barres(liste,canvas,Crect="blue"):
    """Graphique avec une barre par élément de la liste
       Avec comme paramètre: La couleur des barres : Crect
                             Le canvas ou sera affiché le graphique
                             La liste de données du pays"""
    canvas.delete("all")
    a=0
    Ox = 100
    Oy=550
    years=1960
    max = maxi(liste)
    for element in liste:
        element = int(element)
        taille=(element * 500)/max
        canvas.create_rectangle(Ox+a,Oy,Ox+a+5,Oy-taille,width=10, outline=Crect)
        canvas.create_text(Ox+a,Oy+15,font=('Arial',8),text=str(years),fill="white")
        a =a +50
        years= years +5
    b = ((max/10)*500)/max
    for i in range(11):
        if i == 10:
            canvas.create_text(Ox-50,50+i*b,font=('Arial',8),text=str(0)+"-",fill="black")
        if i == 0:
            canvas.create_text(Ox-50,20+i*b,font=('Arial',8),text="Nombre d'habitant :",fill="white")
            canvas.create_text(Ox-50,50+i*b,font=('Arial',8),text=str(max-(max//10)*i)+"-",fill="black")
        else:
            canvas.create_text(Ox-50,50+i*b,font=('Arial',8),text=str(max-(max//10)*i)+"-",fill="black")


if __name__ == "__main__":
    root = Tk()
    root.geometry("1200x800")

    GraphFrame = Frame(root)
    GraphFrame.place(x=250, y=100)
    canvas = Canvas(GraphFrame, width=800, height=600, background="grey")
    canvas.pack()

    liste = [randint(1,999999999) for i in range(13)]
    graphique_barres(liste,canvas)

    root.mainloop()
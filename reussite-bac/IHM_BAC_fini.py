from tkinter import*
from Graph_Bac import*

OriginList = [
"Agriculteurs exploitants",
"Autres personnes sans activité professionnelle",
"Artisans, commerçants, chefs d'entreprise",
"Cadres, professions intellectuelles supérieures",
"Cadres, professions intellectuelles supérieures : professeurs et assimilés",
"Employés",
"Ensemble",
"Indéterminé",
"Ouvriers",
"Professions intermédiaires",
"Professions intermédiaires : instituteurs et assimilés",
"Retraités"
]
Info =[
"pourcentage d'admis au baccalaureat","pourcentage d'admis au baccalaureat general",
"pourcentage d'admis au baccalaureat technologique",
"pourcentage d'admis au baccalaureat professionel"]
An1List = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
root=Tk()
root.geometry('600x500')
root.title("Représentations graphiques des résultats de BAC")
root.iconbitmap("Icone_Tk.ico")
root.resizable(width=False, height=False)


def action_barre():
    """
    Fonction qui s'active lors d'une interaction avec bouton_graph

    parametre : aucun
    resultat : attribution des valeurs des différents boutons et entrées de l'IHM dans des variables
                appel de la méthode attribut() ayant pour parametre les variables précédentes
                puis appel de la méthode Barre()
    """
    ori=variable0.get()
    an1=int(variable1.get())
    an2=int(variable2.get())
    dn=variable3.get()
    nm=Nom.get()
    graph.attribut(ori,an1,an2,dn,nm)
    graph.Barre()

def action_courbe():
    """
    Fonction qui s'active lors d'une interaction avec bouton_graph2

    parametre : aucun
    resultat : attribution des valeurs des différents boutons et entrées de l'IHM dans des variables
                appel de la méthode attribut() ayant pour parametre les variables précédentes
                puis appel de la méthode Courbe()
    """
    ori=variable0.get()
    an1=int(variable1.get())
    an2=int(variable2.get())
    dn=variable3.get()
    nm=Nom.get()
    graph.attribut(ori,an1,an2,dn,nm)
    graph.Courbe()


variable0 = StringVar(root)
variable0.set(OriginList[0])

variable1 = StringVar(root)
variable1.set(An1List[0])

variable2 = StringVar(root)
variable2.set(An1List[0])

variable3 = StringVar(root)
variable3.set(Info[0])

Indic3 = Label(root,text="↓ Veuillez sélectionner l'information désirée: ↓",font = ('Ubuntu Condensed', '12', 'bold'))
Indic3.place(x = 120, y = 80)

Info=OptionMenu(root, variable3,*Info)
Info.place(x = 175, y = 110)

Indic1 = Label(root,text="↓ Veuillez sélectionner la classe sociale désirée: ↓",font = ('Ubuntu Condensed', '12', 'bold'))
Indic1.place(x = 105, y = 150)


origine = OptionMenu(root, variable0,*OriginList)
origine.place(x = 215, y = 180)

Indic2 = Label(root,text="↓ Veuillez entrer la période désirée: ↓",font = ('Ubuntu Condensed', '12', 'bold'))
Indic2.place(x = 150, y = 220)

an1=OptionMenu(root, variable1,*An1List)
an1.place(x = 232, y = 255)

an2=OptionMenu(root, variable2,*An1List)
an2.place(x = 298, y = 255)

Nom=Entry(root,font = ('Ubuntu Condensed','10', 'bold'))
Nom.place(x = 228, y = 310)
Nom.insert(0,"Nom_du_Graphique")

bouton_graph = Button(root,text="Graphique Barre", width=14, command=action_barre)
bouton_graph.place(x = 300, y = 350)

bouton_graph2 = Button(root,text="Graphique Courbe", width=14, command=action_courbe)
bouton_graph2.place(x = 190, y = 350)

bouton_quitter = Button(root,text="Quitter", width=8, command=root.destroy)
bouton_quitter.place(x = 265, y = 470)


root.mainloop()
from tkinter import *
from interface import *
from Recup_donnee_POO import *

#Differentes valeurs prises pour la liste déroulante
OptionList = ["Cinéma","Centre équestre","Piscine","Activités sportives et ludiques","Aire de pique-nique","Jeux pour enfants"]

app = Tk()
app.geometry('1000x800')

#Zone de dessin
canvas = Canvas(app,width=500, height=700, background="white")
canvas.pack(side=LEFT, fill="both", expand=True)

#Bouton pour le total
Total = Button(app, text="Nombre de centre d'activité", width=30,command=lambda: graphique_secteurs(canvas,NombreTotal_par_Activite()))
Total.pack(pady=10)

#Selection pour le bouton déroulant
variable = StringVar(app)
variable.set("Choisir une activité")

#Bouton quitter
bouton_quitter = Button(app,text="Quitter", width=20,command=app.destroy)
bouton_quitter.pack(side=BOTTOM, pady=10)

#Liste déroulante
opt = OptionMenu(app, variable, *OptionList)
opt.config(width=30)
opt.pack(side=TOP, pady=10)

#Zone de texte pour la selection
labelTest = Label(text="")
labelTest.pack(side="top")

#Fonction pour appeler le graph 
def callback(*args):
    graph(canvas,NombreActivite_par_CodePostal(variable.get()))

#Action de bouton
variable.trace("w", callback)


app.mainloop()
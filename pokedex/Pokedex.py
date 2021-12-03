# Créé par Gaby, le 24/11/2021 en Python 3.7


#________________________Import des modules et des librairies________________________
from tkinter import*
import requests, json
from PIL import ImageTk,Image


#________________________Construction de la fenêtre de base________________________
root = Tk()
w, h = 640, 800                                                 # dimensions de base de la fenêtre
root.title("PokéDex by Goby & Tom")                             # titre de la fenêtre
root.maxsize(640, 800)                                          # on bloque les dimensions de la fenêtre
root.minsize(640, 800)
root.iconbitmap('pokeball.ico')                                 # ajout de l'icône de la fenêtre

image = PhotoImage(file='pokedex.png', master=root)             # import du fond de la fenêtre
canvas = Canvas(root, width=w, height=h)
canvas.create_image((w//2, h//2), image=image)
canvas.pack()


#________________________Position des boutons________________________
echage = PhotoImage(file = r"echange.png")                      # import de l'image du bouton échange
Echange = echage.subsample(3, 3)

haut = PhotoImage(file = r"haut.png")                           # import de l'imahe du bouton haut
Haut = haut.subsample(3, 3)

bas = PhotoImage(file = r"Bas.png")                             # import de l'image du bouton bas
Bas = bas.subsample(3, 3)

on_off = PhotoImage(file = r"on_off.png")                       # import de l'image du bouton on/off
onoff = on_off.subsample(3, 3)


#________________________Fonctions________________________
def affichage_numéro(n:int)->str:
    """
    Paramètre : n est un entier représentant le numéro du pokémon
    Résultat : renvoie No.n sous la forme d'une chaîne de caractères (le nombre de zéros s'adapte à la valeur de n)
    """
    if n >=100:
        x='No. '+str(n)
    elif n >=10:
        x='No. 0'+str(n)
    else:
        x='No. 00'+str(n)
    return x

def slide(n:int):
    """
    Paramètre : n est le numéro du pokémon choisi sur le slider
    Résultat : charge la fiche du pokémon correspondant au numéro choisi sur le slider
    """
    x = vertical.get()
    if x > n:
        forward(n,x-n)
    elif x < n:
        back(n,n-x)


def delete_(nom):
    """
    Paramètre : nom est un élément affiché dans la fenêtre
    Résultat : supprime nom
    """
    nom.destroy()


def forward(n:int,z=1):
    """
    Paramètres : n est le numéro du pokémon
    Résultat : va au pokémon suivant (actualisation de toutes les valeurs)
    """
    global label_image
    global button_forward
    global button_back
    global text_num
    global text_nom
    global image_type1
    global image_type2
    global label_type1
    global label_type2

    n = n + z
    types=Type(n)

    delete_(text_num)
    delete_(text_nom)
    delete_(label_type1)
    delete_(label_type2)

    label_image = Label(image=image_list[n-1])
    label_image.place(x=83, y=130)

    text_num= Label(root,text=affichage_numéro(n), font=('Helvetica bold',40))
    text_num.place(x=50, y=40)

    text_nom= Label(root,text=listName[n-1], font=('Helvetica bold',40))
    text_nom.place(x=50, y=100)

    button_forward = Button(root, bg='#4a5252', image = Bas, command=lambda: forward(n))
    button_forward.place(x=195, y=710)

    button_back = Button(root, bg='#4a5252', image = Haut, command=lambda: back(n))
    button_back.place(x=195, y=553)

    my_btn = Button(root, image = Echange, command=lambda: slide(n))
    my_btn.place(x=62, y=390)

    types=Type(n)                                                                           # gestion des types
    image_type1 = ImageTk.PhotoImage(Image.open(str(types.idImage()[1])))
    label_type1 = Label(image = image_type1)
    label_type1.place(x=400, y=230)
    if types.tab[0]==2:
        image_type2 = ImageTk.PhotoImage(Image.open(str(types.idImage()[2])))
        label_type2 = Label(image = image_type2)
        label_type2.place(x=400, y=300)

    if n == 151:                                                                            # désactive le bouton si on est au dernier pokémon
        button_forward = Button(root, bg='#4a5252', image = Bas, state=DISABLED)
        button_forward.place(x=195, y=710)

def back(n,z=1):
    """
    Paramètres : n est le numéro du pokémon
    Résultat : va au pokémon précédent (actualisation de toutes les valeurs)
    """
    global label_image
    global button_forward
    global button_back
    global text_num
    global text_nom
    global image_type1
    global image_type2
    global label_type1
    global label_type2

    n = n - z

    delete_(text_num)
    delete_(text_nom)
    delete_(label_type1)
    delete_(label_type2)

    label_image = Label(image=image_list[n-1])
    label_image.place(x=83, y=130)

    text_num= Label(root,text=affichage_numéro(n), font=('Helvetica bold',40))
    text_num.place(x=50, y=40)

    text_nom= Label(root,text=listName[n-1], font=('Helvetica bold',40))
    text_nom.place(x=50, y=100)

    button_forward = Button(root, bg='#4a5252', image = Bas, command=lambda: forward(n))
    button_forward.place(x=195, y=710)

    button_back = Button(root, bg='#4a5252', image = Haut, command=lambda: back(n))
    button_back.place(x=195, y=553)

    my_btn = Button(root, image = Echange, command=lambda: slide(n))
    my_btn.place(x=62, y=390)

    types=Type(n)                                                                           # gestion des types
    image_type1 = ImageTk.PhotoImage(Image.open(types.idImage()[1]))
    label_type1 = Label(image = image_type1)
    label_type1.place(x=400, y=230)
    if types.tab[0]==2:
        image_type2 = ImageTk.PhotoImage(Image.open(types.idImage()[2]))
        label_type2 = Label(image = image_type2)
        label_type2.place(x=400, y=300)

    if n == 1:                                                                              # désactive le bouton si on est au premier pokémon
        button_back = Button(root, bg='#4a5252', image = Haut, state=DISABLED)
        button_back.place(x=195, y=553)


#________________________Classe________________________
class Type:
    """
    Classe utilisée pour gérer les types de chaque pokémon
    """
    def __init__(self,n):
        self.lienPkmn=requests.get('https://pokeapi.co/api/v2/pokemon/'+str(n))
        self.tab=json.loads(self.lienPkmn.text)
        self.tab=self.tab['types']
        self.nbType=len(self.tab)
        if self.nbType==1:
            self.tab=1,self.tab[0]['type']['name']
        else:
            self.tab0=self.tab[0]['type']['name']
            self.tab1=self.tab[1]['type']['name']
            self.tab=2,self.tab0,self.tab1

    def idImage(self):
        """
        Résultat : renvoie le nombre de types du pokémon, puis l'adresse de chaque type sous la forme d'une chaîne de caractères
        """
        if self.nbType==1:
            return self.nbType,'Types/'+self.tab[1]+'.png'
        else:
            return self.nbType,'Types/'+self.tab[1]+'.png','Types/'+self.tab[2]+'.png'


#________________________Programme principal________________________
r=requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')                                                   # import des noms des 151 premiers pokémon
tabjson=json.loads(r.text)
tabjson=tabjson['results']

n=1                                                                                                             # on commence avec le pokémon n°1

vertical = Scale(root, from_=1, to=151)                                                                         # création du slider permettant de choisir le numéro du pokémon
vertical.place(x=42, y=190)

image_list=[]
for i in range(151):                                                                                            # import de toutes les images des pokémon dans la liste image_list
    user_input = "my_img"+str(i+1)
    globals()[user_input] = ImageTk.PhotoImage(Image.open("Sprites/"+str(i+1)+".png").resize((300, 300)))
    image_list.append(globals()[user_input])

label_image = Label(image=my_img1)                                                                              # position de l'image du premier pokémon
label_image.place(x=83, y=130)

listName=[]
for pokemon in tabjson:                                                                                         # ajout des noms de tous les pokémon dans la liste listName
    listName.append(pokemon['name'])

text_nom= Label(root,text=listName[n-1], font=('Helvetica bold',40))                                            # position du Label du nom du premier pokémon
text_nom.place(x=50, y=100)

types=Type(n)                                                                                                   # affichage des types du premier pokémon
image_type1 = ImageTk.PhotoImage(Image.open(types.idImage()[1]))
label_type1 = Label(image = image_type1)
label_type1.place(x=400, y=230)
image_type2 = ImageTk.PhotoImage(Image.open(types.idImage()[2]))
label_type2 = Label(image = image_type2)
label_type2.place(x=400, y=300)

text_num= Label(root,text=affichage_numéro(n), font=('Helvetica bold',40))                                      # position du numéro du premier pokémon
text_num.place(x=50, y=40)

my_btn = Button(root, image = Echange, command=lambda: slide(n))                                                # position du bouton actualiser
my_btn.place(x=62, y=390)

button_back = Button(root, bg='#4a5252', image = Haut, command=back, state=DISABLED)                            # position du bouton back
button_back.place(x=195, y=553)

button_forward = Button(root,bg='#4a5252', image = Bas, command=lambda: forward(1))                             # position du bouton forward
button_forward.place(x=195, y=710)

Bouton_quitter = Button(root,bg='#4a5252', image = onoff,command=root.destroy)                                   # position du bouton quitter
Bouton_quitter.place(x=525, y=685)

root.mainloop()                                                                                                 # lancement de la fenêtre tkinter
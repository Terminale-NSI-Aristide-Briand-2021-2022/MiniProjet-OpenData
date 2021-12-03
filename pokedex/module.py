# Créé par Gaby, le 24/11/2021 en Python 3.7
from tkinter import*
import requests, json
from PIL import ImageTk,Image
root = Tk()
w, h = 640, 800
root.title("PokéDex by Goby & Tom")               # titre
root.maxsize(640, 800)
root.minsize(640, 800)
root.iconbitmap('pokeball.ico')

image = PhotoImage(file='pokedex.png', master=root)
canvas = Canvas(root, width=w, height=h)
canvas.create_image((w//2, h//2), image=image)
canvas.pack()

r=requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
tabjson=json.loads(r.text)
tabjson=tabjson['results']

n=1 #valeur de base du pokemon choisi

echage = PhotoImage(file = r"echange.png")
Echange = echage.subsample(3, 3)

haut = PhotoImage(file = r"haut.png")              # prend les images des boutons
Haut = haut.subsample(3, 3)

bas = PhotoImage(file = r"Bas.png")
Bas = bas.subsample(3, 3)

on_off = PhotoImage(file = r"on_off.png")
onoff = on_off.subsample(3, 3)

image_list=[]

listName=[]

# ________________Fonctions________________

def affichage_numéro(n):
    if n >=100:
        x='No. '+str(n)
    elif n >=10:
        x='No. 0'+str(n)
    else:
        x='No. 00'+str(n)
    return x

def slide(n):
    x = vertical.get()
    if x > n:
        forward(n,x-n)
        print(n)

    elif x < n:
        back(n,n-x)
        print(n)



def delete_text(nom):
   nom.destroy()

# ________________Fonctions________________



for i in range(151):
    user_input = "my_img"+str(i+1)
    globals()[user_input] = ImageTk.PhotoImage(Image.open("Sprites/"+str(i+1)+".png").resize((300, 300)))
    image_list.append(globals()[user_input])

label_image = Label(image=my_img1)
label_image.place(x=83, y=130)


for pokemon in tabjson:
    listName.append(pokemon['name'])

text_nom= Label(root,text=listName[n-1], font=('Helvetica bold',40))
text_nom.place(x=50, y=100)




def forward(n,z=1):
	global label_image
	global button_forward
	global button_back
	global text_num
	global text_nom

	n = n + z

	delete_text(text_num)
	delete_text(text_nom)
	label_image = Label(image=image_list[n-1])
	text_num= Label(root,text=affichage_numéro(n), font=('Helvetica bold',40))
	text_nom= Label(root,text=listName[n-1], font=('Helvetica bold',40))
	button_forward = Button(root, bg='#4a5252', image = Bas, command=lambda: forward(n))
	button_back = Button(root, bg='#4a5252', image = Haut, command=lambda: back(n))
	my_btn = Button(root, image = Echange, command=lambda: slide(n))
	text_nom.place(x=50, y=100)
	text_num.place(x=50, y=40)
	my_btn.place(x=62, y=390)
	label_image.place(x=83, y=130)
	button_back.place(x=195, y=553)
	button_forward.place(x=195, y=710)
	print(n,'for')

	if n == 151:
		button_forward = Button(root, bg='#4a5252', image = Bas, state=DISABLED)





def back(n,z=1):
	global label_image
	global button_forward
	global button_back
	global text_num
	global text_nom

	n = n - z

	delete_text(text_num)
	delete_text(text_nom)
	label_image = Label(image=image_list[n-1])
	text_num= Label(root,text=affichage_numéro(n), font=('Helvetica bold',40))
	text_nom= Label(root,text=listName[n-1], font=('Helvetica bold',40))
	button_forward = Button(root, bg='#4a5252', image = Bas, command=lambda: forward(n))
	button_back = Button(root, bg='#4a5252', image = Haut, command=lambda: back(n))
	my_btn = Button(root, image = Echange, command=lambda: slide(n))
	my_btn.place(x=62, y=390)
	label_image.place(x=83, y=130)
	button_back.place(x=195, y=553)
	button_forward.place(x=195, y=710)
	text_num.place(x=50, y=40)
	text_nom.place(x=50, y=100)
	print(n,'back')



	if n == 1:
		button_back = Button(root, bg='#4a5252', image = Haut, state=DISABLED)








vertical = Scale(root, from_=1, to=151)
vertical.place(x=42, y=190)

text_num= Label(root,text=affichage_numéro(n), font=('Helvetica bold',40))
text_num.place(x=50, y=40)

my_btn = Button(root, image = Echange, command=lambda: slide(n))
my_btn.place(x=62, y=390)

button_back = Button(root, bg='#4a5252', image = Haut, command=back, state=DISABLED)
button_forward = Button(root,bg='#4a5252', image = Bas, command=lambda: forward(1))

button_back.place(x=195, y=553)
button_forward.place(x=195, y=710)

Bouton_qutter = Button(root,bg='#4a5252', image = onoff,command=root.destroy)
Bouton_qutter.place(x=525, y=685)


root.mainloop()

from random import *
from tkinter import *
from PIL import ImageTk, Image
from time import *



class Anim1:
    def __init__(self,img,canvas):
        self.image = Image.open(img)
        self.posx = -1100
        Pic = ImageTk.PhotoImage(self.image)
        self.image_label = Label(canvas,image=Pic,borderwidth=0)
        self.image_label.image = Pic

    def transition(self):
        self.posx = self.posx + 20
        if self.posx <= 820:
            self.image_label.place(x=self.posx, y=0)
            self.image_label.after(10,self.transition)
        else:
            self.posx = -1100

    def move(self,x=0,y=0):
        self.image_label.place(x=x, y=y)

class Anim2:
    def __init__(self,color):
        self.color = color
        Trans = []
        for i in range(5):
            Trans.append(canvas.create_rectangle(0,0+i*120,0+i*160,0+(i+1)*120,width=10, outline="blue"))





if __name__ == "__main__":

    root = Tk()
    root.geometry("1000x700")

    canvas = Canvas(root, width=800, height=600, background="grey")
    canvas.pack()

    #img = Image.open("Images/Poule1.png")



    Poule1 = Anim1("Images/Poule1.png")
    Poule2 = Anim1("Images/Poule2.png")
    #test=Anim2(None)

    Bouton1 = Button(root,text="Poule 1",command=Poule1.transition)
    Bouton2 = Button(root,text="Poule 2",command=Poule2.transition)
    Bouton1.pack()
    Bouton2.pack()


    root.mainloop()

# ================ IMPORT ================ #
from pandas import DataFrame
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Button, Canvas, Event, Listbox, Label, Tk
from tkinter.constants import BOTH, LEFT, NORMAL, DISABLED

# ============= LOCAL IMPORT ============= #
from cogs.player_data import DATAS
from utils.logger import Logger
from utils.tri import tri

# ================ CLASS ================= #
class CustomWindow:
  def __init__(self, screen: Tk, data: DataFrame) -> None:
    """Constructor

    Args:
        screen (Tk): The Tkinter windows
        data (DataFrame): Our datas
    """
    # Initialisation of the attributs
    LOG.debug("Initialisation")

    # Attributs
    self.screen = screen
    self.data = data
    self.item = "Temps de jeu"
    self.type = "graphic"
    self.w = None
    
    # Buttons creations
    self.classmentButton = Button(self.screen, text="Classement", state = NORMAL, command=self.classment)
    self.graphicButton = Button(self.screen, text="Graphique", state = NORMAL, command=self.graphic)
    
    # Buttons placement
    self.graphicButton.place(x=700, y=100)
    self.classmentButton.place(x=700, y=150)

    # Liste creation
    listTypes = Listbox(self.screen, background=COLORS["GREY"], bd=0, highlightthickness=0)
    DATATYPES = list(FINALDATAS.keys())
    DATATYPES.pop(0)
    for i in range(len(DATATYPES)):
      listTypes.insert(i + 1, DATATYPES[i])
    
    # List event linking
    def onselect(evt: Event):
      self.item = evt.widget.get(int(evt.widget.curselection()[0]))
      self.execute()
    listTypes.bind('<<ListboxSelect>>', onselect)
    
    # List and its corresponding text placement
    listTypes.place(x=700, y=325, width=200)
    Label(text="Choisissez l'action que vous voulez voir :", background=COLORS["GREY"]).place(x=700, y=300)
    
    # At launch we will see the graph
    self.graphic()
  
  def execute(self):
    """
    Run the needed view with the type
    """
    LOG.debug(f"Clicked an item: Type = {self.type} | Item = {self.item}")
    if self.type == "graphic":
      self.graphic()
    else:
      self.classment()

  def graphic(self):
    """
    Graphic view
    """
    LOG.debug(f"Changement to graphic: Type = {self.type} | Item = {self.item}")
    self.type = "graphic"
    
    # We invert the buttons state
    self.graphicButton['state'] = DISABLED
    self.classmentButton['state'] = NORMAL
    
    # Destroy the previous widget (canvas or figure)
    if self.w is not None: 
      self.w.destroy()
    
    # Creation of the figure and set it's color
    graphicFigure = Figure(figsize=(9, 5), dpi=60)
    graphicFigure.set_facecolor(COLORS["RED"])
    # "111" mean it's a graphic (cf mathplotlib doc)
    axe = graphicFigure.add_subplot(111)
    
    # This convert mathplotlib item into tkinter item (aka magic stuff)
    graphic = FigureCanvasTkAgg(graphicFigure, self.screen)
    self.w = graphic.get_tk_widget()
    self.w.pack(side=LEFT, fill=BOTH)
    
    # Import of the datas into the figure
    datas = self.data[["Joueur", self.item]].groupby("Joueur").sum()
    # Set the type of graphic to bar and link it to the ax
    datas.plot(kind="bar", legend=None, ax=axe, color=COLORS["BLACK_RED"])
    
    # Title
    axe.set_title(f"{self.item} des joueurs de KaniPlayers")
    axe.set_facecolor(COLORS["RED"])
  
  def classment(self):
    """
    Classment view
    """
    LOG.debug(f"Changement to classment: Type = {self.type} | Item = {self.item}")
    self.type = "classment"
    
    # We invert the buttons state
    self.graphicButton['state'] = NORMAL
    self.classmentButton['state'] = DISABLED
    
    # Destroy the previous widget (see up)
    if self.w is not None: 
      self.w.destroy()
    
    # Canvas creation and placement
    self.w = Canvas(self.screen, width=550, height=1100, background=COLORS["RED"], bd=0, highlightthickness=0)
    self.w.place(x=-10, y=-10)
    
    # Title
    self.w.create_text(275, 50, text= f"{self.item} des joueurs de KaniPlayers", font = ('Lucida', '16'), fill=COLORS["BLACK"])
    
    # Creation of the classment
    TEXT = ""
    FinalList = tri(FINALDATAS, self.item)
    for i in range(len(FinalList)):
      TEXT += f"\n\n• #{i+1}   {FinalList[i][0]}       avec {FinalList[i][1]}"
      if self.item == "Temps de jeu":
        TEXT += " minutes"

    # We view the classment
    self.w.create_text(270, 320, text=TEXT, justify = LEFT, font = ('Helvetica', '16'), fill=COLORS["BLACK"])

# =============== CONSTANTS ============== #

LOG = Logger(False) # The boolean in it represente if he is in debug mode or not
                    # it's just to see debug info in the console
FINALDATAS = {
  "Joueur": [d.name for d in DATAS],
  "Minerais de Netherite minés": [d.netheriteMine for d in DATAS],
  "Temps de jeu": [d.playTime for d in DATAS],
  "Morts": [d.deaths for d in DATAS],
  "Sauts": [d.jump for d in DATAS],
  "Entités tuées": [d.totalKills for d in DATAS],
  "Dégats pris": [d.damageTaken for d in DATAS],
  "Coffres ouverts": [d.chestOpened for d in DATAS]
}
DATAFRAME = DataFrame(FINALDATAS, columns=list(FINALDATAS.keys()))
COLORS = {
  "BLACK_RED": "#591a20",
  "RED": "#8e0000",
  "BLACK": "#1A1616",
  "GREY": "#756969"
}
SCREEN = Tk()

# ================ LAUNCH ================ #

CustomWindow(SCREEN, DATAFRAME)
SCREEN.title("KaniPlayers' Stats")
SCREEN.geometry("1000x700")
SCREEN.configure(background=COLORS["GREY"])
SCREEN.iconbitmap("img/kaniplayers.ico")
SCREEN.mainloop()

# And we launch the window ~~(with Windows)~~
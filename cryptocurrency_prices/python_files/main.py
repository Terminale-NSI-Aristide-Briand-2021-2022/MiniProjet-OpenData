import tkinter as tk
from PIL import ImageTk, Image
from python_files.scrolling_menus import gen_menus
from python_files.graph import Graph
from python_files.crypto_currencies_prices import currency_symbol
from python_files.lower_right_area import InformationBoxes, actual_prices


class Main:

    def __init__(self) -> None:
        """Create the window
        """

        # window creation
        self.root = tk.Tk()
        self.root.geometry('1080x740')
        self.root.resizable(False, False)
        self.root.iconbitmap('assets/icon.ico')
        self.root.title("Evolution of the value of the main cryptocurrencies")
        self.root['bg'] = '#E6E6E6'

        # graph area creation
        self.graph_area = tk.Frame(self.root, width=self.root.winfo_width()*0.5, height=self.root.winfo_height()*0.5,
                                   bg='#E6E6E6')
        self.graph_area.place(x=-180, y=-10)

        # scrolling menus generation
        self.scrolling_menu = gen_menus(self.root)

        # graph generation
        self.graph = Graph(self.graph_area)

        # actual price generation
        self.actual_price_text = tk.StringVar()
        actual = actual_prices[self.scrolling_menu[1].get().split()[0]][self.scrolling_menu[2].get()[:3]]
        self.actual_price_text.set(f"Actual Price : {actual}{currency_symbol[self.scrolling_menu[2].get()[:3]]}")
        self.actual_price_label = tk.Label(self.root, textvariable=self.actual_price_text,
                                           font=("Bold", 14), fg='#107FE8', bg='#E6E6E6').place(x=730, y=48)

        # lower right area generation
        self.lower_right_area = InformationBoxes(self.root, self.graph.values, self.scrolling_menu[1].get().split()[0],
                                                 self.scrolling_menu[2].get()[:3])

        # update button creation
        self.update_button_image = ImageTk.PhotoImage(Image.open('assets/update.png'))
        self.update_button = tk.Button(self.root, image=self.update_button_image, cursor="hand2", command=self.update)
        self.update_button.place(x=self.root.winfo_width()*0.9, y=8)

        # exit button creation
        self.exit_button = tk.Button(self.root, text='Exit', cursor="hand2", command=self.root.destroy)
        self.exit_button.place(x=8, y=8)

        # window opening
        self.root.mainloop()

    # update function creation
    def update(self) -> None:
        """Update the graph, the area of information and the actual price
        """
        physical = self.scrolling_menu[2].get()[:3]
        self.graph.update([menu.get() for menu in self.scrolling_menu])
        self.lower_right_area.update(self.graph.values, self.scrolling_menu[1].get().split()[0], physical)
        self.actual_price_text.set("Actual Price : " +
                                   str(round(actual_prices[self.scrolling_menu[1].get().split()[0]][physical], 6)) +
                                   str(currency_symbol[physical]))

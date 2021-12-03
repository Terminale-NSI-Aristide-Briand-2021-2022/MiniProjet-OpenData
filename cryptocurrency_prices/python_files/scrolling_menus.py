import tkinter as tk


class Menu:

    def __init__(self, menu_area, options: list, default: int, column: int = None, place: tuple = None) -> None:
        """Generate a scrolling menu

        Parameters
        ----------
        menu_area : tkinter.Frame
        options : list
        default : int
        column : int [optional]
        place: tuple [optional]
        """
        # scrolling menu options creation
        self.menu_option = options
        self.menu_value = tk.StringVar(menu_area)
        self.menu_value.set(self.menu_option[default])

        # scrolling menu creation
        self.scrolling_menu = tk.OptionMenu(menu_area, self.menu_value, *self.menu_option)

        # for the scrolling menus of the graph
        if column is not None:
            self.scrolling_menu.config(width=15, font=('Helvetica', 12))
            self.scrolling_menu.grid(row=0, column=column)

        # for the scrolling menus of the conversion
        else:
            self.scrolling_menu.config(width=10, font=('Helvetica', 10))
            self.scrolling_menu.place(x=place[0], y=place[1])

    def get(self) -> str:
        """Return the selected value of the scrolling menu

        Returns
        -------
        str
        """
        return self.menu_value.get()


def gen_menus(root) -> list:
    """Generate the menus in root

    Parameters
    ----------
    root : tkinter.Tk

    Returns
    -------
    list of tkinter.StringVar
    """
    # menus area creation
    menu_area = tk.Frame(root)
    menu_area.place(relx=0.5, y=23, anchor=tk.CENTER)

    # menus generation
    all_menus = [
        Menu(menu_area, ['ascent - descent', 'gain - loss', 'full'], 1, 0),
        Menu(menu_area, ['BTC - Bitcoin', 'ETH - Ethereum', 'XRP - Ripple', 'LTC - Litecoin', 'SHIB - Shiba'], 0, 1),
        Menu(menu_area, ['USD - dollar', 'EUR - euro', 'JPY - yen', 'GBP - pound sterling'], 0, 2),
        Menu(menu_area, ['1 year', '1 month', '1 week'], 1, 3)
    ]

    # return the scrolling menus
    return [menu.menu_value for menu in all_menus]

import tkinter as tk
from statistics import mean, median
from python_files.date_verification import *
from python_files.crypto_currencies_prices import currency_symbol, get_crypto_prices, actual_prices,\
    all_cryptos, all_physical
from python_files.scrolling_menus import Menu
from python_files.find_peaks import find_peaks


class InformationBoxes:

    def __init__(self, root, values: list, crypto: str, physical_currency: str) -> None:
        """Generate the lower right area in the root

        Parameters
        ----------
        root : tkinter.Tk
        values : list
        crypto : str
        physical_currency : str
        """

        self.values = values
        self.crypto = crypto
        self.physical_currency = physical_currency
        self.symbol = currency_symbol[self.physical_currency]

        # boxes creation :
        percents = [(0.32, 0.12), (0.25, 0.47), (0.2, 0.75)]
        self.boxes = []
        for i in range(3):
            box = tk.Frame(root, width=root.winfo_width() * 0.28, height=root.winfo_height() * percents[i][0],
                           bg='#D7D7D7', borderwidth=3, relief=tk.RIDGE)
            box.pack_propagate(False)
            box.place(x=root.winfo_width() * 0.69, y=root.winfo_height() * percents[i][1])
            self.boxes.append(box)

        # boxes titles creation
        titles = ['GRAPH INFORMATION', 'INFORMATION ON A DAY', 'CONVERSIONS']
        for i in range(len(titles)):
            tk.Label(self.boxes[i], text=titles[i], background='#D7D7D7',
                     fg='#BB2020', font=('Times', 12)).pack(side=tk.TOP)

        # boxes elements creation
        # graph info box elements creation
        self.graph_start = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_start.place(x=40, y=45)
        self.graph_end = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_end.place(x=165, y=45)
        self.graph_min = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_min.place(x=40, y=75)
        self.graph_max = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_max.place(x=165, y=75)
        self.graph_average = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_average.place(x=30, y=105)
        self.graph_median = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_median.place(x=160, y=105)
        self.graph_low_peak = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_low_peak.place(x=10, y=135)
        self.graph_high_peak = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_high_peak.place(x=155, y=135)
        self.graph_variation_rate = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_variation_rate.place(x=90, y=165)
        self.graph_percent = tk.Label(self.boxes[0], text="", bg='#D7D7D7', fg='#191997')
        self.graph_percent.place(x=65, y=195)

        # update here so you don't have to redo all calculations twice
        self.update(self.values, self.crypto, self.physical_currency)

        # day info box elements creation
        self.day_day_label = tk.Label(self.boxes[1], text="day (DD/MM/YYYY) :", bg='#D7D7D7').place(x=15, y=40)
        self.day_day_entry = tk.Entry(self.boxes[1], width=10)
        self.day_day_entry.place(x=135, y=40)
        self.day_day_button = tk.Button(self.boxes[1], text="✔", cursor="hand2", command=self.day_information)
        self.day_day_button.place(x=215, y=38)

        self.day_day_error_label = tk.Label(self.boxes[1], text="", fg='Red', bg='#D7D7D7')
        self.day_day_error_label.place(x=40, y=60)

        self.day_open_label = tk.Label(self.boxes[1], text="open :  ...", bg='#D7D7D7', fg='#191997')
        self.day_open_label.place(x=40, y=100)
        self.day_close_label = tk.Label(self.boxes[1], text="close :  ...", bg='#D7D7D7', fg='#191997')
        self.day_close_label.place(x=165, y=100)
        self.day_min_label = tk.Label(self.boxes[1], text="min :  ...", bg='#D7D7D7', fg='#191997')
        self.day_min_label.place(x=40, y=120)
        self.day_max_label = tk.Label(self.boxes[1], text="max :  ...", bg='#D7D7D7', fg='#191997')
        self.day_max_label.place(x=165, y=120)
        self.day_min_since_label = tk.Label(self.boxes[1], text="min since :  ...", bg='#D7D7D7', fg='#191997')
        self.day_min_since_label.place(x=20, y=140)
        self.day_max_since_label = tk.Label(self.boxes[1], text="max since :  ...", bg='#D7D7D7', fg='#191997')
        self.day_max_since_label.place(x=160, y=140)
        self.day_percent_label = tk.Label(self.boxes[1], text="variation rate between this day and today :  ...",
                                          bg='#D7D7D7', fg='#191997')
        self.day_percent_label.place(x=10, y=160)

        # conversions box elements creation
        self.conversion_from_menu = Menu(self.boxes[2], all_cryptos + all_physical, 0, place=(20, 40))
        self.conversion_to_menu = Menu(self.boxes[2], all_cryptos + all_physical, 5, place=(20, 100))

        self.conversion_entry = tk.Entry(self.boxes[2], width=15)
        self.conversion_entry.place(x=150, y=45)

        self.conversion_label = tk.Label(self.boxes[2], text="", font=("Bold", 11), bg='#D7D7D7', fg='#191997')
        self.conversion_label.place(x=150, y=105)

        self.conversion_button = tk.Button(self.boxes[2], text=">>>", cursor="exchange", command=self.conversion)
        self.conversion_button.place(x=140, y=72)

    def day_information(self) -> None:
        """Displays all the information for the day
        """

        day_entry = self.day_day_entry.get()

        if is_date_valid(day_entry, self.crypto == 'SHIB'):

            days_values = get_crypto_prices(self.crypto, self.physical_currency,
                                            (date.today() - date(day=int(day_entry[:2]), month=int(day_entry[3:5]),
                                                                 year=int(day_entry[6:]))).days, False)

            # hide the day error label
            self.day_day_error_label['text'] = ""

            # display the day info
            self.day_open_label['text'] = f"open :  {days_values[0][0]}{self.symbol}"
            self.day_close_label['text'] = f"close :  {days_values[0][1]}{self.symbol}"
            self.day_min_label['text'] = f"min :  {days_values[0][2]}{self.symbol}"
            self.day_max_label['text'] = f"max :  {days_values[0][3]}{self.symbol}"
            min_since = min([day[2] for day in days_values])
            self.day_min_since_label['text'] = f"min since :  {min_since}{self.symbol}"
            max_since = max([day[3] for day in days_values])
            self.day_max_since_label['text'] = f"max since :  {max_since}{self.symbol}"
            # rate calculation :  100 x (final value – initial value) / initial value
            initial_value = ((days_values[0][2] + days_values[0][3]) / 2)
            percent = round(100 * (actual_prices[self.crypto][self.physical_currency]-initial_value) / initial_value, 2)
            self.day_percent_label['text'] = f"variation rate between this day and today :  {percent}%"

        else:

            # display the day error label
            self.day_day_error_label['text'] = "not valid, must be an DD/MM/YYYY date\n" \
                                               "between 2000 days ago and yesterday"

            # hide the day info
            self.day_open_label['text'] = "open :  ..."
            self.day_close_label['text'] = "close :  ..."
            self.day_min_label['text'] = "min :  ..."
            self.day_max_label['text'] = "max :  ..."
            self.day_min_since_label['text'] = "min since :  ..."
            self.day_max_since_label['text'] = "max since :  ..."
            self.day_percent_label['text'] = "variation rate between this day and today :  ..."

    def conversion(self) -> None:
        """Displays the result of the conversion
        """
        entry = self.conversion_entry.get()
        if entry.replace('.', '').replace(',', '').replace('-', '').isdigit()\
                and entry.count('.') + entry.count(',') <= 1 and entry.count('-') <= 1:
            val = str(actual_prices[self.conversion_from_menu.get()][self.conversion_to_menu.get()] * float(entry))[:12]
            if len(val) > 10:
                val = str(format(float(val), '.1E'))
            self.conversion_label['text'] = val
            self.conversion_label['fg'] = '#191997'
        else:
            self.conversion_label['text'] = "impossible"
            self.conversion_label['fg'] = 'Red'

    def update(self, values: list, crypto: str, physical_currency: str) -> None:
        """Update the lower right area

        Parameters
        ----------
        values : list
        crypto : str
        physical_currency : str
        """

        # change the values from the scrolling menus
        self.values = values
        self.crypto = crypto
        self.physical_currency = physical_currency
        self.symbol = currency_symbol[self.physical_currency]

        # update the graph info box
        self.graph_start['text'] = f"start :  {self.values[0]}{self.symbol}"
        self.graph_end['text'] = f"end :  {self.values[-1]}{self.symbol}"
        self.graph_min['text'] = f"min :  {min(self.values)}{self.symbol}"
        self.graph_max['text'] = f"max :  {max(self.values)}{self.symbol}"
        self.graph_average['text'] = f"average :  {round(mean(self.values), 5)}{self.symbol}"
        self.graph_median['text'] = f"median :  {median(self.values)}{self.symbol}"

        # calculate the low and the high peak
        low_index, high_index = find_peaks(self.values)
        low_peak = self.values[-low_index] if low_index is not None else '...'
        high_peak = self.values[-high_index] if low_index is not None else '...'

        self.graph_low_peak['text'] = f"last low peak :  {low_peak}{self.symbol}"
        self.graph_high_peak['text'] = f"last high peak :  {high_peak}{self.symbol}"

        # rate calculation :  100 x (final value – initial value) / initial value
        variation_rate = round(100 * (self.values[-1] - self.values[0]) / self.values[0], 2)
        self.graph_variation_rate['text'] = f"variation rate :  {variation_rate}%"
        nb_values_greater = len([value for value in self.values[1:] if value > self.values[0]])
        percentage = round(nb_values_greater * 100 / (len(self.values) - 1), 2)
        self.graph_percent['text'] = f"percentage of days greater than\nthe beginning :  {percentage}%"

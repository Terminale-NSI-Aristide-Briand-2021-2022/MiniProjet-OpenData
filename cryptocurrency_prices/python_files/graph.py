from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.ticker import MultipleLocator
from datetime import date, timedelta
from python_files.crypto_currencies_prices import crypto_currencies_prices as ccp, currency_symbol


class Graph:

    def __init__(self, graph_area) -> None:
        """Initializes the graph

        Parameters
        ----------
        graph_area : tkinter.Frame
        """

        # generate the figure
        self.fig = Figure(figsize=(7, 7), dpi=90)

        # generate the graph
        self.values = ccp['BTC']['USD'][-30:]
        self.plot = self.fig.add_subplot(111)
        self.plot.plot([f'{(date.today() - timedelta(days=i)).day}/{(date.today() - timedelta(days=i)).month}' for i
                        in range(30, 0, -1)], self.values, linewidth=3,
                       c='#F78067' if self.values[0] > self.values[-1] else '#78F767')

        # set the different settings of the coordinate system
        self.plot.xaxis.set_major_locator(MultipleLocator(7))
        self.plot.set_title('Evolution of the price of BTC in the last month')
        self.plot.set_xlabel('date')
        self.plot.set_ylabel('price (in $)')

        # draw the graph
        self.canvas = FigureCanvasTkAgg(self.fig, graph_area)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(padx=250, pady=60)

        # add the toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, graph_area)
        self.toolbar.config(background='#E6E6E6')
        self.toolbar.place(x=380, y=700)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()

    def update(self, settings: list) -> None:
        """Updates the graph with the parameters entered

        Parameters
        ----------
        settings : list  [display_mode: str, cryptocurrency: str, physical_currency: str, scale: str]
        """

        # do changes
        # changes depending on cryptocurrency
        crypto = settings[1].split()[0]

        # changes depending on physical currency
        physical = settings[2][:3]
        y_title = 'price (in {})'.format(currency_symbol[physical])

        # changes depending on scale
        scale_text = ' in the last ' + settings[3][2:]
        if settings[3] == '1 year':
            self.values = ccp[crypto][physical]
            abscissa_separator = len(self.values) // 8
            line_width = 2
            if not len(self.values) == 365:
                scale_text = ' from the start'
        elif settings[3] == '1 month':
            self.values = ccp[crypto][physical][-30:]
            abscissa_separator = 7
            line_width = 3
        else:
            self.values = ccp[crypto][physical][-7:]
            abscissa_separator = 1
            line_width = 4
        title = 'Evolution of the price of ' + settings[1].split()[0] + scale_text

        # application of the changes
        # wipe off the existing figure
        self.fig.clf()
        self.plot = self.fig.add_subplot(111)

        # generate the graph
        if settings[0] == 'ascent - descent':
            for i in range(len(self.values) - 1):
                self.plot.plot([f'{(date.today() - timedelta(days=len(self.values) - (i + j))).day}/'
                                f'{(date.today()- timedelta(days=len(self.values) - (i + j))).month}'
                                for j in range(2)], [self.values[i], self.values[i + 1]],
                               c='#F78067' if self.values[i] > self.values[i + 1] else '#78F767', linewidth=line_width)
        elif settings[0] == 'gain - loss':
            self.plot.plot([f'{(date.today() - timedelta(days=i)).day}/{(date.today() - timedelta(days=i)).month}' for i
                            in range(len(self.values), 0, -1)], self.values,
                           c='#F78067' if self.values[0] > self.values[-1] else '#78F767', linewidth=line_width)
        else:
            self.plot.bar([f'{(date.today() - timedelta(days=i)).day}/{(date.today() - timedelta(days=i)).month}' for i
                           in range(len(self.values), 0, -1)], self.values, color='#67B1F7')
            self.plot.set_ylim(min(self.values) * 0.99, max(self.values) * 1.01)

        # set the different settings of the coordinate system
        self.plot.xaxis.set_major_locator(MultipleLocator(abscissa_separator))
        self.plot.set_title(title)
        self.plot.set_xlabel('date')
        self.plot.set_ylabel(y_title)

        # update graph
        self.canvas.draw()

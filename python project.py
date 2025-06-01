import pandas as pd     #  pandas do utworzenia struktury DataFrame do wykresu (latwiejsze operowanie na danych)
import tkinter as tk    #  tkinter do utworzenia GUI 
import numpy as np      #  numpy do utworzenia zbioru xticks(punktow na osi X) 
import matplotlib.pyplot as plt  # matplotlib do figury wykresu (obszar na ktorym znajduje sie wykres)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # do przedstawienia wykresu poprzez tkinter
import seaborn as sns  # do utworzenia wykresu poprzez seaborn(bardziej intuicyjne niz matplotlib)
import random as rd    # do wygenerowania losowych danych przekazanych do wykresu


class gui(tk.Tk):  # stworzenie klasy gui w ktorej zawiera sie caly program
    def __init__(self, title, geometry):  # funkcja ktora odpala sie przy inicjacji klasy
        super().__init__()

        self.title(title)  # tytul okna gui
        self.geometry(geometry)  # rozmiar okna gui
        self.frame = tk.Frame(self)  # dodawanie widgetow label, entry itd do ramki ktora jest w glownym oknie tk.Tk
        self.frame.pack()  # zapakowanie ramki do tk.Tk aby byla widoczna

        mini = tk.StringVar()  # okreslenie zmiennych pod tkinter entry
        maxi = tk.StringVar()
        numb = tk.StringVar()
        bins = tk.StringVar()

        label1 = tk.Label(self.frame, text="Podaj minimalna liczbe")  # label(tekst w gui) informuje co mamy wprowadzic
        label1.grid(row=1, column=1)  # grid(siatka) czyli jakie ma byc ulozenie widgetow
        entry1 = tk.Entry(self.frame, textvariable=mini)  # entry(czyli puste pole do wypelnienia danymi)
        entry1.grid(row=1, column=2)

        label2 = tk.Label(self.frame, text="Podaj maksymalna liczbe")
        label2.grid(row=1, column=3)
        entry2 = tk.Entry(self.frame, textvariable=maxi)
        entry2.grid(row=1, column=4)

        label3 = tk.Label(self.frame, text="Podaj ilosc liczb")
        label3.grid(row=2, column=1)
        entry3 = tk.Entry(self.frame, textvariable=numb)
        entry3.grid(row=2, column=2)

        label4 = tk.Label(self.frame, text="Wybierz ilosc koszykow")
        label4.grid(row=3, column=1)
        entry4 = tk.Entry(self.frame, textvariable=bins)
        entry4.grid(row=3, column=2)

        buttonsum = tk.Button(self.frame, text="Stworz wykres",
                              command=lambda: self.gen(mini.get(), maxi.get(), numb.get(),
                                                       bins.get()))  # tk button czyli guzik wykonujacy funkcje gen(wygeneruj wykres), jest okreslony poprzez lambda gdyz w innym przypadku by nie pozwolil na wprowadzenie danych, .get() sluzy do przetransformowania informacji w rozszerzenie tkinter do zwyklej
        buttonsum.grid(row=4, column=2, columnspan=2)

    def gen(self, mini, maxi, numb, binss):  # funkcja generujaca wykres, przekazanie argumentow z entry
        fig, ax = plt.subplots()  # utworzenie figury oraz podwykresu
        canvas = FigureCanvasTkAgg(fig, master=self.frame)  # umieszczenie figury na plotnie do tkinter
        canvas.get_tk_widget().grid(row=5, column=1, columnspan=4)
        table = []  # utworzenie tabeli do losowych danych
        rd.seed(a=None)  # zresetowanie seeda aby liczby byly pseudolosowe
        for i in range(int(numb)):
            table.append(rd.randint(int(mini), int(maxi)))  # pseudolosowanie danych
        table = pd.DataFrame({"liczby": table})  # utworzenie dataframe z tablicy
        sns.histplot(data=table,  # utworzenie wykresu poprzez seaborn, przekazanie dataframe
                     x=table["liczby"],
                     # wskazanie kolumny do zaprezentowania danych, ze wzgledu ze to jest histogram to wartosci Y to count z X
                     bins=int(binss),  # ilosc koszykow na dane
                     ax=ax)  # wskazanie na ktorym wykresie przedstawic wizualizacje
        ax.set_xticks(np.arange(min(table["liczby"]),
                                max(table["liczby"]) + (max(table["liczby"]) - min(table["liczby"])) / int(binss),
                                (max(table["liczby"]) - min(table["liczby"])) / int(
                                    binss)))  # ustawienie xticks na ilosc
        plt.close()  # zamkniecie starego wykresu aby nie pokazywal sie w notebooku


gui = gui("nygusek", "600x600")
gui.mainloop()
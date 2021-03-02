import tkinter as tk
import tkinter.ttk as ttk

from database.connection import Connection
from database.models import Movie

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.session = Connection().create_session()
        self.title('Movie Database')
        self.geometry('390x210')
        
        self.frame_c = tk.LabelFrame(self, text='Create')
        self.frame_c.grid(row=0, column=0)

        tk.Label(self.frame_c, text='Name').grid(row=0, column=0)
        self.name_c = tk.StringVar()
        tk.Entry(self.frame_c, textvariable=self.name_c).grid(row=0, column=1)
        
        tk.Label(self.frame_c, text='Year').grid(row=1, column=0)
        self.year_c = tk.IntVar()
        self.year_c.set(2021)
        tk.Entry(self.frame_c, textvariable=self.year_c).grid(row=1, column=1)

        tk.Label(self.frame_c, text='Director').grid(row=2, column=0)
        self.director_c = tk.StringVar()
        tk.Entry(self.frame_c, textvariable=self.director_c).grid(row=2, column=1)

        tk.Label(self.frame_c, text='Rate').grid(row=3, column=0)
        self.rate_c = tk.IntVar()
        rate = ttk.Combobox(self.frame_c, width=18, textvariable=self.rate_c) 
        rate['values'] = (1, 2, 3, 4)
        rate.grid(row=3, column=1)

        tk.Button(self.frame_c, text="Create", command=self.create).grid(row=4, column=0)
        self.mainloop()      

    def create(self):
        name = self.name_c.get()
        year = self.year_c.get()
        director = self.director_c.get()
        rate = self.rate_c.get()
        
        movie = Movie(name, year, director, rate)
        self.session.add(movie)
        self.session.commit()
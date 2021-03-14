# import tkinter as tk
# import tkinter.ttk as ttk

# from sqlalchemy.sql.expression import update

# from database.connection import Connection
# from database.models import Movie

# class GUI(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.session = Connection().create_session()
#         self.title('Movie Database')
#         # self.geometry('390x210')
        
#         self.frame_c = tk.LabelFrame(self, text='Create')
#         self.frame_c.grid(row=0, column=0)

#         tk.Label(self.frame_c, text='Name').grid(row=0, column=0)
#         self.name_c = tk.StringVar()
#         tk.Entry(self.frame_c, textvariable=self.name_c).grid(row=0, column=1)
        
#         tk.Label(self.frame_c, text='Year').grid(row=1, column=0)
#         self.year_c = tk.IntVar()
#         self.year_c.set(2021)
#         tk.Entry(self.frame_c, textvariable=self.year_c).grid(row=1, column=1)

#         tk.Label(self.frame_c, text='Director').grid(row=2, column=0)
#         self.director_c = tk.StringVar()
#         tk.Entry(self.frame_c, textvariable=self.director_c).grid(row=2, column=1)

#         tk.Label(self.frame_c, text='Rate').grid(row=3, column=0)
#         self.rate_c = tk.IntVar()
#         rate = ttk.Combobox(self.frame_c, width=18, textvariable=self.rate_c) 
#         rate['values'] = (1, 2, 3, 4)
#         rate.grid(row=3, column=1)

#         tk.Button(self.frame_c, text="Create", command=self.create).grid(row=4, column=0)


#         self.frame_r = tk.LabelFrame(self, text='Read')
#         self.frame_r.grid(row=1, column=0)

#         tk.Label(self.frame_r, text='Movie').grid(row=0, column=0)
#         self.movie_r = tk.StringVar()
#         tk.Entry(self.frame_r, textvariable=self.movie_r).grid(row=0, column=1)

#         tk.Button(self.frame_r, text="Read", command=self.read).grid(row=1, column=0)

#         self.frame_d = tk.LabelFrame(self, text='Delete')
#         self.frame_d.grid(row=1, column=1)

#         tk.Label(self.frame_d, text='Movie').grid(row=0, column=0)
#         self.movie_d = tk.StringVar()
#         tk.Entry(self.frame_d, textvariable=self.movie_d).grid(row=0, column=1)

#         tk.Button(self.frame_d, text="Delete", command=self.delete).grid(row=1, column=0)


#         self.frame_u = tk.LabelFrame(self, text='Update')
#         self.frame_u.grid(row=0, column=1)

#         tk.Label(self.frame_u, text='ID').grid(row=0, column=0)
#         self.ID_u = tk.IntVar()
#         tk.Entry(self.frame_u, textvariable=self.ID_u).grid(row=0, column=1)
        
#         tk.Label(self.frame_u, text='Name').grid(row=1, column=0)
#         self.name_u = tk.StringVar()
#         tk.Entry(self.frame_u, textvariable=self.name_u).grid(row=1, column=1)
        
#         tk.Label(self.frame_u, text='Year').grid(row=2, column=0)
#         self.year_u = tk.IntVar()
#         self.year_u.set(2021)
#         tk.Entry(self.frame_u, textvariable=self.year_u).grid(row=2, column=1)

#         tk.Label(self.frame_u, text='Director').grid(row=3, column=0)
#         self.director_u = tk.StringVar()
#         tk.Entry(self.frame_u, textvariable=self.director_u).grid(row=3, column=1)

#         tk.Label(self.frame_u, text='Rate').grid(row=4, column=0)
#         self.rate_u = tk.IntVar()
#         rate = ttk.Combobox(self.frame_u, width=18, textvariable=self.rate_u) 
#         rate['values'] = (1, 2, 3, 4)
#         rate.grid(row=4, column=1)

#         tk.Button(self.frame_u, text="Update", command=self.up).grid(row=5, column=0)


#         self.mainloop()  


#     def up(self):
#         movie = self.session.query(Movie).filter(Movie.id == self.ID_u.get()) 
#         print(movie)
#         movie.update({
#             'name': self.name_u.get(), 
#             'year': self.year_u.get(), 
#             'director': self.director_u.get(),
#             'rate': self.rate_u.get()
#             })
#         print("Update")
#         self.session.commit()

#     def delete(self):
#         movie = self.session.query(Movie).filter(Movie.id == self.movie_d.get())    
#         movie.delete()
#         self.session.commit()


#     def read(self):
#         name = self.movie_r.get()
#         self.movie_r.set('')
#         movies = self.session.query(Movie).filter(Movie.name.contains(name)) 
#         top = tk.Toplevel()
#         treev = ttk.Treeview(top, selectmode ='browse') 
#         treev.grid(row=0, column=1) 

#         verscrlbar = ttk.Scrollbar(top,  
#                                 orient ="vertical",  
#                                 command = treev.yview) 
#         verscrlbar.grid(row=0, column=0) 
        
#         treev.configure(xscrollcommand = verscrlbar.set) 
#             # github.com/theseana/hichi

#         treev["columns"] = ("1", "2", "3", "4") 
#         treev['show'] = 'headings'
#         treev.column("1", width = 90, anchor ='c') 
#         treev.column("2", width = 90, anchor ='se') 
#         treev.column("3", width = 90, anchor ='se') 
#         treev.column("4", width = 90, anchor ='se') 
#         treev.heading("1", text ="Name") 
#         treev.heading("2", text ="Year") 
#         treev.heading("3", text ="Director") 
#         treev.heading("4", text ="Rate") 

#         for m in movies:
#             treev.insert("", 'end', text ="L1", 
#             values =(m.name, m.year, m.director, m.rate)) 
# #  aryaaaaan

#     def create(self):
#         name = self.name_c.get()
#         year = self.year_c.get()
#         director = self.director_c.get()
#         rate = self.rate_c.get()

#         self.name_c.set('')
#         self.year_c.set(2021)
#         self.director_c.set('')
#         self.rate_c.set(1)

#         movie = Movie(name, year, director, rate)
#         self.session.add(movie)
#         self.session.commit()



import tkinter as tk
import tkinter.ttk as ttk

from connection import Connection
from models import Movie


class GUI(tk.Tk):
    def _init_(self):
        super()._init_()
        self.session = Connection().create_session()
        self.title('Movie Database')
        #self.geometry('390x210')

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

        # github.com/theseana/hichi
        self.frame_r = tk.LabelFrame(self, text='Read')
        self.frame_r.grid(row=1, column=0)

        tk.Label(self.frame_r, text='Movie').grid(row=0, column=0)
        self.movie_r = tk.StringVar()
        tk.Entry(self.frame_r, textvariable=self.movie_r).grid(row=0, column=1)

        tk.Button(self.frame_r, text="Read", command=self.read).grid(row=1, column=0)


        self.frame_d = tk.LabelFrame(self, text='Delete')
        self.frame_d.grid(row=1, column=1)

        tk.Label(self.frame_d, text='Movie').grid(row=0, column=0)
        self.movie_d = tk.StringVar()
        tk.Entry(self.frame_d, textvariable=self.movie_d).grid(row=0, column=1)

        tk.Button(self.frame_d, text="Delete", command=self.delete).grid(row=1, column=0)

        self.frame_u = tk.LabelFrame(self, text='Update')
        self.frame_u.grid(row=0, column=1)

        tk.Label(self.frame_u, text='Name').grid(row=0, column=0)
        self.name_u = tk.StringVar()
        tk.Entry(self.frame_u, textvariable=self.name_u).grid(row=0, column=1)

        tk.Label(self.frame_u, text='Year').grid(row=1, column=0)
        self.year_u = tk.IntVar()
        self.year_u.set(2021)
        tk.Entry(self.frame_u, textvariable=self.year_u).grid(row=1, column=1)

        tk.Label(self.frame_u, text='Director').grid(row=2, column=0)
        self.director_u = tk.StringVar()
        tk.Entry(self.frame_u, textvariable=self.director_u).grid(row=2, column=1)

        tk.Label(self.frame_u, text='Rate').grid(row=3, column=0)
        self.rate_u = tk.IntVar()
        rate = ttk.Combobox(self.frame_u, width=18, textvariable=self.rate_u)
        rate['values'] = (1, 2, 3, 4)
        rate.grid(row=3, column=1)

        tk.Button(self.frame_u, text="Updtate", command=self.up).grid(row=4, column=0)

        self.mainloop()


    def up(self):
        movie = self.session.query(Movie).filter(Movie.id == self.ID_u.get())
        print(movie)
        movie.update({
            'name' : self.name_u.get(),
            'year' : self.year_u.get(),
            'director' : self.director_u.get(),
            'rate' : self.rate_u.get()
        })
        print("Update")
        self.session.commit()


    def delete(self):
        movie = self.session.query(Movie).filter(Movie.id ==self.movie_d.get())
        movie.delete()
        self.session.commit()


    def read(self):
        name = self.movie_r.get()
        self.movie_r.set('')
        movies = self.session.query(Movie).filter(Movie.name.contains(name))
        top = tk.Toplevel()
        treev = ttk.Treeview(top, selectmode='browse')
        treev.grid(row=0, column=1)

        verscrlbar = ttk.Scrollbar(top,
                                   orient="vertical",
                                   command=treev.yview)
        verscrlbar.grid(row=0, column=0)

        treev.configure(xscrollcommand=verscrlbar.set)

        treev["columns"] = ("1", "2", "3", "4")
        treev['show'] = 'headings'
        treev.column("1", width=90, anchor='c')
        treev.column("2", width=90, anchor='se')
        treev.column("3", width=90, anchor='se')
        treev.column("4", width=90, anchor='se')
        treev.heading("1", text="Name")
        treev.heading("2", text="Year")
        treev.heading("3", text="Director")
        treev.heading("4", text="Rate")

        for m in movies:
            treev.insert("", 'end', text="L1",
                         values=(m.name, m.year, m.director, m.rate))

    def create(self):
        name = self.name_c.get()
        year = self.year_c.get()
        director = self.director_c.get()
        rate = self.rate_c.get()


        movie = Movie(name, year, director, rate)
        self.session.add(movie)
        self.session.commit()

        self.name_c.set('')
        self.year_c.set(2021)
        self.director_c.set('')
        self.rate_c.set(1)
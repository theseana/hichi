import tkinter as tk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Label(self, text='Bazinga').grid(row=0, column=0)
        self.mainloop()      

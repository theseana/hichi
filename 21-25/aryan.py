
# # Using treeview widget 
# treev = ttk.Treeview(window, selectmode ='browse') 
# treev.pack(side ='right') 

# verscrlbar = ttk.Scrollbar(window,  
#                            orient ="vertical",  
#                            command = treev.yview) 
# verscrlbar.pack(side ='right', fill ='x') 
  
# treev.configure(xscrollcommand = verscrlbar.set) 
  
# treev["columns"] = ("1", "2", "3") 
# treev['show'] = 'headings'
# treev.column("1", width = 90, anchor ='c') 
# treev.column("2", width = 90, anchor ='se') 
# treev.column("3", width = 90, anchor ='se') 
# treev.heading("1", text ="Name") 
# treev.heading("2", text ="Sex") 
# treev.heading("3", text ="Age") 
  

# treev.insert("", 'end', text ="L1",  
#              values =("Nidhi", "F", "25")) 


# # def azhdar():
# #     print("azhdar asli")


# # class A:
# #     def __init__(self):
# #         azhdar()
# #         self.azhdar()


# # def azhdar(self):
# #     print("Azhdar")

# # A()



a = 2
b = 3

a > b 

def __gt__
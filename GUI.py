from tkinter import *
from tkinter import ttk
import Functions
root = Tk()

btn = ttk.Button(root,text = "Update Data")
btn2 = ttk.Button(root,text = "Get Data")
btn.pack()
btn2.pack()
btn.config(command=Functions.DataLog().UpdateDb)
btn2.config(command=lambda : Functions.DataLog().getData("ERROR"))
root.mainloop()
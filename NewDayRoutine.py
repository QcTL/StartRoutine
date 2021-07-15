from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
import glob
import os

win = Tk()

apps = []



def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title ="Select File",
                                        filetypes=(("executable", "*.exe"),("all files","*.*")))
    if filename != "":
        apps.append(filename)
    print(filename)
    for app in apps:
        label = Label(frame,text=app,bg="gray").pack()

def doneApp():
    with open('./Saves/' +nom.get() + '.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')
    sys.exit()

def delLastApp():
    for widget in frame.winfo_children():
        widget.destroy()
    if len(app) > 0:
        apps.pop()
    for app in apps:
        label = Label(frame,text=app,bg="gray").pack()

wrapper = ttk.Frame(win)
wrapper.grid(column=0, row=0, sticky=(N, W, E, S))


showApps = Canvas(wrapper, width=400, height= 500, bg='blue')
showApps.grid(column=1, row=1,sticky= (N,W,E))
frame = LabelFrame(showApps)
showApps.create_window((0,0), window=frame, width= 400,anchor="nw")




confApps = Canvas(wrapper, width=100, bg='red')
confApps.grid(column=2, row=1,sticky= (N,W))
nom = StringVar()
nom_entry = ttk.Entry(confApps, width=13, textvariable=nom).place(relx=.5,rely=.1,anchor= CENTER)
buttonNew = Button(confApps, text = "New", command = addApp).place(relx=.5,rely=.25,anchor= CENTER)
buttonDelete = Button(confApps, text = "Delete", command = delLastApp).place(relx=.5,rely=.35,anchor= CENTER)
buttonDone = Button(confApps, text = "Done", command = doneApp).place(relx=.5,rely=.6,anchor= CENTER)

win.geometry("510x510")
win.resizable(False,False)
win.title("Start The Day")


win.mainloop()

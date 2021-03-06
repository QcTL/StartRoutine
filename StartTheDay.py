from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
import glob
import os

filesApps = []
apps = []
indexFiles = 0

def newDayRoutine():
    os.startfile("NewDayRoutine.py")

def reloadFiles():
    global filesApps,indexFiles

    filesApps = os.listdir('./Saves')
    indexFiles = len(filesApps)

def showFileScreen():
    global apps
    if indexFiles != 0:
        if os.path.isfile('./Saves/' + filesApps[indexFiles-1]):
            with open('./Saves/'+filesApps[indexFiles-1],'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps =  [x for x in tempApps if x.strip()]
                print(tempApps)


def reloadText():

    global wrapper1
    if indexFiles != 0:
        if os.path.isfile('./Saves/' + filesApps[indexFiles-1]):
            with open('./Saves/'+filesApps[indexFiles-1],'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                apps =  [x for x in tempApps if x.strip()]

    for widget in wrapper1.winfo_children():
        widget.destroy()
    for app in apps:
        label = Label(wrapper1,text=app,wraplength = 400,pady = 2, width=45,bg="gray")
        label.pack()

def UpindexFiles():
    global indexFiles
    if indexFiles == len(filesApps):
        indexFiles = 1
    else:
        indexFiles = indexFiles+1

    reloadText()
    showFileScreen()

def DownindexFiles():
    global indexFiles
    if indexFiles == 1:
        indexFiles = len(filesApps)
    else:
        indexFiles = indexFiles-1

    reloadText()
    showFileScreen()


def runApps():
    for app in apps:
        os.startfile(app)


def reloadAll():
    reloadFiles()
    showFileScreen()
    reloadText()

win = Tk()


helv13 = tkFont.Font(family='Helvetica', size=13, weight=tkFont.BOLD)
helv18 = tkFont.Font(family='Helvetica', size=18, weight=tkFont.BOLD)


wrapper = Canvas(win,bg = "#536B78")
wrapper.grid(column=0, row=0, sticky=(N, W, E, S))
wrapper.config(highlightbackground="#536B78")
win.columnconfigure(0, weight=1,pad= 50)
win.rowconfigure(0, weight=1,pad= 20)

###
setStart = Canvas(wrapper, width=300, height= 100, bg='#637081')
setStart.grid(column=1, row=1,sticky=(N, W, E, S))
setStart.config(highlightbackground="#536B78")
buttonNew = Button(setStart, text = "Start",bg ="#ACCBE1",font=helv18, command = runApps).place(relx=.5,rely=.5,anchor= CENTER)
###


####
setConfig = Canvas(wrapper, width=190, height= 100, bg='#637081')
setConfig.grid(column=2, row=1,sticky=(N,W))
setConfig.config(highlightbackground="#536B78")
buttonNew = Button(setConfig, text = "New",font=helv13, bg='#7C98B3' , command = newDayRoutine).place(relx=.3,rely=.3,anchor= CENTER)
buttonDelete = Button(setConfig, text = "Delete", bg='#7C98B3',font=helv13).place(relx=.3,rely=.7,anchor= CENTER)
buttonReload = Button(setConfig, text = "Reload", bg='#7C98B3',font=helv13, command = reloadAll).place(relx=.7,rely=.5,anchor= CENTER)
#buttonNew.pack()
###



setView = Canvas(wrapper, width=100, height= 300, bg='#637081')
setView.grid(column=1, row=2,sticky=(N,W,E))
setView.config(highlightbackground="#536B78")

wrapper1 = LabelFrame(setView)
wrapper1.pack(fill = "both", expand = "yes")

setChange = Canvas(wrapper, width=190, height= 300, bg='#637081')
setChange.config(highlightbackground="#536B78")
setChange.grid(column=2, row=2,sticky=(N,W))
buttonUp = Button(setChange, text = ">",font=helv13, bg='#7C98B3', command = UpindexFiles).place(relx=.55,rely=.1,anchor= CENTER)
buttonDown = Button(setChange, text = "<",font=helv13, bg='#7C98B3', command = DownindexFiles).place(relx=.35,rely=.1,anchor= CENTER)
buttonRun = Button(setChange, text = "Run",font=helv13, bg='#7C98B3', command = runApps).place(relx=.45,rely=.25,anchor= CENTER)

reloadAll()


win.geometry("500x410")
win.resizable(False,False)
win.title("Start The Day")

win.configure(bg='#637081')
win.mainloop()

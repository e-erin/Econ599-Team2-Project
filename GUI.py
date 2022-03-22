# from curses.textpad import Textbox
#from curses import window
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
from turtle import color, width
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pydantic import FilePath

#global vars
xName=''
yName=''
tName=''
window1 = Tk()
window1.title('file project')
window1.geometry('400x420') 
fileDir=''

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('CSV Files', '*csv')])
    global fileDir
    fileDir=file_path.name
    if file_path is not None:
        pass

def generateGraph():
    
    print(fileDir)
    if(comb.get()=="scatter"):
        dataset = pd.read_csv(fileDir)
        X = dataset.iloc[:, 1:-1].values
        y = dataset.iloc[:, -1].values
        plt.scatter(X, y, color = 'red')
        plt.plot(X, y, color = 'blue')
        plt.title(tName)
        plt.xlabel(xName)
        plt.ylabel(yName)
        plt.legend()
        plt.show()
    else:
        dataset = pd.read_csv(fileDir)
        X = dataset.iloc[:, 1:-1].values
        y = dataset.iloc[:, -1].values
        plt.bar(y,height=50)
        plt.plot(X, y, color = 'blue')
        plt.title(tName)
        plt.xlabel(xName)
        plt.ylabel(yName)
        plt.legend()
        plt.show()


def gettingInpX():
    global xName
    xName=xBox.get()

def gettingInpY():
    global yName
    yName=yBox.get()

def gettingInpT():
    global tName
    tName=tBox.get()

def getComb():
    comb.get()

def mBox():
    if(stateVar.get()==True):
        messagebox.showinfo("great","glad you enjoyed")
    else:
        messagebox.showinfo("Sorry", "hopefully you will find some use")
def mover():
   # moveB.destroy()
    moveB.grid(row=12,column=1)
def dest():
    rButton.destroy()



def windowMake():
    window2 = Tk()
    def dest2():
        window2.destroy() 
    window2.title("test")
    window2.geometry("400x400")
    bw2=Button(window2,text="destroy button",command=dest2)
    bw2.grid(row=0,column=0)
    window2.mainloop()



#getting the csv file  
csvLabel= Label(window1, text='Upload a CSV File ')
csvLabel.grid(row=0, column=0, padx=10)
csvButton = Button(window1, text ='Choose File', command = lambda:open_file()) 
csvButton.grid(row=0, column=1)

#textbox
xLabel=Label(window1,text="x name:")
xLabel.grid(row=2,column=0)
xBox=Entry(window1,width=10)
xBox.grid(column=0,row=3)
xButton=Button(window1,text="enter",command=gettingInpX)
xButton.grid(row=3,column=1)

yLabel=Label(window1,text="y name:")
yLabel.grid(row=4,column=0)
yBox=Entry(window1,width=10)
yBox.grid(column=0,row=5)
yButton=Button(window1,text="enter",command=gettingInpY)
yButton.grid(row=5,column=1)

tLabel=Label(window1,text="Title:")
tLabel.grid(row=6,column=0)
tBox=Entry(window1,width=10)
tBox.grid(column=0,row=7)
tButton=Button(window1,text="enter",command=gettingInpT)
tButton.grid(row=7,column=1)

#combobox
comb=Combobox(window1)
comb['values']=("scatter","bar","None")
comb.current(2)
comb.grid(column=0,row=8)
combButton=Button(window1,text="enter",command=getComb)
combButton.grid(row=8,column=1)

#generating graph
graphLabel = Label(window1, text='Generate Graph')
graphLabel.grid(row=9, column=0, padx=10)
graphButton = Button(window1, text ='generate graph', command=generateGraph) 
graphButton.grid(row=9, column=1)

#checkmark
stateVar=BooleanVar()
stateVar.set(False)
chk=Checkbutton(window1,text="are you satisfied",var=stateVar)
chk.grid(row=10,column=0)
chkButton=Button(window1,text="enter",command=mBox)
chkButton.grid(row=10,column=1)

#moving stuff
moveB=Button(text="move Right",command=mover)
moveB.grid(row=12,column=0)

#destroying
rButton=Button(text="destroy me",command=dest)
rButton.grid(row=13,column=0)

wButton=Button(window1,text="new window", command=windowMake)
wButton.grid(row=14,column=0)
#actually runns the program, put last
window1.mainloop()


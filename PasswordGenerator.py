from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from ttkthemes import ThemedTk
import random
import pyperclip
window=ThemedTk(theme="equilux")
window.config(themebg="equilux")
window.geometry("500x200")
window.title("Password Generator")
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits="ABCDEFGHIJKLMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()"

def generate():
    global c,rb,pe,password
    password=""
    co= c.get()
    rbg=rb.get()

    length= int(co)
    if rbg=="Low":
        for i in range(0,length,1):
            a=random.choice(lower)
            password=password+a

    elif rbg=="Medium":
        for i in range(0,length,1):
            a=random.choice(upper)
            password=password+a

    else:
        for i in range(0,length,1):
            a=random.choice(digits)
            password=password+a

    c.delete(0,END)
    pe.insert(0,password)
def Copy():
    global password
    pyperclip.copy(password)
def Copyen():
    global password
    pyperclip.copy(pen)

plbl=ttk.Label(window,text="Password",font=('bold,40'))
plbl.place(x=10,y=20)
pe=ttk.Entry(text="")
pe.place(x=90,y=20)
gbtn=ttk.Button(window,text="Generate",command=generate)
gbtn.place(x=225,y=17)

cbtn=ttk.Button(window,text="Copy",command=Copy)
cbtn.place(x=320,y=17)


llbl=ttk.Label(window,text="Length",font=('bold,40'))
llbl.place(x=10,y=60)
c = Combobox(window)
c ["values"] = ("4","6","8","16","24")
c.place(x=70,y=60)

rb= StringVar()
rad1=ttk.Radiobutton(window,text="Low",value="Low",variable=rb)
rad1.place(x=225,y=60)

rad2=ttk.Radiobutton(window,text="Medium",value="Medium",variable=rb)
rad2.place(x=300,y=60)

rad3=ttk.Radiobutton(window,text="Strong",value="Strong",variable=rb)
rad3.place(x=400,y=60)

penlbl=ttk.Label(window,text="Password Encrypted",font=('bold,40'))
penlbl.place(x=10,y=120)

pen=ttk.Entry(text="")
pen.place(x=160,y=120)

ebtn=ttk.Button(window,text="Encrypt")
ebtn.place(x=300,y=115)

debtn=ttk.Button(window,text="Decrypt")
debtn.place(x=390,y=115)

cebtn=ttk.Button(window,text="Copy",command=Copyen)
cebtn.place(x=350,y=150)



window.mainloop()
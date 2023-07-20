from tkinter import *
from tkinter import messagebox
import base64 
import os

def encrypt():
    ...

def decrypt():
    ...


def main_screen():
    global screen
    global text1
    global code

    screen = Tk()
    screen.geometry('450x450')
    screen.resizable(True,True)

    image_icon = PhotoImage(file='keys.png')
    screen.iconphoto(False, image_icon)
    screen.title('Criptografia')

    def reset():
        code.set('')
        text1.delete(1.0, END)

    Label(text='Escreva a mensagem', fg='black', font=('calibri',13)).place(x=10,y=10)
    text1 = Text(font='Robote 20', bg='white', relief=GROOVE, wrap=WORD,bd=0)
    text1.place(x=13, y=48, width=424,height=149)
     
    Label(text='Escreva a senha', fg='black', font=('calibri', 13)).place(x=13, y=212) 

    code = StringVar()
    Entry(textvariable=code, width=22, bd=0, font=('arial', 25), show='*').place(x=13, y=248)

    Button(text= 'ENCRIPTAR', height='2', width=23, bg='#ed3833', fg='white', bd=0,\
           command=encrypt).place(x=13, y=307)
    Button(text= 'DESENCRIPTAR', height='2', width=23, bg='#00bd56', fg='white', bd=0,\
           command=decrypt).place(x=236, y=307)
    Button(text= 'RESET', height='2', width=50, bg='#1089ff', fg='white', bd=0,\
           command=reset).place(x=13, y=376)

    screen.mainloop()

main_screen()    

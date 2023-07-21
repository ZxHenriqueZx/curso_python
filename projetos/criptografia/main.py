from tkinter import *
from tkinter import messagebox
import base64 
import os

def decrypt():
    password = code.get() 
    
    if password == 'Lhfds1423@':
        screen2 = Toplevel(screen)
        screen2.title('Descriptografar')
        screen2.geometry('400x200')
        screen2.configure(bg='#00bd56')
        
        message = text1.get(1.0, END)
        decode_message = message.encode('ascii')
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode('ascii')

        Label(screen2, text = 'DESCRIPTOGRAFADO', font='arial', fg='white', bg='#00bd56').place(x=10,y=0)
        text2 = Text(screen2, font='Rpbote 10', bg='white', relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    
    elif password == '':
        messagebox.showerror('Descriptografar', 'Digite uma senha!!')
    elif password != 'Lhfds1423@':
        messagebox.showerror('Descriptografar', 'Senha Inválida!!')

def encrypt():
    password = code.get() 
    
    if password == 'Lhfds1423@':
        screen1 = Toplevel(screen)
        screen1.title('Criptografar')
        screen1.geometry('400x200')
        screen1.configure(bg='#ed3833')
        
        message = text1.get(1.0, END)
        encode_message = message.encode('ascii')
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode('ascii')

        Label(screen1, text = 'CRIPTOGRAFADO', font='arial', fg='white', bg='#ed3833').place(x=10,y=0)
        text2 = Text(screen1, font='Rpbote 10', bg='white', relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
    
    elif password == '':
        messagebox.showerror('Criptografar', 'Digite uma senha!!')
    elif password != 'Lhfds1423@':
        messagebox.showerror('Criptografar', 'Senha Inválida!!')

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

    Button(text= 'CRIPTOGRAFAR', height='2', width=23, bg='#ed3833', fg='white', bd=0,\
           command=encrypt).place(x=13, y=307)
    Button(text= 'DESCRIPTOGRAFAR', height='2', width=23, bg='#00bd56', fg='white', bd=0,\
           command=decrypt).place(x=236, y=307)
    Button(text= 'RESET', height='2', width=50, bg='#1089ff', fg='white', bd=0,\
           command=reset).place(x=13, y=376)

    screen.mainloop()

main_screen()    

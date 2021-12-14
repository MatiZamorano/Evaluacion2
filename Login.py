import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

def menuPantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("400x480")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("logo.ico")

    image=PhotoImage(file="logo2.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Elija una opción", bg="navy", fg="white", width="280", height="3", font=("Calibri", 15)).pack ()
    Label(text="").pack()

    Button(text="Alumno", height="2", width="25").pack()
    Label(text="").pack()
    Button(text="Docente", height="2", width="25").pack()
    Label(text="").pack()
    Button(text="Administrativo", height="2", width="25").pack()

    pantalla.mainloop()


def inicioSesion():

    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("500x300")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1, text= "Por favor ingrese su usuario y contraseña", bg="navy", fg="white", width="280", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global idUsuario_verify
    global contrasenaUsuario_verify

    idUsuario_verify=StringVar ()
    contrasenaUsuario_verify=StringVar ()

    global nombreUsuarioEntry
    global contrasenaUsuarioEntry

    Label(pantalla1, text="Usuario").pack()
    nombreUsuarioEntry= Entry (pantalla1, textvariable= idUsuario_verify)
    nombreUsuarioEntry.pack()
    Label (pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasenaUsuarioEntry= Entry (pantalla1, textvariable= contrasenaUsuario_verify)
    contrasenaUsuarioEntry.pack()
    Label (pantalla1).pack()

    Button (pantalla1, text="Iniciar Sesion").pack()


menuPantalla()






















































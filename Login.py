import tkinter
from tkinter import*
from tkinter import messagebox
import cx_Oracle
lib_dir= 'C:\Users\matia\OneDrive\Escritorio\Proyecto Inacap'
try:
    cx_Oracle.init_oracle_client()
    conexion=cx_Oracle.connect(user="admin", password="Proyectoinacap2021.", dsn="BDproyecto")

        
except Exception as ex:
    print(ex)


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

    Button(text="Alumno", height="2", width="25", command=alumno).pack()
    Label(text="").pack()
    Button(text="Docente", height="2", width="25", command=docente).pack()
    Label(text="").pack()
    Button(text="Administrativo", height="2", width="25").pack()

    pantalla.mainloop()

def alumno():
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("500x300")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1, text= "Elija una opción", bg="navy", fg="white", width="280", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    Button(pantalla1, text="Inicar Sesión", height="2", width="25", command= inicioSesion).pack()
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registrarse", height="2", width="25", command= registrar).pack()
    Label(pantalla1, text="").pack()

def docente():
    global pantalla2
    pantalla2= Toplevel(pantalla)
    pantalla2.geometry("500x300")
    pantalla2.title("Bienvenido")
    pantalla2.iconbitmap("logo.ico")

    Label(pantalla2, text= "Bienvenido", bg="navy", fg="white", width="280", height="3", font=("Calibri", 15)).pack()
    Label(pantalla2, text="").pack()

    Button(pantalla2, text="Inicar Sesión", height="2", width="25", command= inicioSesion).pack()
    Label(pantalla2, text="").pack()


def inicioSesion():

    global pantalla4
    pantalla4= Toplevel(pantalla1)
    pantalla4.geometry("500x300")
    pantalla4.title("Inicio de sesion")
    pantalla4.iconbitmap("logo.ico")

    Label(pantalla4, text= "Por favor ingrese su usuario y contraseña", bg="navy", fg="white", width="280", height="3", font=("Calibri", 15)).pack()
    Label(pantalla4, text="").pack()

    global nombreUsuario_verify
    global contrasenaUsuario_verify

    nombreUsuario_verify=StringVar()
    contrasenaUsuario_verify=StringVar()

    global nombreUsuarioEntry
    global contrasenaUsuarioEntry

    Label(pantalla4, text="Usuario").pack()
    nombreUsuarioEntry= Entry (pantalla4, textvariable= nombreUsuario_verify)
    nombreUsuarioEntry.pack()
    Label (pantalla4).pack()

    Label(pantalla4, text="Contraseña").pack()
    contrasenaUsuarioEntry= Entry (pantalla4, show="*",  textvariable= contrasenaUsuario_verify)
    contrasenaUsuarioEntry.pack()
    Label (pantalla4).pack()

    Button (pantalla4, text="Iniciar Sesion", command=validacioDatos).pack()

def registrar():
    global pantalla5
    pantalla5= Toplevel(pantalla1)
    pantalla5.geometry("500x300")
    pantalla5.title("Registro")
    pantalla5.iconbitmap("logo.ico")

    global nombre_UsuarioEntry
    global contrasena_UsuarioEntry

    nombre_UsuarioEntry= StringVar()
    contrasena_UsuarioEntry= StringVar()

    Label(pantalla5, text="Por favor ingrese usario y contraseña", bg="navy", fg="white", width="280", height="3", font=("Calibri", 15)).pack ()
    Label (pantalla5).pack()

    Label(pantalla5, text="Usuario").pack()
    nombre_UsuarioEntry= Entry (pantalla5)
    nombre_UsuarioEntry.pack()
    Label (pantalla5).pack()

    Label(pantalla5, text="Contraseña").pack()
    contrasena_UsuarioEntry= Entry (pantalla5, show="*")
    contrasena_UsuarioEntry.pack()
    Label (pantalla5).pack()

    Button(pantalla5, text= "Registar", command=insertaDatos).pack()


def insertaDatos():


    fcursor=bd.cursor()

    sql="INSERT INTO Login1 (usuario, contrasena) VALUES ('(0)', '(1)')".format(nombre_UsuarioEntry.get(), contrasena_UsuarioEntry.get() )

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo (message="Registro Exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo (message="No Registrado", title="Aviso")

    bd.close()

def validacioDatos():
    bd= pymysql.connect(
    host="localhost",
    user= "root",
    passwd="",
    db="bd2"
    )

    fcursor=bd.cursor()
    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreUsuario_verify.get()+"' and contrasena '"+contrasenaUsuario_verify.get()+"'")
    if fcursor.fetchall():
        messagebox.showinfo("Inicio sesion correcta", message= "Usuarrio y contraseña validos")

    else:
         messagebox.showinfo("Inicio sesion incorrecta", message= "Usuarrio y contraseña  no validos")


    bd.close()



menuPantalla()






















































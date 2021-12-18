import Clases

import cx_Oracle
lib_dir = "D:\Trabajos Inacap\instantclient_21_3"
try:
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    conexion= cx_Oracle.connect(user="admin", password="Proyectoinacap2021.", dsn="BDproyecto_high")
    
        
except Exception as ex:
    print(ex)


print("bienvenido al menu")
def menu():
    print(
        '**************************************\n'
        'Ingrese una opcion para iniciar\n'
        '1)Asignar modulo a docente\n'
        '2)Ver modulos docente\n'
        '3)Quitar modulos a docente\n'
        '4)Agregar modulo a sistema\n'
        '5)Editar modulo a sistema\n'
        '6)Eliminar modulo a sistema\n'
        '7)Ver todos los modulos del sistema\n'
        '8)Inscribir alumno en modulo\n'
        '9)Quitar alumno del modulo\n'
        '10)Cambiar alumno de seccion\n'
        '11)Agregar nota a alumno\n'
        '12)Editar nota a alumno\n'
        '13)Quitar nota a alumno\n'
        '14)Matricular alumno\n'
        '15)Anular matricula\n'
        '16)Editar matricula\n'
        '17)Listar alumnos matriculados\n'
        '18)Salir\n'
        '**************************************'
    )
menu()
op=0
while op != 18:
    op=int(input('ingresa una opcion: '))
    if op ==1:
        print('ingresaste opcion 1')
        Clases.JefeCarrera.asignarModulo(modulo, docente, modulos)
        print('ingrese el nombre del modulo')
        modulo=input('')
        modulos=[]
        
    elif op ==2:
        print('ingresaste opcion 2')
        Clases.JefeCarrera.verModulo(modulo)

    elif op ==3:
        print('ingresaste opcion 3')
        Clases.JefeCarrera.quitarModulo(modulo)

    elif op ==4:
        print('ingresaste opcion 4')
        Clases.JefeCarrera.agregarModulo(modulo, seccion)

    elif op ==5:
        print('ingresaste opcion 5')
        Clases.JefeCarrera.editarModulo(modulo)

    elif op ==6:
        print('ingresaste opcion 6')
        Clases.JefeCarrera.eliminarModulo(modulo)

    elif op ==7:
        print('ingresaste opcion 7')
        Clases.JefeCarrera.verModuloSistema(modulo)
        for i in range(len(modulos)):
            print(modulos[i])

    elif op ==8:
        print('ingresaste opcion 8')
        Clases.JefeCarrera.inscribirAlumno(alumno, modulo)

    elif op ==9:
        print('ingresaste opcion 9')
        Clases.JefeCarrera.quitarAlumnoModulo(alumno, modulo)

    elif op ==10:
        print('ingresaste opcion 10')
        Clases.JefeCarrera.cambiarAlumnoSeccion(alumno, seccion)

    elif op ==11:
        print('ingresaste opcion 11')
        Clases.Modulo.agregarNota(nota, modulo, alumno)


    elif op ==12:
        print('ingresaste opcion 12')
        Clases.Modulo.editarNota(nota, modulo, alumno)

    elif op ==13:
        print('ingresaste opcion 13')
        Clases.Modulo.quitarNota(nota, modulo, seccion)

    elif op ==14:
        print('ingresaste opcion 14')
        Clases.Matricula.matricularAlumno(matricula, alumno)


    elif op ==15:
        print('ingresaste opcion 15')
        Clases.Matricula.anularMatricula(matricula, alumno)

    elif op ==16:
        print('ingresaste opcion 16')
        Clases.Matricula.editarMatricula(matricula, alumno)

    elif op ==17:
        print('ingresaste opcion 17')
        Clases.Matricula.listarAlumnosMatriculados(matricula, alumno)

    elif op ==18:
        print('ingresaste opcion 18\n'
        '****************************\n'
        'Gracias por usar mi programa'
        )
        exit()
        
    else:
        print('error vuelva a intentarlo')
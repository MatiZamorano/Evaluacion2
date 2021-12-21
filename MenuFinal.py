import BD
import time
import hashlib
#import requests

#ir = requests.get(' https://api.sbif.cl/api-sbifv3/recursos_api/uf?apikey=418085a3c5c55e2101b8ba8d1c82f7393c1c8a7e&formato=json')

#datos = ir.json()

#x= float(datos['UFs'][0]['Valor'].replace('.','').replace(',','.'))
#print('Valor de la UF',x)
ahora = time.strftime("%c")
clave=int(input("ingrese clave numerica: "))


print('\n***********************')
print('\n❇ Sesión Iniciada ❇')
print('\n***********************')

MenuPrincipal=int(input('\n Menú Principal: \n 1- Alumno \n 2- Docente \n 3- Jefe Carrera \n 4- Cerrar Sesión \n -------- \n Ingrese Número de Usuario: '))
while MenuPrincipal != 0:

    if MenuPrincipal == 1:
        print('\nAcabas de ingresar como Alumno')
        NombreUsuario=str(input('Ingresar  Nombre: '))

        Alumno=int(input('\nSeleccione una Acción: \n 1- Matricularse \n 2- Anular Matricula \n 3- Ver Matriculados\n 4- Retroceder\n -------- \n Ingrese Opción: '))
        
        while Alumno != 0:
            
            if Alumno == 1:
                print('\nVentana de Matricula')
                NombreMatricula=str(input('\nNombre y Apellido: '))
                CorreoMatricula=str(input('Correo Electrónico: '))
                IngresoMatricula=int(input('Ingreso Anual: '))
                CarreraMatricula=str(input('Carrera: '))
                HoraMatricula=str(input('Horario Carrera: '))

                print('\n---Matricula Realizada---')
                print(f'\n|Nombre del Alumno: {NombreMatricula}')
                print(f'\n|Correo Electrónico: {CorreoMatricula}')
                print(f'\n|Carrera Escogida: {CarreraMatricula}')
                print(f'\n|Horario: {HoraMatricula}')
                print("\n|Fecha y hora: " + time.strftime("%c"))
                print('\n|ESTAS MATRICULADO|\n')
                Matricula=[]
                Matricula=[NombreMatricula, CorreoMatricula, CarreraMatricula, HoraMatricula]
                print(Matricula)
                sistema=[Matricula]

            if Alumno == 2:
                print('\nVentana para Anular Matricula')
                Matricula=[NombreMatricula, CorreoMatricula, CarreraMatricula, HoraMatricula]
                Matricula.pop(0)[NombreMatricula, CorreoMatricula, CarreraMatricula, HoraMatricula]
                print("matricula eliminada")
                print(Matricula)

            if Alumno == 3:
                print('\nVentana para ver a los Matriculados')
                print(Matricula)
            
            if Alumno == 4:
                print('\nAtrás')
                break
            Alumno=int(input('\nSeleccione una Acción: \n 1- Matricularse \n 2- Anular Matricula \n 3- Ver Matriculados\n 4- Retroceder\n ---------- \n Ingrese Opción: '))
    
    if MenuPrincipal == 2:
        print('\n Has ingresado como Docente \n')
        NombreDocente=str(input('Nombre: '))
        SeccionDocente=str(input('Sección: '))
        HorasTrabajo=str(input('Horas de Trabajo: '))
        CargoDocente=str(input('Cargo: '))

        Docente=int(input('\nSeleccione una Acción: \n 1- Ver Sección \n 2- Ver Horas de Trabajo \n 3- Cargo \n 4- Ingresar Notas \n 5- Editar Notas \n 6- Retroceder \n Ingrese Opción: '))
        while Docente != 0:

            if Docente == 1:
                print('\nVentana Sección')
                print(f'\nSección: {SeccionDocente}')

            if Docente == 2:
                print('\nVentana Horas')
                print(f'\nHoras de Trabajo: {HorasTrabajo}')

            if Docente == 3:
                print('\nVentana Cargo')
                print(f'\nCargo Asignado: {CargoDocente}')

            if Docente == 4: 
                print('\nVentana Notas')
                Nota1=int(input('\nIngrese las Notas N°1: '))
                Nota2=int(input('\nIngrese las Notas N°2: '))
                Nota3=int(input('\nIngrese las Notas N°3: '))
                Prom=(Nota1+Nota2+Nota3)/3
                print('')
                print(int(Prom))
                print('')
                AlumnoNota=[Nota1, Nota2, Nota3]
                print(AlumnoNota)

            if Docente == 5: 
                print('\nVentana Edición Notas')
                print('\nEdite las Notas ')
                AlumnoNota.remove(int(input("ingrese la nuevas nota")))
                print(AlumnoNota)
                
                print(f'\n===Se han Editado las Notas del Alumno {NombreAlumno}===')
                NombreAlumno=str(input('\nNombre del Alumno: '))
                AlumnoNota.remove(int(input("ingresa las notas de nuevo:")))

            if Docente == 6:
                print('\nAtrás')
                break
            Docente=int(input('\nSeleccione una Acción: \n 1- Ver Sección \n 2- Ver Horas de Trabajo \n 3- Cargo \n 4- Ingresar Notas \n 5- Editar Notas \n 6- Retroceder \n Ingrese Opción: '))

    if MenuPrincipal == 3:
        print('\n Has entrado como JefeCarrera C.\n ')
        NombreDirectorC=str(input('Nombre: '))
        CargoDirectorC=str(input('Carrera Encargado/a: '))
        

        JefeCarrera=int(input('\nSeleccione una Acción: \n 1- Asignar Modulo \n 2- Asignar N° Sección \n 3- Ver Modulo Docente \n 4- Ver Todos los Modulos \n 5- Editar Matricula \n 6- Atrás \n Ingrese Opción:'))
        while  JefeCarrera != 0:

            if JefeCarrera == 1:
                print('\nVentana Asignar Modulo')
                AsigM=str(input(f'\nPersona a quien Asignar: '))
                NombreM=str(input(f'\nNombre del Modulo: '))

            if JefeCarrera == 2:
                print('\nVentana Asignar Sección')
                AsigSD=str(input('\nDocente: '))
                AsigSA=str(input('\nSección Asignada: '))
                print("\n|Fecha y hora: " + time.strftime("%c"))

            if JefeCarrera == 3:
                print('\nVentana Ver Modulos')
                print(f'\nDocente: {AsigM}')
                print(f'\nModulo: {NombreM}')

            if JefeCarrera == 4:
                print('\nVentana Todos los Modulos')
                print(f'\nModulos:  ') 

            if JefeCarrera == 5:
                print('\nVentana Editar Matricula')
                NombreMatricula1=str(input('Nombre Matriculado: '))

            if JefeCarrera == 6:
                print('\nAtrás')
                break
            JefeCarrera=int(input('\nSeleccione una Acción: \n 1- Asignar Modulo \n 2- Asignar N° Sección \n 3- Ver Modulo Docente \n 4- Ver Todos los Modulos \n 5- Editar Matricula \n 6- Atrás \n Ingrese Opción:'))

    if MenuPrincipal == 4:
        print('\n Se ha cerrado la sesión')
        break
    
    else:
        print('\nError. Si Sale el Menú entonces no hay Error.\n ')
    
    MenuPrincipal = int(input('\n Menú Principal: \n 1- Alumno \n 2- Docente \n 3- Director Carrera \n 4- Cerrar Sesión \n ---------- \n Ingrese Número de Usuario: '))
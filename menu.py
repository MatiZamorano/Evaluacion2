import Clases


print("bienvenido al menu")
def menu():
    print(
        '**************************************'
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
        '10)Cambiar alumno de secci贸n\n'
        '11)Agregar nota a alumno\n'
        '12)Editar nota a alumno\n'
        '13)Quitar nota a alumno\n'
        '14)Matricular alumno\n'
        '15)Anular matricula\n'
        '16)Editar matricula\n'
        '17)Sistar alumnos matriculados\n'
        '18)Salir\n'
        '**************************************'
    )
menu()
op=0
while op != 18:
    op=int(input('ingresa una opcion: '))
    if op ==1:
        print('ingresaste opcion 1')


    elif op ==2:
        print('ingresaste opcion 2')

    elif op ==3:
        print('ingresaste opcion 3')

    elif op ==4:
        print('ingresaste opcion 4')

    elif op ==5:
        print('ingresaste opcion 5')

    elif op ==6:
        print('ingresaste opcion 6')

    elif op ==7:
        print('ingresaste opcion 7')

    elif op ==8:
        print('ingresaste opcion 8')

    elif op ==9:
        print('ingresaste opcion 9')

    elif op ==10:
        print('ingresaste opcion 10')

    elif op ==11:
        print('ingresaste opcion 11')

    elif op ==12:
        print('ingresaste opcion 12')

    elif op ==13:
        print('ingresaste opcion 13')

    elif op ==14:
        print('ingresaste opcion 14')

    elif op ==15:
        print('ingresaste opcion 15')

    elif op ==16:
        print('ingresaste opcion 16')

    elif op ==17:
        print('ingresaste opcion 17')

    elif op ==18:
        print('ingresaste opcion 18')
        
    else:
        print('error vuelva a intentarlo')
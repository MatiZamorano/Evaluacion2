
 
def agregarTexto(texto):
    """ funcion para añadir un texto """
    while True:
        nombre = input(texto)
        if nombre=="":
            print("No puede estar vacio")
        else:
            return nombre
 
def ingresarNota(text):
    """ funcion para añadir una nota """
    while True:
        try:
            nota = float(input("{}(0-100): ".format(text)))
            if 10<=nota<=70:
                return nota
            else:
                print("la nota tiene que estar entre 10 y 70")
        except:
            print("la nota tiene que ser un valor numerico")
 
def agregarModulo():
    """Funcion para añadir una nueva asignatura"""
    asignaturas.append(agregarTexto("Introduce el nombre de la asignatura: "))
    # agregamos la nota a cada estudiante
    [estudiantes[key].append(-1) for key in estudiantes.keys()]
 
def agregarEstudiante():
    """Funcion para añadir estudiantes"""
    estudiantes[agregarTexto("Introduce el nombre del estudiante: ")]=[-1]*len(asignaturas)
 
def seleccionarEstudiante():
    """
    Funcion para seleccionar un estudiante
    Devuelve el nombre del estudiante seleccionado o -1
    """
    count=0
    for el in estudiantes:
        count+=1
        print ("{} - {}".format(count, el))
    try:
        estudiante=int(input("selecciona el número del estudiante a añadir las notas: "))
        if 0<estudiante<=len(estudiantes):
            return list(estudiantes.keys())[estudiante-1]
    except:
        print("Error seleccionar estudiantes")
    return -1
 
def agregarNotas():
    """Funcion para agregar todas las notas a uno de los estudiantes"""
    if len(estudiantes)==0 or len(asignaturas)==0:
        return
    estudiante=seleccionarEstudiante()
    if estudiante==-1:
        return
    for i in range(len(asignaturas)):
        notaActual="sin nota" if estudiantes[estudiante][i]==-1 else estudiantes[estudiante][i]
        estudiantes[estudiante][i]=ingresarNota("Introduce la nota para '{}' ({}): ".format(asignaturas[i], notaActual))
 
def listarAsignaturas():
    """listado de las asignaturas"""
    print("--- Listado de las asignaturas ---")
    print("\n".join([i for i in asignaturas]))
 
def listarEstudiantes():
    """Listado de los estudiantes con sus asignaturas"""
    print("--- Listado de los estudiantes con sus notas ---")
    for el in estudiantes:
        print(el)
        for i in range(len(asignaturas)):
            print("\t{} - {}".format(asignaturas[i], "Sin nota" if estudiantes[el][i]==-1 else estudiantes[el][i]))
 
def notaMediaAsignaturas():
    print("--- Nota media de las asignaturas ---")
    if len(estudiantes)==0 or len(asignaturas)==0:
        return
    for i in range(len(asignaturas)):
        valores=list(filter(lambda x: x!=-1, list(map(lambda x: x[i], estudiantes.values()))))
        print("{} - {}".format(asignaturas[i], sum(valores)/len(valores)))
 
def notaMediaEstudiantes():
    print("--- Nota media de los estudiantes ---")
    for estudiante in estudiantes:
        valores=list(filter(lambda x: x!=-1, estudiantes[estudiante]))
        if len(valores):
            print("{} - {}".format(estudiante, sum(valores)/len(valores)))
 
def borrarModulo():
    print("--- Borrar una asignatura ---")
    if len(asignaturas)==0:
        return
    print("Indica el numero de la asignatura a borrar...")
    for i in range(len(asignaturas)):
        print("\r{} - {}".format(i+1, asignaturas[i]))
    try:
        asignaturaEliminar=int(input("Asignatura a eliminar: "))
        if 0<asignaturaEliminar<=len(asignaturas):
            asignaturaEliminar-=1
            # eliminamos la asignatura
            del asignaturas[asignaturaEliminar]
            # eliminamos la nota en los estudiantes
            for key in estudiantes.keys():
                del estudiantes[key][asignaturaEliminar]
    except:
        pass
 
def borrarEstudiante():
    print("--- Borrar un estudiante ---")
    if len(estudiantes)==0 or len(asignaturas)==0:
        return
    print("Indica el numero del estudiante a borrar...")
    estudiante=seleccionarEstudiante()
    if estudiante==-1:
        return
    del estudiantes[estudiante]
 
 
def Menu():
    print ("\n".join([
        "\n---------------------------------------------------------------",
        "Selecciona una opción...",
        "1 - Añadir Modulo",
        "2 - Añadir estudiante",
        "3 - Añadir/modificar notas a los estudiantes",
        "4 - Listado de los Modulos",
        "5 - Listado de los estudiantes",
        "6 - Mostrar el promedio de las notas por Modulo",
        "7 - Mostrar el promedio de las notas por estudiante",
        "8 - Borrar una asignatura",
        "9 - Borrar un estudiante",
        "\n0 - Salir"
    ]))
 
# definimos el diccionario que contendra los estudiantes con sus notas
asignaturas=[]
# definimos el diccionario que contendra los estudiantes con sus notas
estudiantes={}
 
while True:
    Menu ()
 
    opcion = input("Ingrese el número de la opción escogida: ")
 
    functionsList={
        "1":"agregarModulo()",
        "2":"agregarEstudiante()",
        "3":"agregarNota()",
        "4":"listarAsignaturas()",
        "5":"listarEstudiantes()",
        "6":"PromedioModulo()",
        "7":"PromedioEstudiantes()",
        "8":"borrarAsignatura()",
        "9":"borrarEstudiante()"
    }
    if opcion in functionsList.keys():
        eval(functionsList[opcion])
    elif opcion == "0":
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")
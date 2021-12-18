import datetime

class Usuario:
    def __init__(self, nombre, apellido, rut, direccion, telefono, correo, usuario, contraseña, tipoUsuario, idUsuario):
        pass
        self.nombre= ''
        self.apellido= ''
        self.rut= ''
        self.direccion=''
        self.telefono=0
        self.correo=''
        self.usuario=''
        self.constraseña=''
        self.tipoUsuario=''
        self.idUsuario=''

    def validarAcceso(self):
        pass
    def editarContraseña(self):
        pass
    def modificarDatos(self):
        pass


class Alumno (Usuario):
    def __init__(self, idAlumno, registroAlumnos):

        self.idAlumno=''
        self.registroAlumnos=[]

    def iniciarSesion(self, usuario, contrasena):
        pass
    def verNotas(self, notas, modulo):
        pass

class JefeCarrera (Usuario):
    def __init__(self, idJefecarrera, listaModulos):

        self.idJefeCarrera=''
        self.litaModulos=[]

    def asignarModulo(modulo, docente):
        pass

    def verModulo (modulo, docente):
        pass

    def quitarModulo(modulo, docente):
        pass

    def agregarModulo(modulo, seccion):
        pass

    def editarModulo(modulo):
        pass

    def eliminarModulo(modulo, seccion):
        pass

    def verModuloSistema (modulo, seccion):
        pass

    def inscribirAlumno(alumno, modulo):
        pass

    def quitarAlumnoModulo (alumno, modulo):
        pass

    def cambiarAlumnoSeccion(alumno, seccion):
        pass

class Docente (Usuario):
    idDocente=''
    listaModulos=[]

class Seccion:
    idSeccion=''
    nombreSeccion=''
    modalidad=''

class Modulo:
    idModulo=''
    nombreModulo=''
    listaAlumnos=[]
    notas={}
    registroModulos=[]

    def agregarNota(self, nota, modulo, alumno):
        pass

    def editarNota(self, nota, modulo, alumno):
        pass

    def quitarNota(self, nota, modulo, alumno):
        pass


class Matricula:
    idMatricula=''
    folio=0
    fechaInscripcion= datetime
    semestre= 0
    valorMatricula=0
    arancel=0
    carrera=''
    sede=''
    listaMatricula=[]

    def matricularAlumno(self, matricula, alumno, seccion):
        pass

    def anularMatricula(self, matricula, alumno):
        pass

    def editarMatricula(self, matricula, alumno, seccion):
        pass

    def listarAlumnosMatriculados(self, alumnos, matricula):
        pass



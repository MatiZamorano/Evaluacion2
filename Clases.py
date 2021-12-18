import datetime

class Usuario:
    nombre= ''
    apellido= ''
    rut= ''
    direccion=''
    telefono=0
    correo=''
    usuario=''
    constraseña=''
    tipoUsuario=''
    idUsuario=''

    def validarAcceso(self):
        pass
    def editarContraseña(self):
        pass
    def modificarDatos(self):
        pass


class Alumno (Usuario):
    idAlumno=''
    registroAlumnos=[]

    def iniciarSesion(self, usuario, contrasena):
        pass
    def verNotas(self, notas, modulo):
        pass

class JefeCarrera (Usuario):
    idJefeCarrera=''
    lisaModulos=[]

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



from abc import abstractmethod
import re
'''Ejercicios extras'''

'''Crea un programa en el cual, mientras haya errores, vuelva a empezar. Usa las cláusulas else y finally. ¿Cómo es el comportamiento de finally?¿Interesa usarlo en este caso?'''

lista = [1,2,3]

def excepcion():
    while True:
        valor = input("\n Introduce un número: ")
        try:
            numero = int(valor)
            print(lista[numero])
        except ValueError:
            print("\nEl valor que me has dado no es númerico!")
        except IndexError:
            print("\nLa lista no tiene tantos elementos! Pon un número mas corto!")
        else:
            print("\nTodo salio bien!!!")
            break
        finally:
            print("\nFINALLY!!!!")

#excepcion()

'''Modifica la práctica de bandas musicales de la siguiente manera capturando los errores:

Si se intenta asignar una edad negativa.
Si se intenta asignar una edad que no es un número
Si se intenta instanciar un objeto cuyos atributos de nombres y apellidos sean un nº o su extensión sea de menos de tres letras. Crea tu propia clase derivada de Exception para esto.
Captura de un AttributeError si se intenta acceder a un atributo inexistente.'''

class no_letras(Exception):
    __cause__ = "No es letras"

class no_negativo(Exception):
    __cause__ = "No se acepta edad negativa"

class Persona:

    nacionalidad = None

    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None):

        #
        while True:
            try:
                if re.match(r"^[A-Za-z]+$",apellido1):
                    raise no_letras
            except no_letras:
                input("El apellido solo puede contener letras: ")
            else:
                break

        while True:
            try:
                if re.match(r"^[A-Za-z]+$",apellido2):
                    raise no_letras
            except no_letras:
                input("El apellido solo puede contener letras: ")
            else:
                break
        #

        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._edad =edad

    @abstractmethod    
    def saludo():
        pass

    def despedida(self):
        print("Adiós")

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre


    def del_nombre(self):
        self._nombre = None

    type = property(get_nombre, set_nombre, del_nombre, 'Nombre de la persona.')

    def get_apellido1(self):
        return self._apellido1

    def set_apellido1(self, apellido1):
        self._apellido1 = apellido1


    def del_apellido1(self):
        self._apellido1 = None

    type = property(get_apellido1, set_apellido1, del_apellido1, 'apellido1 de la persona.')

    def get_apellido2(self):
        return self._apellido2

    def set_apellido2(self, apellido2):
        self._apellido2 = apellido2


    def del_apellido2(self):
        self._apellido2 = None

    type = property(get_apellido2, set_apellido2, del_apellido2, 'apellido2 de la persona.')

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        #
        while True:
            try:
                if edad < 0:
                    raise no_negativo
            except no_negativo:
                edad = int(input("Introduce una edad no negativa: "))
            except TypeError:
                edad = int(input(" Introduce un valor númerico positivo válido: "))
            else:
                break
        #
        self._edad = edad


    def del_edad(self):
        self._edad = None

    type = property(get_edad, set_edad, del_edad, 'edad de la persona.')

try:
    print(Persona.sexo)
except AttributeError:
    print("No existe dicho atributo")

'''Crea las siguientes clases:
Alumno: atributos → nombre
Asignatura: atributos → nombre, nota
Los datos de cada objeto deben ser introducidos usando input y controlados con try
Crea 3 alumnos y 2 asignaturas (Geología y Filosofía)
Usa zip para unificar alumnos y notas. Llama al zip/list resultante trimestre_1
Muéstralo todo por pantalla incluyendo la media de las dos asignaturas teniendo en cuenta que Geología vale un 40% y Filosofía un 60%'''

class Alumno():

    def __init__(self, nombre):
        self.nombre = nombre

def crear_alumno():
    nombre = input("Introduce un nombre para el alumno: ")
    while True:
        try:
            if len(nombre) < 4:
                raise LongNombre
        except LongNombre:
            nombre = input("Introduce un nombre para la alumno: ")
        else:
            break
    alumno = Alumno(nombre)
    return alumno

class LongNombre(Exception):
    __cause__ = "Longitud insuficiente"

class NotaInvalida(Exception):
    __cause__ = "Nota no comprendida entre 0 y 10"

class Asignatura():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

def crear_asignatura():
    nombre = input("Introduce un nombre para la asignatura: ")
    while True:
        try:
            if len(nombre) < 4:
                raise LongNombre
        except LongNombre:
            nombre = input("Introduce un nombre para la asignatura: ")
        else:
            break
    nota = input("Introduce una nota para la asignatura: ")
    while True:
        try:
            if nota < 0 or nota > 10:
                raise NotaInvalida
        except NotaInvalida:
            nombre = input("Introduce una nota entre 0 y 10: ")
        else:
            break
    asignatura = Asignatura(nombre, nota)
    return asignatura

alumnos = [Alumno("Pepito"), Alumno("Juanito"), Alumno("Fulanito")]
geologia = [Asignatura("Geología", 8), Asignatura("Geología", 5), Asignatura("Geología", 6)]
filosofia = [Asignatura("Filosofía", 8), Asignatura("Filosofía", 7), Asignatura("Filosofía", 9)]

primer_trimestre = list(zip(alumnos, geologia, filosofia))

for elemento in primer_trimestre:
    print(f"Alumno: {elemento[0].nombre}, Asignatura: {elemento[1].nombre}, Nota: {elemento[1].nota}, Asignatura: {elemento[2].nombre}, Nota: {elemento[2].nota} Media: {(elemento[1].nota+elemento[2].nota)/2}")

'''Con los mismo estudiantes del ejercicio anterior:
Crea un conjunto de datos y guárdalo en el zip/list trimestre_2. 
Compara las notas de cada estudiante asignatura por asignatura incluyendo la media final. Nota por nota debes indicar si mejora, empeora o se queda igual. Esto debe hacerse usando zip.'''

geologia = [Asignatura("Geología", 8), Asignatura("Geología", 6), Asignatura("Geología", 8)]
filosofia = [Asignatura("Filosofía", 7), Asignatura("Filosofía", 8), Asignatura("Filosofía", 1)]

segundo_trimestre = list(zip(alumnos, geologia, filosofia))
trimestres = list(zip(primer_trimestre, segundo_trimestre))

print()

for elemento in trimestres:
    print(f"{elemento[0][0].nombre} sacó en {elemento[0][1].nombre}: un {elemento[0][1].nota} y {elemento[1][1].nota} en cada trimestre.")
    if elemento[0][1].nota > elemento[1][1].nota:
        print("Su nota en Geología ha empeorado.")
    elif elemento[0][1].nota < elemento[1][1].nota:
        print("Su nota en Geología ha mejorado.")
    else:
        print("Su nota en Geología se ha mantenido.")
    print(f"{elemento[0][0].nombre} sacó en {elemento[0][2].nombre}: un {elemento[0][2].nota} y {elemento[1][2].nota} en cada trimestre.")
    if elemento[0][2].nota > elemento[1][2].nota:
        print("Su nota en Filosofía ha empeorado.")
    elif elemento[0][2].nota < elemento[1][2].nota:
        print("Su nota en Filosofía ha mejorado.")
    else:
        print("Su nota en Filosofía se ha mantenido.")
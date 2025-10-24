from abc import abstractmethod

'''class Persona:

    nacionalidad = None

    def __init__(self, nombre=None, apellido=None):
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def hablar(self):
        pass'''

class Persona:

    nacionalidad = None

    def __init__(self, *args):
        if len(args) > 0:
            self.nombre = args[0]
        else:
            self.nombre = None
        if len(args) > 1:
            self.apellido = args[1]
        else:
            self.apellido = None

    @abstractmethod
    def hablar(self):
        pass

class Madre(Persona):
    
    def hablar(self):
        print("Soy la madre")

class Padre(Persona):
    
    def hablar(self):
        print("Luke yo soy tu Padre...")

class Hijo(Padre, Madre):
    pass

p = Persona("Luis", "Tur")
print(p)
print(p.nacionalidad)
print(p.nombre)

h = Hijo("Luke", "Skywalker")

h.hablar()
print(Hijo.__mro__)
p.hablar()

'''
nom = Madre(nombre="María")
apellido = Padre(apellido="Jiménez")
null = Hijo()
'''

nom = Madre("María")
apellido = Padre(None, "Jiménez")
null = Hijo()

print(nom.nombre, nom.apellido)
print(apellido.nombre, apellido.apellido)
print(null.nombre, null.apellido)

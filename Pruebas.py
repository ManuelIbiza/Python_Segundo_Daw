# Manuel Pérez Torres
# 20/10/2025

# Creación de clases
from abc import abstractmethod
import random

class Animal():
    '''Vamos a convertir piel en atributo de clase de las clases que heredan de Animal para que todos los animales de una misma especie tengan el mismo tipo de piel.
    
    Para esto vamos a ignorar este atributo en animal ya que me estaba dando muchos problemas.'''


    def __init__(self, peso:int, especie:str):
        self.vivo = True
        self.__peso = peso
        self.especie = especie


    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def reproducirse(self):
        pass


        #NECESITO CREAR ESTOS SETTERS GETTERS Y DELETERS
    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def del_peso(self):
        self.peso = 0

    peso = property(get_peso, set_peso, del_peso, 'Peso del animal')

class Mamifero(Animal):

    def __init__(self, peso:int, especie:str):
        _piel = "Pelo"

        super().__init__(peso, especie)
        

    @classmethod
    def reproducirse(cls):
        print("\nTengo crías!\n")

class Reptil(Animal):

    def __init__(self, peso:int, especie:str):
        _piel = "Escamas"

        super().__init__(peso, especie)  


    @classmethod
    def reproducirse(cls):
        print("\nPongo huevos!\n")

class Depredador():

    def __init__(self):
        pass

    @classmethod
    def hablar(cls):
        print("\nTE ATACO!\n")

class Presa():

    def __init__(self):
        pass

    @classmethod
    def hablar(cls):
        print("\nNO ME COMAS!\n")

class Leon(Mamifero, Depredador):

    def __init__(self, peso:int, especie:str):
        super().__init__(peso, especie)
        Depredador.__init__(self)

    @classmethod
    def hablar(cls):
        print("\nGRRRRRRRRR!!!!\n")

class Bufalo(Mamifero, Presa):

    def __init__(self, peso:int, especie:str):
        super().__init__(peso, especie)
        Presa.__init__(self)

    @classmethod
    def hablar(cls):
        print("\nAY QUE DOLOOOR!!!!\n")

class Cocodrilo(Reptil, Depredador):

    def __init__(self, peso:int, especie:str):
        super().__init__(peso, especie)
        Depredador.__init__(self)

    @classmethod
    def hablar(cls):
        print("\nBOMBARDILO CROCODILO!!!\n")

cocodrilo = Cocodrilo(300, "cocodrilo")

print(isinstance(cocodrilo, (Depredador)))
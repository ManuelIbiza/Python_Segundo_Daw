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

# FUNCIONES AUXILIARES
def generar_leones(cantidad:int):
    '''Bucle que genera un número dado de leones'''
    contador = 0
    lista = []
    while contador < cantidad:
        leon = Leon(random.randint(100, 250), "Leon")
        lista.append(leon)
        contador += 1
    return lista

def generar_bufalos(cantidad:int):
    '''Bucle que genera un número dado de bufalos'''
    contador = 0
    lista = []
    while contador < cantidad:
        bufalo = Bufalo(random.randint(100, 400), "Bufalo")
        lista.append(bufalo)
        contador += 1
    return lista

def generar_cocodrilo(cantidad:int):
    '''Bucle que genera un número dado de cocodrilos'''
    contador = 0
    lista = []
    while contador < cantidad:
        cocodrilo = Cocodrilo(random.randint(100, 500), "Cocodrilo")
        lista.append(cocodrilo)
        contador += 1
    return lista

class Manada():

    def __init__(self, especie:str,grupo:list[Animal]):
        self.especie = especie
        self.grupo = grupo

    @classmethod
    def reproduccion(cls, especie:str):
        '''Método de clase ya que se llamara desde la propia clase y generará una instancia.'''
        cantidad = random.randint(4,15)
        match especie:
            case "Leon":
                Leon.reproducirse()
                lista = generar_leones(cantidad)
            case "Bufalo":
                Bufalo.reproducirse()
                lista = generar_bufalos(cantidad)
            case "Cocodrilo":
                Cocodrilo.reproducirse()
                lista = generar_cocodrilo(cantidad)
        print(f"\nLa manada de animales de tipo {especie} consta de {cantidad} miembros.\n")
        manada = Manada(especie, lista)
        return manada


    def ordena_manada(self):
        self.grupo.sort(key=lambda miembro:miembro.peso)


class Sabana():

    def __init__(self, manadas:list[Manada]):
        '''Añado una lista de muertos que incluira todos los animales que mueran en cacerias para evitar combates con animales muertos en futuras cacerias.'''
        self.manadas = manadas
        self.muertos = []

    def caceria(self, depredador:Manada, presa:Manada, despiadada=False):

        if despiadada: # Si es despiadada se va a liar parda.
            depredador.ordena_manada()
            presa.ordena_manada()
            presa.grupo.reverse()

        # Variables para calcular el número de duelos
        cantidad_dep = len(depredador.grupo)
        cantidad_pre = len(presa.grupo)
        duelos = min(cantidad_dep, cantidad_pre)

        # Variables para gestionar muertes
        contador_duelos = 0 # Cuenta los duelos llevados a cabo
        muertos_presa = 0 # Cuenta las presas muertas para un calculo
        muertos_depred = 0 # Cuenta los depredadores muertos para un calculo

        while contador_duelos < duelos:
            print(f"\nSe enfrentan {depredador.grupo[(contador_duelos - muertos_depred)].especie} de {depredador.grupo[(contador_duelos - muertos_depred)].get_peso()} kilos como depredador y {presa.grupo[(contador_duelos - muertos_presa)].especie} de {presa.grupo[(contador_duelos - muertos_presa)].get_peso()} kilos como presa.\n")
            depredador.grupo[contador_duelos - muertos_depred].hablar()
            presa.grupo[contador_duelos - muertos_presa].hablar()

            if depredador.grupo[contador_duelos - muertos_depred].get_peso() > presa.grupo[contador_duelos - muertos_presa].get_peso():
                presa.grupo[contador_duelos - muertos_presa].vivo = False
                print(f"\nMuere el {presa.grupo[contador_duelos - muertos_presa].especie}\n")
                self.muertos.append(presa.grupo.pop(contador_duelos - muertos_presa))
                muertos_presa += 1
            elif depredador.grupo[contador_duelos - muertos_depred].get_peso() < presa.grupo[contador_duelos - muertos_presa].get_peso():
                depredador.grupo[contador_duelos - muertos_depred].vivo = False
                print(f"\nMuere el {depredador.grupo[contador_duelos - muertos_depred].especie}\n")
                self.muertos.append(depredador.grupo.pop(contador_duelos - muertos_depred))
                muertos_depred += 1
            else:
                suerte = random.randint(1,2)
                match suerte:
                    case 1:
                        presa.grupo[contador_duelos - muertos_presa].vivo = False
                        print(f"\nMuere el {presa.grupo[contador_duelos - muertos_presa].especie}\n")
                        self.muertos.append(presa.grupo.pop(contador_duelos - muertos_presa))
                        muertos_presa += 1
                    case 2:
                        depredador.grupo[contador_duelos - muertos_depred].vivo = False
                        print(f"\nMuere el {depredador.grupo[contador_duelos - muertos_depred].especie}\n")
                        self.muertos.append(depredador.grupo.pop(contador_duelos - muertos_depred))
                        muertos_depred += 1
                    case _:
                        print("\nTe has lucido Juanjo...\n")
            contador_duelos += 1
        self.mostrar_animales()

    def mostrar_animales(self):
        for manada in self.manadas:
            print(f"\n{manada.especie}\n")
            for animal in manada.grupo:
                if animal.vivo:
                    vivo = "Vivo"
                else:
                    vivo = "Muerto"
                print (f"Especie: {animal.especie}, Peso: {animal.get_peso()}Kg, {vivo}.")
                animal.hablar()
        for animal in self.muertos:
            print (f"Especie: {animal.especie}, Peso: {animal.get_peso()}Kg, Muerto.")

leones = Manada.reproduccion("Leon")
bufalos = Manada.reproduccion("Bufalo")

sabana = Sabana([leones,bufalos])

sabana.caceria(sabana.manadas[0], sabana.manadas[1])
print("\nLa siguiente cacería será despiadada.")
sabana.caceria(sabana.manadas[0], sabana.manadas[1], despiadada=True)
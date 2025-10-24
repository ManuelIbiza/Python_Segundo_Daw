# EJEMPLO DE "SOBRECARGA" DE MÉTODOS CONSTRUCTORES
# Recordad que la sobrecarga NO existe en Python.
# A continuación se explican maneras de simular este propiedad que si tienen algunos lenguajes como Java.

class Animal:
    # Constructor estándar
    """
    def __init__(self, nombre, color, patas, grupo, sonidos):
        self.nombre = nombre
        self.color = color
        self.patas = patas
        self.grupo = grupo
        self.sonidos = sonidos
    """

    # OPCIÓN 2: Usando *args. Nos obliga a pasar los parámetros ordenados
    def __init__(self, *args):
        # Iniciamos los atributos porque si falta alguno no se crea

        long = len(args)
        if long >= 1:
            self.nombre = args[0]
        if long >= 2:
            self.color = args[1]
        if long >= 3:
            self.patas = args[2]
        if long >= 4:
            self.grupo = args[3]
        if long >= 5:
            self.sonidos = args[4]


    # Recorre todos los atributos y los imprime
    def info_atributos(self):
        for atributo, valor in vars(self).items():
            print(f"El atributo {atributo} contiene {valor}")

# OPCIÓN 2
animalico = Animal("perro", "marron", 4, "mamiferos", "arf")
animalico.info_atributos()

print("\n")
animalico = Animal("perro")
animalico.info_atributos()

print("\n")
animalico = Animal("perro","marron")
animalico.info_atributos()
print(animalico.patas)

'''
1. Define con tus propias palabras:

· Herencia
    Capacidad de una clase de herecar atributos y métodos de una "clase padre" o superclase.

· Polimorfismo
    Capacidad de un método de actuar de manera diferente en función de que clase de objeto lo llama.

· Abstracción
    Capacidad de que se entienda que hace una función sin entender cómo funciona por dentro.

· Encapsulamiento
    Capacidad de los atributos de ser públicos, privados, o protegidos.

· Cohesión
    Simplificación de funciones y métodos para que cada uno de ellos haga una única cosa.

· Acoplamiento
    Simplificación de las conexiones entre métodos y funciones necesaria para evitar errores al modificar estos.

· PascalCase
    Normas de escritura utilizadas en Python para las clases, cada inicial de cada palabra es mayúscula y no hay separación alguna entre palabras.

· snake_case
    Normas de escritura utilizadas en Python para todo excepto clases. todas las letras son minúsculas y las palabras se separan con la barra baja "_".

· Constructor
    Método que crea instancias de clase.

2. Crea la siguiente estructura de clases:
· Persona
· Profesional — Hereda de Persona
· Manager, TecnicoSonido — Heredan de Profesional
· Artista
· Musico — Hereda de Artista y Profesional
· Banda
· Festival

Las características de las clases serán las siguientes:
· Persona
o nombre
o apellido1
o apellido2
o edad
o nacionalidad — Atributo de clase
o Métodos:
§ saludo() — Abstracto
§ despedida() — Se despide diciendo “Adiós”
'''
from abc import abstractmethod


class Persona:

    nacionalidad = None

    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None):
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
        self._edad = edad


    def del_edad(self):
        self._edad = None

    type = property(get_edad, set_edad, del_edad, 'edad de la persona.')

'''
· Artista (saluda y despide de manera molona)
o talento_principal
o talentos[]
o Métodos:
§ saludo()
§ despedida()
'''

class Artista:

    def __init__(self, talento_principal=None, talentos=None):

        self.talento_principal = talento_principal
        self.talentos = talentos

    def saludo(self):
        print("Lo primero de todo! ¿Cómo están los máquinas?")

    def despedida(self):
        print("Nos vemos en el infierno!")

'''
· Profesional (saluda y se despide de manera educada)
o profesion
o estudios
o alma_mater — Donde estudió
o ganancias  Se refiere a lo que gana anualmente. Puede ser 0
o trabajando — Atributo de clase
o Métodos:
§ ganarse_la_vida() — Abstracto. Introduce en ganancias lo que
obtiene el profesional por su trabajo.
'''

class Profesional(Persona):
    trabajando = None

    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None, profesion=None, estudios=None, alma_mater=None, ganancias=0):
        super().__init__(nombre, apellido1, apellido2, edad)
        self.profesion = profesion
        self.estudios = estudios
        self.alma_mater = alma_mater
        self.__ganancias = ganancias

    def saludo(self):
        print("Buenos días caballero.")

    def despedida(self):
        print("Adiós que tenga usted un buen día.")

    @abstractmethod
    def ganarse_la_vida():
        pass

    def get_ganancias(self):
        return self.__ganancias

    def set_ganancias(self, ganancias):
        self.__ganancias = ganancias


    def del_ganancias(self):
        self._ganancias = None

    type = property(get_ganancias, set_ganancias, del_ganancias, 'Ganancias del profesional.')


'''
· Manager (saluda y se despide de manera formal si es honesto, si no, de manera
altiva)
o honestidad
o comision — Si el mánager es honesto cobrará un 5% de comisión. En caso
contrario un 20%
o Métodos:
§ quiero_mi_comision() — devuelve el porcentaje exigido
'''

#Me estoy fumando el atributo comision porque es calculado en función del boleano "Honestidad".
class Manager (Profesional):

    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None,
                 profesion=None, estudios=None, alma_mater=None, ganancias=0,
                 Honestidad=True):
        super().__init__(nombre=nombre, apellido1=apellido1, apellido2=apellido2, edad=edad,
                         profesion=profesion, estudios=estudios, alma_mater=alma_mater, ganancias=ganancias)
        self.honestidad = Honestidad

    def saludo(self):
        if self.honestidad:
            print("Buenos días caballero.")
        else:
            print("Y tú que quieres?")

    def despedida(self):
        if self.honestidad:
            print("Adiós que tenga usted un buen día.")
        else:
            print("Pirate ya anda.")

    def quiero_mi_comision(self):
        if self.honestidad:
            return 0.05
        else:
            return 0.2
        

'''
· TecnicoSonido (saluda y se despide de manera pasota)
o especialidad — Puede ser técnico de estudio o de directos
o La ganancia del técnico de sonido es de 2000€ mensuales.
'''

class TecnicoSonido(Profesional):
    
    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None,
                 profesion=None, estudios=None, alma_mater=None, ganancias=2000,
                 especialidad=None):
        super().__init__(nombre=nombre, apellido1=apellido1, apellido2=apellido2, edad=edad,
                         profesion=profesion, estudios=estudios, alma_mater=alma_mater, ganancias=ganancias)
        self.especialidad = especialidad

'''
· Musico (saluda y se despide como un Artista)
o talento_principal “Musica”
o instrumento_principal — a elegir entre voz, bajo, guitarra y batería
o instrumentos[] — el principal debe ir en primera posición
'''

class Musico(Artista, Profesional):
    
    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None,
                 talento_principal="Música", talentos=None, instrumentos=None,
                 profesion=None, estudios=None, alma_mater=None, ganancias=0, activo=True):
        
        Artista.__init__(self, talento_principal=talento_principal, talentos=talentos)
        Profesional.__init__(self, nombre=nombre, apellido1=apellido1, apellido2=apellido2, edad=edad,
                             profesion=profesion, estudios=estudios, alma_mater=alma_mater, ganancias=ganancias)
        self.instrumento_principal = instrumentos[0]
        self.instruments = instrumentos

'''
● Banda (la banda se compone de un técnico, un manager y varios músicos sin ser
obligatorio que esté compuesta por voz, bajo, guitarra, batería)
o nombre
o idioma
o estilos_musicales[]
o integrantes — ¿Qué colección usarías para este atributo?
o discos — ¿Y para éste?
o num_fans — cantidad de fans que siguen a la banda
o ganancias_totales Se refiere a las ganancias totales en un año. De aquí
sale lo que gana el manager y músicos
o distribucion_ganancias usa una colección para asignar un porcentaje a
cada músico y al manager (recuerda que éste lo tiene predefinido). No se
cuenta al técnico.
'''

class Banda():

    def __init__(self, nombre="", idioma=None, estilos_musicales=[], integrantes=set(), discos=0, num_fans=0, ganancias_totales= 0, distribucion_ganancias={}):
        self.nombre = nombre
        self.idioma = idioma
        self.estilos_musicales = estilos_musicales
        self.integrantes = integrantes
        self.discos = discos
        self.num_fans = num_fans
        self.ganancias_totales = ganancias_totales
        self.distribucion_ganancias = distribucion_ganancias

    def ganancias_por_miembro(self):
        dinero_restante = self.ganancias_totales
        for integrante in self.integrantes:
            if isinstance(integrante, Manager):
                integrante.ganancias = integrante.quiero_mi_comision()* dinero_restante
                dinero_restante -= integrante.ganancias
        for integrante in self.integrantes:
            if isinstance(integrante, Musico):
                integrante.ganancias = self.distribucion_ganancias.get(integrante.name)* dinero_restante

'''
· Festival
o nombre
o precio
o cartel[]
'''

class Festival:

    def __init__(self, nombre=None, precio=0, cartel=[]):
        self.nombre = nombre
        self.precio = precio
        self.cartel = cartel
        

'''
· Recuerda que, a parte de los métodos indicados, debes crear los constructores
correspondientes. Si crees que necesitas más de un constructor crea adicionales.
· Si crees que necesitas un atributo o un método adicional lo puedes añadir.
· Usa los parámetros que creas necesarios en los métodos propuestos.
· Recuerda comentar el código.

3. Crea una banda con sus correspondientes integrantes. Haz que todos se saluden y
se despidan. ¿Qué concepto o conceptos de POO están interviniendo aquí?

Cantante, Guitarra, Batería, Bajo
'''

#músicos
victor = Musico(talentos= ["Cantante", "Futbolín"], instrumentos="Voz", estudios="Bachillerato", alma_mater="IES Santa María")
haibo = Musico(talentos= ["Guitarra", "League of Legends"], instrumentos="Guitarra", estudios="Bachillerato", alma_mater="IES Santa María")
sergio = Musico(talentos= ["Batería", "Pádel"], instrumentos="Batería", estudios="Bachillerato", alma_mater="IES Sa Blancadona")
hugo = Musico(talentos= ["Bajo", "Contar dinero"], instrumentos="Bajo", estudios="CFGM SMIX", alma_mater="IES Sa Colomina")

#no músicos
juanjo = Manager(profesion= "Manager", estudios="Ingenieria Informática", alma_mater="UAB", ganancias=0, Honestidad=False)
manuel = TecnicoSonido(profesion="Técnico", estudios="CFGM SMIX", alma_mater= "Ilerna")

dawn2 = Banda(nombre = "2º Dawn", idioma="Español", estilos_musicales="Regueton", integrantes= {victor, haibo, sergio, hugo,juanjo,manuel}, ganancias_totales= 100000, num_fans=10, distribucion_ganancias= {victor:0.3, haibo:0.25, sergio:0.23, hugo:0.22})

for persona in dawn2.integrantes:
    persona.saludo()

for persona in dawn2.integrantes:
    persona.despedida()

'''
4. Resulta que hay una mala racha y la banda (incluyendo técnico y manager) no está
trabajando. Modifica el atributo necesario para indicar que sus integrantes están
inactivos.

class Musico(Artista,Profesional):
    
    def __init__(self, talento_principal="Música", talentos=None, instrumentos=[], profesion=None, estudios=None, alma_mater= None, ganancias = 0, activo = True):
        Artista.__init__(self, talento_principal, talentos)
        Profesional.__init__(self, profesion, estudios, alma_mater, ganancias)
        self.instrumentos = instrumentos
        self.activo = activo
'''
        
'''
5. Todos vuelven a trabajar. Informa el atributo ganancias_totales y muestra por
pantalla que gana cada integrante además de su nombre, apellido, edad y el
instrumento que toca si lo tiene. El técnico tiene un sueldo fijo de 2000€.

class Banda():

    def __init__(self, nombre="", idioma=None, estilos_musicales=[], integrantes=set(), discos=0, num_fans=0, ganancias_totales= 0, distribucion_ganancias={}):
        self.nombre = nombre
        self.idioma = idioma
        self.estilos_musicales = estilos_musicales
        self.integrantes = integrantes
        self.discos = discos
        self.num_fans = num_fans
        self.ganancias_totales = ganancias_totales
        self.distribucion_ganancias = distribucion_ganancias

    def ganancias_por_miembro(self):
        dinero_restante = self.ganancias_totales
        for integrante in self.integrantes:
            if isinstance(integrante, Manager):
                integrante.ganancias = integrante.quiero_mi_comision()* dinero_restante
                dinero_restante -= integrante.ganancias
        for integrante in self.integrantes:
            if isinstance(integrante, Musico):
                integrante.ganancias = self.distribucion_ganancias.get(integrante.name)* dinero_restante
'''
                

'''
6. Crea 5 bandas más (pon los mínimos integrantes posibles y puedes repetir al
técnico y al mánager) y un festival con todas ellas. Ordena el cartel según el nº de
fans de maneras ascendente y muéstralo por pantalla.
'''

# Manager y técnico
manager_global = Manager(nombre="Brian", apellido1="May", profesion="Manager", estudios="ADE", alma_mater="LSE", ganancias=0, Honestidad=True)
tecnico_global = TecnicoSonido(nombre="Mike", apellido1="Sound", profesion="Técnico de sonido", estudios="CFGS Sonido", alma_mater="IES Audio", ganancias=2000, especialidad="Directos")

# The Rolling Stones 
rs_cantante = Musico(nombre="Mick", apellido1="Jagger", talentos=["Cantante"], instrumentos="Voz")
rs_guitarra = Musico(nombre="Keith", apellido1="Richards", talentos=["Guitarra"], instrumentos="Guitarra")
rs_bateria  = Musico(nombre="Charlie", apellido1="Watts", talentos=["Batería"], instrumentos="Batería")
rs_bajo     = Musico(nombre="Bill", apellido1="Wyman", talentos=["Bajo"], instrumentos="Bajo")

rolling_stones = Banda(
    nombre="The Rolling Stones",
    idioma="Inglés",
    estilos_musicales=["Rock"],
    integrantes={rs_cantante, rs_guitarra, rs_bateria, rs_bajo, manager_global, tecnico_global},
    discos=30,
    num_fans=95_000_000,
    ganancias_totales=5_000_000
)

# The Beatles 
bt_cantante = Musico(nombre="John", apellido1="Lennon", talentos=["Cantante"], instrumentos="Voz")
bt_guitarra = Musico(nombre="George", apellido1="Harrison", talentos=["Guitarra"], instrumentos="Guitarra")
bt_bateria  = Musico(nombre="Ringo", apellido1="Starr", talentos=["Batería"], instrumentos="Batería")
bt_bajo     = Musico(nombre="Paul", apellido1="McCartney", talentos=["Bajo"], instrumentos="Bajo")

beatles = Banda(
    nombre="The Beatles",
    idioma="Inglés",
    estilos_musicales=["Rock", "Pop"],
    integrantes={bt_cantante, bt_guitarra, bt_bateria, bt_bajo, manager_global, tecnico_global},
    discos=13,
    num_fans=120_000_000,
    ganancias_totales=6_000_000
)

# Nirvana
nv_cantante = Musico(nombre="Kurt", apellido1="Cobain", talentos=["Cantante"], instrumentos="Voz")
nv_guitarra = Musico(nombre="Pat", apellido1="Smear", talentos=["Guitarra"], instrumentos="Guitarra")
nv_bateria  = Musico(nombre="Dave", apellido1="Grohl", talentos=["Batería"], instrumentos="Batería")
nv_bajo     = Musico(nombre="Krist", apellido1="Novoselic", talentos=["Bajo"], instrumentos="Bajo")

nirvana = Banda(
    nombre="Nirvana",
    idioma="Inglés",
    estilos_musicales=["Grunge", "Rock alternativo"],
    integrantes={nv_cantante, nv_guitarra, nv_bateria, nv_bajo, manager_global, tecnico_global},
    discos=3,
    num_fans=45_000_000,
    ganancias_totales=2_500_000
)

# Iron Maiden
im_cantante = Musico(nombre="Bruce", apellido1="Dickinson", talentos=["Cantante"], instrumentos="Voz")
im_guitarra = Musico(nombre="Dave", apellido1="Murray", talentos=["Guitarra"], instrumentos="Guitarra")
im_bateria  = Musico(nombre="Nicko", apellido1="McBrain", talentos=["Batería"], instrumentos="Batería")
im_bajo     = Musico(nombre="Steve", apellido1="Harris", talentos=["Bajo"], instrumentos="Bajo")

iron_maiden = Banda(
    nombre="Iron Maiden",
    idioma="Inglés",
    estilos_musicales=["Heavy Metal"],
    integrantes={im_cantante, im_guitarra, im_bateria, im_bajo, manager_global, tecnico_global},
    discos=17,
    num_fans=60_000_000,
    ganancias_totales=4_200_000
)

# Projecte Mut
pm_cantante = Musico(nombre="David", apellido1="Serra", talentos=["Cantante"], instrumentos="Voz")
pm_guitarra = Musico(nombre="Joan", apellido1="Barbé", talentos=["Guitarra"], instrumentos="Guitarra")
pm_bateria  = Musico(nombre="Pep", apellido1="Tuduri", talentos=["Batería"], instrumentos="Batería")
pm_bajo     = Musico(nombre="Jaume", apellido1="Escandell", talentos=["Bajo"], instrumentos="Bajo")

projecte_mut = Banda(
    nombre="Projecte Mut",
    idioma="Catalán/Illenc",
    estilos_musicales=["Folk-Rock"],
    integrantes={pm_cantante, pm_guitarra, pm_bateria, pm_bajo, manager_global, tecnico_global},
    discos=8,
    num_fans=250_000,
    ganancias_totales=300_000
)

# Festival con todas 
festival = Festival(
    nombre="MegaFest",
    precio=120,
    cartel=[rolling_stones, beatles, nirvana, iron_maiden, projecte_mut]
)

festival.cartel.sort(key=lambda b: b.num_fans)

print(f"Cartel de {festival.nombre} (orden ascendente por nº de fans):")
for idx, banda in enumerate(festival.cartel, start=1):
    print(f"{idx}. {banda.nombre} — fans: {banda.num_fans:,}")

'''
7. Crea “constructores” alternativos al método __init__. Aplica todas las alternativas
explicadas en clase pero solamente deja activas las que utilizan el decorador


POR VALORES DEFAULTS
class Banda():

    def __init__(self, nombre="", idioma=None, estilos_musicales=[], integrantes=set(), discos=0, num_fans=0, ganancias_totales= 0, distribucion_ganancias={}):
        self.nombre = nombre
        self.idioma = idioma
        self.estilos_musicales = estilos_musicales
        self.integrantes = integrantes
        self.discos = discos
        self.num_fans = num_fans
        self.ganancias_totales = ganancias_totales
        self.distribucion_ganancias = distribucion_ganancias

USANDO ARGS

class Banda():

    def __init__(self, *args):
        long = len(args)
        if long >= 1
            self.nombre = args[0]
        elif long >= 2
            self.idioma = args[1]
        elif long >= 3
            self.estilos_musicales = args[2]
        elif long >= 4    
            self.integrantes = args[3]
        elif long >= 5    
            self.discos = args[4]
        elif long >= 6    
            self.num_fans = args[5]
        elif long >= 7    
            self.ganancias_totales = args[6]
        elif long >= 8    
            self.distribucion_ganancias = args[7]        

USANDO KWARGS

class Banda():

    def __init__(self, **kwargs):
            self.nombre = kwargs.get('nombre', "")
            self.idioma = kwargs.get('idioma', None)
            self.estilos_musicales = kwargs.get('estilos_musicales', [])
            self.integrantes = kwargs.get('integrantes', set()) 
            self.discos = kwargs.get('discos', [])
            self.num_fans = kwargs.get('num_fans', 0)  
            self.ganancias_totales = kwargs.get('ganancias_totales', 0)
            self.distribucion_ganancias = kwargs.get('distribucion_ganancias', [])    
            

USANDO CLASSMETHOD            

class Banda():

    def __init__(self, nombre, idioma, estilos_musicales, integrantes, discos, num_fans, ganancias_totales, distribucion_ganancias):
        self.nombre = nombre
        self.idioma = idioma
        self.estilos_musicales = estilos_musicales
        self.integrantes = integrantes
        self.discos = discos
        self.num_fans = num_fans
        self.ganancias_totales = ganancias_totales
        self.distribucion_ganancias = distribucion_ganancias

    @classmethod
    def constructor2(cls, nombre)
        return cls(nombre, idioma=None, estilos_musicales=[], integrantes=set(), discos=0, num_fans=0, ganancias_totales= 0, distribucion_ganancias={})
    
'''



'''
8. Redefine la clase Persona con decoradores para que cada atributo tenga su getter,
setter y deleter correspondiente. Deben ser atributos protegidos.

class Persona:

    nacionalidad = None

    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None):
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._edad =edad

    @abstractmethod    
    def saludo():
        pass

    def despedida():
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
        self._edad = edad


    def del_edad(self):
        self._edad = None

    type = property(get_edad, set_edad, del_edad, 'edad de la persona.')

'''




'''
9. Haz que el atributo ganancias de la clase Profesional sea privado y crea también el
getter, setter y deleter correspondiente.
class Profesional(Persona):
    trabajando = None

    def __init__(self, nombre=None, apellido1=None, apellido2=None, edad=None, profesion=None, estudios=None, alma_mater=None, ganancias=0):
        super().__init__(nombre=None, apellido1=None, apellido2=None, edad=None)
        self.profesion = profesion
        self.estudios = estudios
        self.alma_mater = alma_mater
        self.__ganancias = ganancias

    def saludo(self):
        print("Buenos días caballero.")

    def despedida():
        print("Adiós que tenga usted un buen día.")

    @abstractmethod
    def ganarse_la_vida():
        pass

    def get_ganancias(self):
        return self.__ganancias

    def set_ganancias(self, ganancias):
        self.__ganancias = ganancias


    def del_ganancias(self):
        self._ganancias = None

    type = property(get_ganancias, set_ganancias, del_ganancias, 'Ganancias del profesional.')
'''


'''
10. En la clase Banda vamos a añadir nuevos métodos:

'''

'''
● burbuja()  ordena de menor a mayor los integrantes de la banda según sus
ganancias. El algoritmo debe ser implementado por vosotros mismos.
'''

def burbuja(banda):
    lista_integrantes = list(banda.integrantes)

    longitud = len(lista_integrantes)
    indice_principal = 0
    while indice_principal  < longitud :
        indice_secundario = 0
        while indice_secundario < (longitud - indice_principal - 1):
            if lista_integrantes[indice_secundario].ganancias < lista_integrantes[indice_secundario + 1].ganancias:
                lista_integrantes[indice_secundario], lista_integrantes[indice_secundario + 1] = lista_integrantes[indice_secundario + 1], lista_integrantes[indice_secundario]
            indice_secundario +=1
        indice_principal += 1
    return lista_integrantes


print("!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!")
'''
● ordenar_banda()  usa directamente sort() para ordenar sus ganancias de
menor a mayor.
'''
def ordenar_banda(banda):
        lista = list(banda.integrantes)
        lista.sort(key=lambda integrante: integrante.get_ganancias())
        for elemento in lista:
            print(elemento.get_nombre())

ordenar_banda(dawn2)

'''
● ordenar_banda_reverse()  lo mismo pero de mayor a menor.
'''



def reverse(banda):
        lista = list(banda.integrantes)
        lista.sort(key=lambda integrante: integrante.get_ganancias(), reverse= True)
        for elemento in lista:
            print(elemento.get_nombre())

'''
● ordenar_banda_multi()  debe ordenar primero por ganancia y si hay dos
integrantes que ganan lo mismo que ordene por nombre, por apellido1 y por
apellido 2.
'''

def ordenar_banda_multi(banda):
    lista_integrantes = list(banda.integrantes)
    lista_integrantes.sort(
        key=lambda i: (-i.ganancias, i.nombre, i.apellido1, i.apellido2)
    )

    return lista_integrantes

'''
● muestra_banda()  muestra los siguientes campos de los integrantes y debe
incluir al manager:

i. Nombre de la banda
ii. Nombre
iii. Apellido 1
iv. Apellido 2
v. Tipo de integrante (músico/manager/técnico)
vi. Instrumento principal
vii. % ganancia
viii. Ganancia personal
'''
def muestra_banda(banda):
    if isinstance(banda, Banda):
        for integrante in banda.integrantes:
            print(banda.nombre)
            print(integrante.get_nombre())
            print(integrante.get_apellido1())
            print(integrante.get_apellido2())
            if isinstance(integrante, Musico):
                print("Músico")
                print(integrante.instrumento_principal)
                print(banda.distribucion_ganancias.get(integrante._nombre))
            elif isinstance(integrante, Manager):
                print("Manager")
                print("Los Manager no tocan instrumentos")
                print(integrante.quiero_mi_comision())
            elif isinstance(integrante, TecnicoSonido):
                print("Técnico de sónido")
                print("Los técnicos de sónido no tocan instrumentos.")
                print("Los técnicos de sónido no cobran por porcentage")
            print(integrante.get_ganancias())
            print()


    else:
        print('El objeto recibido no es una banda')

'''
11. Crea varias bandas que actúen en un festival y muestra sus datos usando
muestra_banda()
'''


muestra_banda(rolling_stones)
muestra_banda(dawn2)
muestra_banda(projecte_mut)
muestra_banda(iron_maiden)
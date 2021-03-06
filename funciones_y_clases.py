global1 = 34
#print(global1)

def cambiar_global(val1):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1 
    global1 = val1
    return global1
    pass
cambiar_global(2)

def anio_bisiesto(anio):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    if anio % 4 == 0 and anio % 100 != 0 and anio % 400:
      return True
    else:
      return False

    pass

def contar_valles(lista):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso 
    hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    conteo = 0
    n = 0
#negativo a positivo
    
    for el in lista:
      #print('n',n)
      #print('el',el)
      #print(lista[n+1])
      if n < len(lista)-1:
        if el > 0 and lista[n+1] >= 0:
          conteo += 1 
        n += 1
      
    return conteo 
    pass

#print(contar_valles([-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1]))

def saltando_rocas(lista):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    #lista = [1,0,0,1,0,1,1]
    # [0,1,1,0,0,1,0]
    # [0,0,1,0,1,1,0]
    n = 0
    salto = 0

    for el in lista:
      if n < (len(lista)-1):
        print('valor n',n)
        print('posicion',lista[n])
        if lista[n] == 0 and lista[n+1]== 1:
          salto += 0
          print('primer if')
        elif lista[n] == 0 and lista[n+1]== 1 :
          salto += 0
        elif lista[n] == 1 and lista[n+1]== 1:
          salto += 0
        elif lista[n] == 1 and lista[n+1]== 0:
          salto += 1
        n += salto
    
    return salto


    pass

print(saltando_rocas([0,0,1,0,1,1,0]))

def pares_medias():
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    # no se deben contar las medias que no tienen par 
    pass

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

class ListaComa:
  lista = None
  
  def __init__(self,lista):
      self.lista = lista
      print(lista)
      #return lista
  
  def __str__(self):
    #return " ".join([str(_) for _ in self.lista])
    return ",".join(map(str,self.lista))


#l = ListaComa(['a','b'])
l = ListaComa([1,2,3,4])
print('clase',str(l))




# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

class Persona: 
    nombres = []
    apellidos = []
    
    def __init__(self,nombres,apellidos):
        self.nombres = " ".join(map(str,nombres)).capitalize()
        self.apellidos = " ".join(map(str,apellidos)).capitalize()

    def nombre_completo(self): 
      return self.nombres + ' ' + self.apellidos        
      #return self.apellidos + ','

juan = Persona(['jose','david'],['gomez','diaz'])
print(juan.nombre_completo())

# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.


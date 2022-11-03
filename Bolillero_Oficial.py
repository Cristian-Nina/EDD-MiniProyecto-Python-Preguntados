import random
from preguntas_deportes import BASE_DEPORTES
from preguntas_historia import BASE_HISTORIA
from preguntas_ciencia import BASE_CIENCIA
from preguntas_geografia import BASE_GEOGRAFIA
from preguntas_arte import BASE_ARTE
from preguntas_entretenimiento import BASE_ENTRETENIMIENTO

class Bolillero:
  '''Con este objeto elegimos una pregunta para el jugador '''
  categorias_preguntas = ["Deporte","Historia","Arte","Ciencia","Entretenimiento","Geografia"]
  lista_categorias_bolillero = ["Deporte","Historia","Arte","Ciencia","Entretenimiento","Geografia","Corona"]

  def __init__(self):  #Constructor
    self.base_deportes = BASE_DEPORTES
    self.base_historia = BASE_HISTORIA
    self.base_ciencia = BASE_CIENCIA
    self.base_geografia = BASE_GEOGRAFIA
    self.base_arte = BASE_ARTE
    self.base_entretenimiento = BASE_ENTRETENIMIENTO
    self.preguntas_deportes = list(self.base_deportes.keys())
    self.preguntas_historia = list(self.base_historia.keys())
    self.preguntas_ciencia = list(self.base_ciencia.keys())
    self.preguntas_geografia = list(self.base_geografia.keys())
    self.preguntas_arte = list(self.base_arte.keys())
    self.preguntas_entretenimiento = list(self.base_entretenimiento.keys())
    return None


  def sacarpregunta(self): #se sacan las preguntas y sus opciones
    categoria_elegida = random.choice(self.categorias_preguntas)
    if categoria_elegida == "Deporte":
      pregunta = random.choice(self.preguntas_deportes)
      opciones = self.base_deportes[pregunta]
    elif categoria_elegida == "Historia":
      pregunta = random.choice(self.preguntas_historia)
      opciones = (self.base_historia[pregunta])
    elif categoria_elegida == "Arte":
      pregunta = random.choice(self.preguntas_arte)
      opciones = self.base_arte[pregunta]
    elif categoria_elegida == "Ciencia":
      pregunta = random.choice(self.preguntas_ciencia)
      opciones = self.base_ciencia[pregunta]
    elif categoria_elegida == "Geografia":
      pregunta = random.choice(self.preguntas_geografia)
      opciones = self.base_geografia[pregunta]
    elif categoria_elegida == "Entretenimiento":
      pregunta = random.choice(self.preguntas_entretenimiento)
      opciones = self.base_entretenimiento[pregunta]
    return categoria_elegida, pregunta, opciones

  def elegir_categoria(self): #Elige la categoria
    categoria_azar = random.choices(self.lista_categorias_bolillero)
    for categoria_elegir in categoria_azar:
      pass
    return categoria_elegir

  def corona_time(self): #Cuando podes conseguir la categoria

    print("")
    usuario_opcion = int(input("¿Que categoria queres?: "))
    while usuario_opcion == 0 or usuario_opcion >= 7:
      print("Ingrese de vuelta")
      usuario_opcion = int(input("¿Que categoria queres?: "))

    usuario_opcion -= 1
    personaje_corona = self.categorias_preguntas[usuario_opcion]
    if personaje_corona == "Arte":
      pregunta = random.choice(self.preguntas_arte)
      opciones = self.base_arte[pregunta]
    elif personaje_corona == "Deporte":
      pregunta = random.choice(self.preguntas_deportes)
      opciones = self.base_deportes[pregunta]
    elif personaje_corona == "Historia":
      pregunta = random.choice(self.preguntas_historia)
      opciones = self.base_historia[pregunta]
    elif personaje_corona == "Ciencia":
      pregunta = random.choice(self.preguntas_ciencia)
      opciones = self.base_ciencia[pregunta]
    elif personaje_corona == "Geografia":
      pregunta = random.choice(self.preguntas_geografia)
      opciones = self.base_geografia[pregunta]
    elif personaje_corona == "Entretenimiento":
      pregunta = random.choice(self.preguntas_entretenimiento)
      opciones = self.base_entretenimiento[pregunta]
    return pregunta, opciones, personaje_corona
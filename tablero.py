from Bolillero_Oficial import Bolillero
import random
boli = Bolillero()
class Tablero:
  '''Con este objeto los creamos el tablero para que puedan jugar '''

  def jugar(self, player,boli,rondas):

    contador_preguntas_correctas = 0
    perdio = False
    contar_coronas = 0
    print(f'''\n════════════════════════════\n   ► Turno de: {player.nombre} ◄\n categorias conseguidas : {player.contador_corona}/6\n         Ronda:{rondas}/3 \n════════════════════════════\n''')
    while not perdio:
      categoria = boli.elegir_categoria() #se elige la categoria al azar.
      #Deporte
      if categoria != "Corona": #Si la categoria que salio no es corona.
        categoria, pregunta, respuestas = boli.sacarpregunta()
        respuesta,lista_opciones = self.mostrar_pregunta(categoria, pregunta, respuestas)
        if lista_opciones[respuesta]:
          '''Si la respueta es correcta... '''
          print("\n╔════════════════════════╗\n║ ✓ Respuesta Correcta✓  ║\n╚════════════════════════╝\n")

          contador_preguntas_correctas += 1
        elif lista_opciones[respuesta] == False:
          '''Si la respueta NO ES correcta... '''
          print("\n┌────────────────────────┐\n│X Respuesta Incorrecta X│\n└────────────────────────┘\n")

          contador_preguntas_correctas = 0
          return 1  #Retorna si se esquivoco
        contador_corona = 0
        if contador_preguntas_correctas == 3:  #Si acierta 3 preguntas correctas puede conseguir categoria

          player.mostrar_corona() #Muestra las categorias del jugador
          respuesta_corona, lista_corona, categoria = self.mostrar_corona()
          if lista_corona[respuesta_corona]:
            print("\n╔════════════════════════╗\n║  ¡Respuesta Correcta!  ║\n║♦Conseguiste una corona♦║\n╚════════════════════════╝\n")
            contador_corona +=1

            contador_preguntas_correctas = 0
            #retorna las coronas
            #contar_coronas = player.otorgar_corona(categoria,contador_corona) #Le da la corona
            player.otorgar_corona(categoria,contador_corona) #Le da la corona
            if player.contador_corona == 6:
              return 0

          elif lista_corona[respuesta_corona] == False: #Si la respuesta de la corona no es correcta
            print("\n┌────────────────────────┐\n│  Respuesta Incorrecta  │\n│    No hay corona :C    │\n└────────────────────────┘\n")
            contador_preguntas_correctas = 0
            return 1
        if contar_coronas == 6:
          return False
      elif categoria == "Corona": #Si sale corona en el bolillero
        contador_corona = 0
        print("○ Que suerte la ruleta nos dio Corona!! ○")
        player.mostrar_corona()
        respuesta_corona, lista_corona, categoria = self.mostrar_corona()

        if lista_corona[respuesta_corona]:
          print("\n╔════════════════════════╗\n║  ¡Respuesta Correcta!  ║\n║♦Conseguiste una corona♦║\n╚════════════════════════╝\n")
          contador_corona +=1
          contador_preguntas_correctas = 0

          contar_coronas = player.otorgar_corona(categoria,contador_corona)
          if player.contador_corona == 6:
            return 0

        elif lista_corona[respuesta_corona] == False: #Si l respuesta de corona no es correcta

          print("\n┌────────────────────────┐\n│  Respuesta Incorrecta  │\n│    No hay corona :C    │\n└────────────────────────┘\n")
          contador_preguntas_correctas = 0
          return 1

    #Este def sirve para mostrar las preguntas
  def mostrar_pregunta(self, categoria, pregunta, respuestas):
    print(f"○ La ruleta nos dio {categoria}! ○ \n{pregunta}")
    lista_opciones1 = list()

    for clave, valor in respuestas.items():
      lista_opciones1.append(clave)
      random.shuffle(lista_opciones1)
    lista_opciones = list()
    contador = 0
    for clave1 in lista_opciones1:
      for clave2, valor2 in respuestas.items():
        if clave1 == clave2:
          contador = contador + 1
          print(f"{contador} --> {clave1}")
          lista_opciones.append(valor2)

    respuesta_usuario = int(input("¿Cual es la respuesta correcta?: "))
    while respuesta_usuario == 0 or respuesta_usuario >= 5:
      print("Ingrese de vuelta")
      respuesta_usuario = int(input("¿Cual es la respuesta correcta?: "))
    respuesta_usuario -= 1
    return respuesta_usuario , lista_opciones

  def mostrar_corona(self): #es para imprimir la respueta de la corona

    pregunta, opciones, categoria = boli.corona_time()
    contador = 0
    lista_opciones = list()
    lista_opciones1 = list()
    print(f"\n{categoria}\n{pregunta}")
    for mostrar_pregunta1,validar in opciones.items():
      lista_opciones1.append(mostrar_pregunta1)
    random.shuffle(lista_opciones1)
    for mostrar_pregunta in lista_opciones1:
      for pregunta1,opcion in opciones.items():
        if mostrar_pregunta == pregunta1:
          contador += 1
          print(f" {contador} --> {mostrar_pregunta}")
          lista_opciones.append(opcion)

    respuesta_usuario_corona = int(input("¿Cual es la respuesta correcta?: "))
    while respuesta_usuario_corona == 0 or respuesta_usuario_corona >= 5:
      print("Ingrese de vuelta")
      respuesta_usuario_corona = int(input("¿Cual es la respuesta correcta?: "))
    respuesta_usuario_corona -= 1
    return respuesta_usuario_corona, lista_opciones, categoria

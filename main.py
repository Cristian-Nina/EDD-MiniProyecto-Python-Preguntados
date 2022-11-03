from Bolillero_Oficial import Bolillero
from jugador import Jugador
from tablero import Tablero


def main():
  print("\nEl que tenga mas categorias en 3 rondas gana!!")

  tablero = Tablero()
  boli = Bolillero()
  nombre1 = input("♥ Ingrese el nombre del jugador 1: ")
  nombre2 = input("♥ Ingrese el nombre del jugador 2: ")
  
  player1 = Jugador(nombre1)
  player2 = Jugador(nombre2)
  nadie_gano = True
  rondas = 1

  while nadie_gano:  #Se empieza a jugar
    nadie_gano = tablero.jugar(player1,boli,rondas)
    verificar_ganador(player1)
    
    if nadie_gano == 1:
      nadie_gano = tablero.jugar(player2,boli, rondas)
      verificar_ganador(player2)
    rondas += 1
    if rondas == 4: #Si la ronda llega 4 se termina
      if player1.contador_corona > player2.contador_corona:
        print(f'''\n\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n Se acabaron las rondas\n   El ganador es: {player1.nombre} \n    con "{player1.contador_corona}" coronas\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')
        print(f"\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n█» FIN DEL JUEGO « █\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        volver_jugar()
      elif player2.contador_corona > player1.contador_corona:
        print(f'''\n\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n Se acabaron las rondas\n   El ganador es: {player2.nombre} \n    con "{player2.contador_corona}" coronas\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')
        print(f"\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n█» FIN DEL JUEGO « █\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        volver_jugar()
      elif player1.contador_corona == player2.contador_corona:
        print(f"\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n Se acabaron las rondas\n     Hubo un empate\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print(f"\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n█» FIN DEL JUEGO « █\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        volver_jugar()
        
      return None
  
  print(f"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n█» FIN DEL JUEGO « █\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")


def verificar_ganador(jugador):
  if jugador.contador_corona == 6:
    print(f'''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n El ganador es: {jugador.nombre} \n    con {jugador.contador_corona} categorias\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')
    
    volver_jugar()


  return None


def arrancar():
  jugar = int(input("\n╔════════════════════════════╗\n║ ¡Bienvenido al preguntados!║\n║        Desea jugar?        ║\n╚════════════════════════════╝\n1. Si\n2. No\n"))
  while jugar == 0 or jugar >= 3:
    print("Ingrese de vuelta")
    jugar = int(input("\n╔════════════════════════════╗\n║ ¡Bienvenido al preguntados!║\n║        Desea jugar?        ║\n╚════════════════════════════╝\n1. Si\n2. No\n"))
  if jugar == 1:
    main()
  elif jugar == 2:
    print("¡Has decidido no jugar!")

def volver_jugar():
  volve_jugar = int(input("\n ¿Desea volver a jugar?\n╚══════════════════════╝\n1. Si\n2. No \n"))
  while volve_jugar == 0 or volve_jugar >= 3:
    print("Ingrese de vuelta")
    volve_jugar = int(input("\n ¿Desea volver a jugar?\n╚══════════════════════╝\n1. Si\n2. No \n"))
  if volve_jugar == 1:
    main()
  elif volve_jugar == 2:
    print("¡Has decidido no volver a jugar!")


arrancar()
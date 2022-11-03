class Jugador:

  def __init__(self,nombre):
    self.nombre = nombre
    self.entretenimiento = False
    self.deportes = False
    self.ciencia = False
    self.historia = False
    self.arte = False
    self.geografia = False
    self.contador_corona = 0

  def mostrar_corona(self):
    print("¡Podes conseguir una categoria!")
    if self.deportes == True:
      print(f'''1 -> Ya tenes "Deporte"! ✓''')
    elif not self.deportes:
      print(f'''1 -> No tenes "Deporte" ''')
    if self.historia == True:
      print(f'''2 -> Ya tenes "Historia"! ✓ ''')
    elif not self.historia:
      print(f'''2 -> No tenes "Historia"''')
    if self.arte == True:
      print(f'''3 -> Ya tenes "Arte"! ✓''')
    elif not self.arte:
      print(f'''3 -> No tenes "Arte"''')
    if self.ciencia == True:
      print(f'''4 -> Ya tenes "Ciencia"! ✓''')
    elif not self.ciencia:
      print(f'''4 -> No tenes "Ciencia"''')
    if self.entretenimiento == True:
      print(f'''5 -> Ya tenes "Entretenimiento"! ✓''')
    elif not self.entretenimiento:
      print(f'''5 -> No tenes "Entretenimiento"''')
    if self.geografia == True:
      print(f'''6 -> Ya tenes "Geografia"! ✓ ''')
    elif not self.geografia:
      print(f'''6 -> No tenes "Geografia"''')
    print(f"Categorias obtenidas: {self.contador_corona}/6")

  def otorgar_corona(self,categoria,contador):
    self.contador_corona += contador
    #print(self.contador_corona)
    if categoria == "Arte":
      self.arte = True
    elif categoria == "Ciencia":
      self.ciencia = True
    elif categoria == "Deporte":
      self.deportes = True
    elif categoria == "Entretenimiento":
      self.entretenimiento = True
    elif categoria == "Geografia":
      self.geografia = True
    elif categoria == "Historia":
      self.historia = True
    return self.contador_corona

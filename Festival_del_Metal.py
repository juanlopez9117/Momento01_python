Registro_de_bandas = []
opcion = 0

while opcion != 5:
  
  agrupacion = {}
  
  print("*_*_*_*_* FESTIVAL DE METAL *_*_*_*_*")
  print("1. Ingresar una banda")
  print("2. Mostrar todas las bandas")
  print("3. Cambiar hora de presentación")
  print("4. Retirar una banda")
  print("5. Salir.")
  opcion = int(input("Digite una opción: "))

  if opcion == 1:
    agrupacion["nombre"] = input("Digite el nombre de la banda: ")
    agrupacion["id"] = int(input("Digite el id de la banda: "))
    agrupacion["genero"] = input("Que genero tocá? R/= ")
    agrupacion["hora_presentacion"] = input("Digite la hora de presentación (HH:mm): ")
    agrupacion["presentado"] = input("¿La banda ya se presento?: ")
    agrupacion["valor_pago"] = input("Valor a pagar: ")
    
    if agrupacion["presentado"].lower() == "si":
      agrupacion["presentado"] = True
    else:
      agrupacion["presentado"] = False
    
    Registro_de_bandas.append(agrupacion)

  elif opcion == 2:
    for agrupacion in Registro_de_bandas:
      if not agrupacion["presentado"]:
        print(f"La agrupación {agrupacion['nombre']} no se ha presentado")

  elif opcion == 3:
    for agrupacion in Registro_de_bandas:
      if not agrupacion["presentado"]:
        nombre = agrupacion["nombre"]
        print(f"Se cambiará la hora de la agrupación {nombre}")
        agrupacion["hora_presentacion"] = input(f"Digite la nueva hora de presentación: ")

  elif opcion == 4:
    for agrupacion in Registro_de_bandas:
      if not agrupacion["presentado"]:
        nombre = agrupacion["nombre"]
        Registro_de_bandas.remove(agrupacion)


print("Vuelva pronto")

def costo_total(costo_und, cantidad):
    total_costo = costo_und * cantidad
    return total_costo

def costo_und(fruta):
    return fruta['costo_und']

def ordenar_frutas(frutas):
    frutas_ordenadas = sorted(frutas, key=costo_und, reverse=True)
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio por unidad: {fruta['costo_und']}, Cantidad: {fruta['cantidad']}")

def mostrar_precio(frutas):
    fruta_barata = min(frutas, key=costo_und)
    fruta_cara = max(frutas, key=costo_und)
    print(f"La fruta más barata es: {fruta_barata['nombre']} con un precio por unidad: {fruta_barata['costo_und']}")
    print(f"La fruta más cara es: {fruta_cara['nombre']} con un precio por unidad: {fruta_cara['costo_und']}")



frutas = []
opcion = 0


print("*_*_*_*_* VENTA DE SALPICON *_*_*_*_*")

while opcion != 5:
    print("1. Ingresar frutas")
    print("2. Costo total del salpicón")
    print("3. Todas las frutas")
    print("4. Cuál es la fruta más barata y más cara")
    print("5. SALIR")

    opcion = int(input("Digite una opción: "))

    if opcion == 1:
        fruta = {}
        fruta["nombre"] = input("Digite el nombre de la fruta: ")
        fruta["cantidad"] = int(input("Digite la cantidad de frutas a comprar: "))
        fruta["id"] = int(input("Asignele un ID a la fruta: "))
        fruta["costo_und"] = float(input("Digite el precio por unidad: "))
        
        frutas.append(fruta)
    elif opcion == 2:
        costo_total = sum(costo_total(fruta['costo_und'], fruta['cantidad']) for fruta in frutas)
        print(f"El costo total del salpicón es: ${costo_total}")
    elif opcion == 3:
        ordenar_frutas(frutas)
    elif opcion == 4:
        mostrar_precio(frutas)
    elif opcion == 5:
        print("Finalizado el programa")
    else:
        print("Opción inválida, inténtalo de nuevo")

def quick_sort(lista):
    if len(lista) <=1:
        return  lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1] < pivote[1]]
        iguales = [x for x in lista [1:] if x == pivote]
        mayores = [x for x in lista [2:] if x > pivote[1]]

        return quick_sort(menores) + iguales + (mayores)


def busqueda(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

repartidores = {}

n= int(input("Cuantos repartidores desea ingresar: "))
for _ in range(n):
    while True:
        nombre = input("Nombre del repartidor: ")
        if nombre == "" or nombre  in repartidores:
            print("Este nombre ya se encuentra registrado.")
        else:
            break
    while True:
        try:
            paquetes = int(input("Cuantos paquetes entrego? "))
            if paquetes < 0:
                print("No se permiten cantidades negativas.")
            else:
                break
        except ValueError:
            print("Ingrese un numero valido.")

    while True:
        zona = input("Zona asignada: ")
        if zona == "":
            print("La zona no puede estar vacia.")
        else:
            break

    repartidores[nombre] = {
        "informacion" : {
            "paquetes" : paquetes,
            "zona" : zona
        }
    }

print("\n*******REGISTRO ORIGINAL*******")
print(repartidores)

listaOrdenada = [
    (nombre,datos["informacion"]["paquetes"],datos["informacion"]["zona"])
    for nombre,datos in repartidores.items()
]
ordenados = quick_sort(listaOrdenada)

print("\n*******RANKING*******")
for nombre in range(listaOrdenada):
    print(f"{nombre} - {paquetes} Paquetes - Zona: {zona}")

print("\n*******BUSCAR REPARTIDOR*******")
buscado = input("Nombre del repartidor: ")
buscadoLista = list(repartidores.keys())
pos = busqueda(buscadoLista,buscado)

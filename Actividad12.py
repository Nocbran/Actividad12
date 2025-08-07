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


    repartidores[nombre] = {
        "informacion" : {
            "paquetes" : paquetes,
            "zona" : zona
        }
    }
print("\n*******REGISTRO DE REPARTIDORES*******")
print(repartidores)

listaOrdenada = [
    (nombre,datos["informacion"]["paquetes"],datos["informacion"]["zona"])
    for nombre,datos in repartidores.items()
]
ordenados = quick_sort(listaOrdenada)

for nombre in range(listaOrdenada)


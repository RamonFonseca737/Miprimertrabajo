def mi_funcion():
    print("Hola desde modulo1")
BIENVENIDA="""
Te damos la bienvenida a de nuestra tienda de carros te daremos las opciones para escoger
1) Agregar carro
2) Eliminar carro
3) Ver la lista
4) Salir del programa
"""
cars = ["Nisan","BMW"]
element = []
while True:
    comands = input(BIENVENIDA)
    if comands =="1":
        element = input ("Agrega un carro ")
        cars.append(element)
        print(cars)
        break
    if comands == "2":
        element = input("Escribe el nombre del auto que quieres eliminar: ")
        cars.remove(element)
        print(f"{element} eliminado correctamente.")
    else:
        print(f"Advertencia: {element} no está en la lista.")
        print("Lista actualizada:", cars)
        break
    if comands =="3":
        print (cars)
        break
    if comands =="4":
        break
print("Gracias por utilizar el inventario")
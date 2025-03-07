def mi_funcion():
    print("Hola desde modulo1")
BIENVENIDA="""
Te damos la bienvenida a de nuestra tienda de motos te daremos las opciones para escoger
1) Agregar motos
2) Eliminar motos
3) Ver la lista
4) Salir del programa
"""
motors = ["Nisan","BMW"]
while True:
    opcion = input(BIENVENIDA)
    if opcion =="1":
        element = input ("Agrega un carro ")
        motors.append(element)
        print(motors)
        break
    if opcion == "2":
        if motors:
            moto = input("Escribe el nombre de la moto que quieres eliminar: ")
            if moto in motors:
                motors.remove(moto)
                print(f"{moto} eliminado correctamente.")
            else:
                print(f"Error: {moto} no está en la lista.")
                break
    else:
            print("No hay motos para borrar.")
            break
    if opcion =="3":
        print (opcion)
        break
    if opcion =="4":
        break
print("Gracias por utilizar el inventario")
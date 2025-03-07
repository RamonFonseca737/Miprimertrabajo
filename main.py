from src import taller_mecanico
taller_mecanico.mi_funcion()
def leer_readme():
    with open("README.md", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        return contenido

if __name__ == "__main__":
    contenido_readme = leer_readme()
    print(contenido_readme)
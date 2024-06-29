import json

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.cargar_datos()

    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor}
        self.libros.append(libro)
        self.guardar_datos()

    def mostrar_libros(self):
        for libro in self.libros:
            print(f'Título: {libro["titulo"]}, Autor: {libro["autor"]}')

    def buscar_libro(self, clave):
        resultados = [libro for libro in self.libros if clave.lower() in libro["titulo"].lower() or clave.lower() in libro["autor"].lower()]
        return resultados

    def guardar_datos(self):
        with open('biblioteca.json', 'w') as file:
            json.dump(self.libros, file)

    def cargar_datos(self):
        try:
            with open('biblioteca.json', 'r') as file:
                self.libros = json.load(file)
        except FileNotFoundError:
            self.libros = []

def main():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Agregar libro\n2. Mostrar todos los libros\n3. Buscar libro\n4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            biblioteca.agregar_libro(titulo, autor)
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            clave = input("Buscar por título o autor: ")
            resultados = biblioteca.buscar_libro(clave)
            for libro in resultados:
                print(f'Título: {libro["titulo"]}, Autor: {libro["autor"]}')
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

# mostrar_libros.py
def mostrar_libros():
    try:
        with open('data/libros.txt', 'r') as file:
            libros = file.readlines()
            if libros:
                print("\nLista de libros:")
                for libro in libros:
                    print(libro.strip())
            else:
                print("No hay libros registrados.")
    except FileNotFoundError:
        print("El archivo de libros no existe.")

if __name__ == "__main__":
    mostrar_libros()

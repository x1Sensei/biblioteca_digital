# buscar_autor.py
def buscar_autor(autor_buscar):
    try:
        with open('data/libros.txt', 'r') as file:
            libros = file.readlines()
            encontrados = [libro.strip() for libro in libros if autor_buscar.lower() in libro.lower()]
            if encontrados:
                print("\nLibros encontrados:")
                for libro in encontrados:
                    print(libro)
            else:
                print(f"No se encontraron libros de {autor_buscar}.")
    except FileNotFoundError:
        print("El archivo de libros no existe.")

if __name__ == "__main__":
    autor_buscar = input("Ingrese el autor a buscar: ")
    buscar_autor(autor_buscar)

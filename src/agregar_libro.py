# agregar_libro.py
def agregar_libro(titulo, autor, anio):
    with open('data/libros.txt', 'a') as file:
        file.write(f"{titulo},{autor},{anio}\n")
    print(f"Libro '{titulo}' agregado con éxito.")

if __name__ == "__main__":
    # Solicitar datos del libro
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio = input("Ingrese el año de publicación: ")
    
    agregar_libro(titulo, autor, anio)

import csv
from libro import Libro

class Biblioteca:
    def __init__(self, archivo= "inventario.txt"): 
        self.archivo = archivo

    def agregar_libro(self):
        try:
            titulo = input("Ingresa el título del libro: ").strip()
            autor = input("Ingresa el autor del libro: ").strip()
            fecha_publicacion = input("Ingresa la fecha de publicación del libro: ").strip()
            disponible = input("Estado (disponible/prestado): ").strip().lower()
            # Si no se ingresa estado, por defecto le asignamos "Disponible"
            disponible = disponible if disponible else "disponible"

            #Creamos el objeto libro que se validara con metodos de clase Libro
            libro = Libro(titulo, autor, fecha_publicacion, disponible)

            # Agregar el libro al archivo
            with open(self.archivo, "a", encoding="utf-8") as f:
                f.write(f"{titulo}, {autor}, {fecha_publicacion}, {disponible}\n")
        except Exception as e:


    def eliminar_libro(self, libro):
        pass

    def listar_libros(self):
        pass

    def buscar_libro(self, titulo):
        pass

    def prestar_libro(self):
        pass

    def devolver_libro(self):
        pass

    def listar_libros_prestados(self):
        pass


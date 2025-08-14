import os
from libro import Libro
from libro_digital import LibroDigital
from errores import LibroNoDisponibleError, LibroYaPrestadoError, LibroNoEncontradoError, LibroNoPrestadoError

class Biblioteca:
    """Se define clase Biblioteca para gestionar la biblioteca"""
    def __init__(self, archivo="biblioteca.txt"): 
        self.archivo = archivo
        self.libros: list[Libro] = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee los libros desde el archivo al iniciar"""
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    datos = linea.split("|")
                    if len(datos) == 4:
                        titulo, autor, anio, estado = datos
                        self.libros.append(Libro(titulo, autor, anio, estado))
                    elif len(datos) == 5:  # Libro digital
                        titulo, autor, anio, estado, formato = datos
                        self.libros.append(LibroDigital(titulo, autor, anio, estado, formato))
        except Exception as e:
            print(f"Error al cargar libros: {e}")
                        
    def guardar_en_archivo(self):
        """Guarda todos los libros en el archivo (sobrescribe)"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for libro in self.libros:
                    if isinstance(libro, LibroDigital):
                        f.write(f"{libro.get_titulo()}|{libro.get_autor()}|{libro.get_fecha_publicacion()}|{libro.get_disponible()}|{libro.get_formato()}\n")
                    else:
                        f.write(f"{libro.get_titulo()}|{libro.get_autor()}|{libro.get_fecha_publicacion()}|{libro.get_disponible()}\n")
        except Exception as e:
            print(f"Error al guardar libros: {e}")

    def agregar_libro(self):
        """Agrega un nuevo libro a la biblioteca"""
        try:
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            fecha_publicacion = input("Año de publicación: ").strip()

            disponible = (input("Estado (disponible/prestado) [disponible]: ").strip().lower() or "disponible")
            if disponible not in ("disponible", "prestado"):
                print("Estado inválido. Se usará 'disponible'.")
                disponible = "disponible"
            
            tipo = input("¿Es un libro físico o digital? (f/d): ").strip().lower()
            if tipo == "d":
                formato = input("Formato (PDF, EPUB, MOBI): ").strip().lower()
                libro = LibroDigital(titulo, autor, fecha_publicacion, disponible, formato)
            else:
                libro = Libro(titulo, autor, fecha_publicacion, disponible)

            self.libros.append(libro)
            self.guardar_en_archivo()
            print(f"Libro '{titulo}' agregado correctamente.")
        except Exception as e:
            print(f"Error al agregar el libro: {e}")

    def eliminar_libro(self):
        """Eliminar libro de la biblioteca"""
        objetivo = input("¿Qué libro desea eliminar?: ").strip().lower()
        encontrado = False
        nuevas_lineas = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.rstrip("\n")
                    if not linea:
                        continue
                    campos = linea.split("|")
                    titulo = campos[0].strip().lower()
                    if titulo == objetivo:
                        encontrado = True
                        continue
                    nuevas_lineas.append(linea + "\n")

            with open(self.archivo, "w", encoding="utf-8") as f:
                f.writelines(nuevas_lineas)

            #Sincroniza memoria
            self.libros = [l for l in self.libros if l.get_titulo().strip().lower() != objetivo]

            if encontrado:
                print(f"Libro '{objetivo}' eliminado.")
                return
            
            # No encontrado -> Error Personalizado
            raise LibroNoDisponibleError (f"Libro '{objetivo}' no disponible.")

        except FileNotFoundError:
            print(f"Error: No se encontro el archivo 'biblioteca.txt'")

        except Exception as e:
            print(f"Error inesperado al eliminar el libro: {e}")

    
    def listar_libros(self):
        """Listar libros de la biblioteca"""
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        
        for libro in self.libros:
            print(libro) # LLamamos al metodo  __str__()
            print("-" * 20)

    def buscar_libro(self):
        """Busca libro en la biblioteca por titulo (Coincidencia exacta)"""
        libro_buscar = input("¿Qué libro desea buscar?: ").strip().lower()
        encontrado = False
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue # Salta líneas vacias
                    atributos = [atributo.strip() for atributo in linea.split("|")]
                    nombre_libro = atributos[0].strip().lower()
                    
                    if nombre_libro == libro_buscar:
                        print("\n=== LIBRO ENCONTRADO ===")
                        print(f"Título: {atributos[0]}")
                        print(f"Autor: {atributos[1] if len(atributos) > 1 else ''}")
                        print(f"Fecha de publicación: {atributos[2] if len (atributos) > 2 else ''}")
                        print(f"Estado: {atributos[3] if len(atributos) > 3 else ''}")
                        if len(atributos) > 4:
                            print(f"Formato: {atributos[4]}")
                        encontrado = True
                        break
            if not encontrado:
                #Excepción personalizada
                raise LibroNoEncontradoError (f"Libro '{libro_buscar}' no encontrado.")

        except FileNotFoundError:
            print(f"Error: No se encontro el archivo 'biblioteca.txt'")

        except Exception as e:
            print(f"Error inesperado al buscar el libro: {e}")

    def prestar_libro(self):
        """Marcar un libro como prestado en biblioteca"""
        libro_prestado = input("¿Qué libro desea prestar?: ").strip().lower()

        for libro in self.libros:
            if libro.get_titulo().strip().lower() == libro_prestado:
                if libro.get_disponible().strip().lower() == "prestado":
                    raise LibroYaPrestadoError(f"El libro '{libro_prestado}' ya esta prestado.")            
                libro.set_disponible("prestado")
                self.guardar_en_archivo()
                print(f"Libro '{libro_prestado}' prestado correctamente.")
                return
            #Error personalizado
        raise LibroNoEncontradoError(f"Libro '{libro_prestado}' no encontrado.")
                        
    def devolver_libro(self):
        """Marcar un libro como disponible en biblioteca"""
        libro_devuelto = input("¿Qué libro desea devolver?: ").strip().lower()

        for libro in self.libros:
            if libro.get_titulo().strip().lower() == libro_devuelto:
                if libro.get_disponible().strip().lower() == "disponible":
                    raise LibroNoPrestadoError(f"El libro '{libro_devuelto}' no se encuentra prestado.")
                libro.set_disponible("disponible")
                self.guardar_en_archivo()
                print(f"Libro '{libro_devuelto}' devuelto correctamente.")
                return
            #Error personalizado
        raise LibroNoEncontradoError(f"Libro '{libro_devuelto}' no encontrado.")

    def listar_libros_prestados(self):
        """Listar libros prestados de la biblioteca"""
        libros_prestados = [libro for libro in self.libros if libro.get_disponible().strip().lower() == "prestado"]
        if not libros_prestados:
            print("No hay libros prestados en la biblioteca.")
            return
        for libro in libros_prestados:
            print(libro) # Usa __str__ de Libro o LibroDigital
            print("-" * 20)


    def listar_libros_disponibles(self):
        """Listar libros disponibles de la biblioteca"""
        disponibles = [l for l in self.libros if l.get_disponible().strip().lower() == "disponible"]
        if not disponibles:
            print("No hay libros disponibles en la biblioteca.")
            return
        print("\n=== LIBROS DISPONIBLES ===")
        for l in disponibles:
            print(l)
            print("-" * 20)
import os
from libro import Libro
from libro_digital import LibroDigital
from errores import LibroNoDisponibleError, LibroYaPrestadoError, LibroNoEncontradoError

class Biblioteca:
    """Gestión de una biblioteca con persistencia en archivo de texto."""
    def __init__(self, archivo: str = "biblioteca.txt"):
        self.archivo = archivo
        self.libros: list[Libro] = []
        self.cargar_desde_archivo()

    # ------------------ Persistencia ------------------ #
    def cargar_desde_archivo(self) -> None:
        """Lee los libros desde el archivo al iniciar (formato: T|A|AÑO|ESTADO[|FORMATO])."""
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split("|")
                    if len(partes) == 4:
                        titulo, autor, anio_str, estado = partes
                        anio: Optional[int] = self._parse_anio(anio_str)
                        self.libros.append(Libro(titulo, autor, anio, estado))
                    elif len(partes) == 5:
                        titulo, autor, anio_str, estado, formato = partes
                        anio: Optional[int] = self._parse_anio(anio_str)
                        self.libros.append(LibroDigital(titulo, autor, anio, estado, formato))
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    def guardar_en_archivo(self) -> None:
        """Guarda todos los libros en el archivo (sobrescribe)."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for libro in self.libros:
                    # Año: escribe vacío si es None
                    anio = libro.get_fecha_publicacion()
                    anio_str = "" if anio is None else str(anio)
                    if isinstance(libro, LibroDigital):
                        f.write(
                            f"{libro.get_titulo()}|{libro.get_autor()}|{anio_str}|{libro.get_disponible()}|{libro.get_formato()}\n"
                        )
                    else:
                        f.write(
                            f"{libro.get_titulo()}|{libro.get_autor()}|{anio_str}|{libro.get_disponible()}\n"
                        )
        except Exception as e:
            print(f"Error al guardar libros: {e}")

# ------------------ Metodos ------------------ #
    def agregar_libro(self) -> None:
        """Agrega un nuevo libro (interactivo). Estado se maneja como string."""
        try:
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            anio_in = input("Año de publicación (opcional): ").strip()
            anio = self._parse_anio(anio_in)

            estado = (input("Estado (disponible/prestado) [disponible]: ").strip().lower() or "disponible")
            if estado not in ("disponible", "prestado"):
                print("Estado inválido. Se usará 'disponible'.")
                estado = "disponible"

            tipo = input("¿Es un libro físico o digital? (f/d): ").strip().lower()
            if tipo == "d":
                formato = input("Formato (PDF, EPUB, MOBI): ").strip()
                libro = LibroDigital(titulo, autor, anio, estado, formato)
            else:
                libro = Libro(titulo, autor, anio, estado)

            self.libros.append(libro)
            self.guardar_en_archivo()
            print(f"Libro '{titulo}' agregado correctamente.")
        except Exception as e:
            print(f"Error al agregar el libro: {e}")

    def eliminar_libro(self) -> None:
        """Elimina un libro por su título (interactivo)."""
        objetivo = input("¿Qué libro desea eliminar?: ").strip().lower()
        encontrado = False
        try:
            # Filtra en memoria
            antes = len(self.libros)
            self.libros = [l for l in self.libros if l.get_titulo().strip().lower() != objetivo]
            encontrado = len(self.libros) < antes

            # Persiste cambios
            self.guardar_en_archivo()

            if encontrado:
                print(f"Libro '{objetivo}' eliminado.")
            else:
                # Si tienes excepción custom, puedes usarla:
                # raise LibroNoEncontradoError(f"No se encontró el libro '{objetivo}'.")
                print(f"No se encontró el libro '{objetivo}'.")
        except Exception as e:
            print(f"Error al eliminar el libro: {e}")

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


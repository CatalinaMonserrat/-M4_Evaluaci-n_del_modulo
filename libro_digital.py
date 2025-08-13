from libro import Libro
from typing import Optional

class LibroDigital(Libro):
    """Clase que hereda de libro y que representa un libro digital"""
    def __init__(self, titulo, autor, fecha_publicacion: Optional[int], disponible=True, formato="Físico"):
        super().__init__(titulo, autor, fecha_publicacion, disponible)
        self.set_formato(formato)


    def get_formato(self):
        """Función para acceder al atributo formato"""
        return self._formato

    def set_formato(self, formato: str):   
        """Función para modificar el formato del libro"""
        if not isinstance(formato, str) or not formato.strip():
            raise ValueError("El formato no puede estar vacío")
        self._formato = formato.strip()

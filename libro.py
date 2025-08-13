from typing import Optional

class Libro:
    """Definición de clase Libro y sus atributos - métodos"""
    def __init__(self, titulo: str, autor: str, fecha_publicacion: Optional[int], disponible: str):
        # Atributos base
        self._titulo: str = None
        self._autor: str = None
        self._fecha_publicacion: Optional[int] = None  # Dejamos None por defecto
        self._disponible: str = "disponible"  # Valor por defecto

        # Setters para inicializar con validación
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_fecha_publicacion(fecha_publicacion)
        self.set_disponible(disponible)

    # ======= GETTERS =======
    def get_titulo(self):
        """Accede al atributo título"""
        return self._titulo

    def get_autor(self):
        """Accede al atributo autor"""
        return self._autor

    def get_fecha_publicacion(self):
        """Accede al atributo fecha de publicación"""
        return self._fecha_publicacion

    def get_disponible(self):
        """Accede al estado disponible como string"""
        return self._disponible

    # ======= SETTERS =======
    def set_titulo(self, nuevo_titulo: str):
        if not isinstance(nuevo_titulo, str) or not nuevo_titulo.strip():
            raise ValueError("El título no puede estar vacío")
        self._titulo = nuevo_titulo.strip()

    def set_autor(self, nuevo_autor: str):
        if not isinstance(nuevo_autor, str) or not nuevo_autor.strip():
            raise ValueError("El autor no puede estar vacío")
        self._autor = nuevo_autor.strip()

    def set_fecha_publicacion(self, nueva_fecha: Optional[int]):
        if nueva_fecha in (None, ""):
            self._fecha_publicacion = None
            return
        try:
            fecha = int(str(nueva_fecha).strip())
            if not (1400 <= fecha <= 2100):
                raise ValueError("El año debe estar entre 1400 y 2100")
            self._fecha_publicacion = fecha
        except ValueError:
            raise ValueError("La fecha debe ser un entero válido")

    def set_disponible(self, estado: str):
        if not isinstance(estado, str):
            raise ValueError("El estado debe ser un texto")
        estado = estado.strip().lower()
        if estado not in ("disponible", "prestado"):
            raise ValueError("El estado debe ser 'disponible' o 'prestado'")
        self._disponible = estado

    # ======= Representación Legible =======
    def __str__(self):
        fecha = self._fecha_publicacion if self._fecha_publicacion is not None else "Desconocida"
        return f"{self._titulo} ({self._autor}, {fecha}, estado: {self._disponible.capitalize()})"
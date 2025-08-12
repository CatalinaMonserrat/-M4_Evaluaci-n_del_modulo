from typing import Optional
"""Utilización de type hiting con Optional (int) para validar el ingreso de fecha"""

class Libro:
    """Definición de clase Libro y sus atributos - metodos"""
    def __init__(self, titulo, autor, fecha_publicacion: Optional[int], disponible):
        # Atributos base
        self._titulo: str = None
        self._autor: str = None
        self._fecha_publicacion: Optional[int] = None #Dejamos None por defecto
        self._disponible: bool = True
        # Setters
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_fecha_publicacion(fecha_publicacion)
        # Normaliza el estado con una sola función
        self._disponible = self._to_bool_estado(disponible)
            
# Transforaremos los estados a booleanos ya sean str, bool o int
    _ESTADOS_TRUE = ("disponible", "si", "sí", "true", "1", "y", "yes")
    _ESTADOS_FALSE = ("prestado", "no", "nó", "false", "0", "n", "not")

    def _to_bool_estado(self, valor) -> bool:
        """Función para transformar los estados a booleanos estandarizados"""
        if isinstance(valor, bool):
            return valor
        if not isinstance(valor, str):
            return bool(valor)
        v = valor.strip().lower()
        if v in Libro._ESTADOS_TRUE: 
            return True
        if v in Libro._ESTADOS_FALSE: 
            return False
        raise ValueError(f"Estado {valor} no reconocido")
        
#=======GETTERS=======
    def get_titulo(self):
        """Función para acceder al atributo título del libro"""
        return self._titulo
        
    def get_autor(self):
        """Función para acceder al atributo autor"""
        return self._autor
        
    def get_fecha_publicacion(self):
        """Función para acceder al atributo fecha de publicación"""
        return self._fecha_publicacion
        
    def get_disponible(self):
        """Función para acceder al atributo estado disponible"""
        return self._disponible

    #=======SETTERS=======
    def set_titulo(self, nuevo_titulo):
        if not isinstance(nuevo_titulo, str) or not nuevo_titulo.strip():
            raise ValueError("El título no puede estar vacío")
        self._titulo = nuevo_titulo.strip()

    def set_autor(self, nuevo_autor):
        if not isinstance(nuevo_autor, str) or not nuevo_autor.strip():
            raise ValueError("El autor no puede estar vacío")
        self._autor = nuevo_autor.strip()

    def set_fecha_publicacion(self, nueva_fecha: Optional[int]):
        if nueva_fecha in (None, ""): # Si no se ingresa fecha
            self._fecha_publicacion = None
            return
        try:
            fecha = int(str(nueva_fecha).strip())
            if not (1400 <= fecha <= 2100): #Dejamos una validación de rango de años amplia
                raise ValueError ("El año debe estar entre 1400 y 2100")
            self._fecha_publicacion = fecha
        except ValueError:
            raise ValueError("La fecha debe ser un entero valido")

    def set_disponible(self, estado):
        self._disponible = self._to_bool_estado(estado)
                
    #=======Representación Legible=======      
    def __str__(self):
        estado_texto = "Disponible" if self._disponible else "Prestado"
        fecha = self._fecha_publicacion if self._fecha_publicacion is not None else "Desconocida"
        return f"{self._titulo} ({self._autor}, {fecha}, estado: {estado_texto})"           

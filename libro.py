class Libro:
    def __init__(self, titulo, autor, fecha_publicacion, disponible):
        # Se usaran setters para validad desde el inicio
        self._titulo = None
        self._autor = None
        self._fecha_publicacion = ""
        self._disponible = True

        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_fecha_publicacion(fecha_publicacion)

        # Validar disponibilidad
        if isinstance(disponible, str):
            estado_norm = disponible.strip().lower()
            disponible_validos = ("disponible", "si", "sí", "true")
            prestados_validos = ("prestado", "no", "nó", "false")
            if estado_norm in disponible_validos:
                self._disponible = True
            elif estado_norm in prestados_validos:
                self._disponible = False
            else:
                raise ValueError(f"Estado {disponible} no reconocido")
        else:
            self._disponible = bool(disponible)

#=======GETTERS=======
    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def get_fecha_publicacion(self):
        return self._fecha_publicacion
    
    def get_disponible(self):
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

    def set_fecha_publicacion(self, nueva_fecha):
        if nueva_fecha in (None, ""):
            self._fecha_publicacion = ""
            return
        try:
            fecha = int(str(nueva_fecha).strip())
            self._fecha_publicacion = fecha
        except ValueError:
            raise ValueError("La fecha debe ser un entero")

    def set_disponible(self, estado):
        if isinstance(estado, str):
            estado_norm = estado.strip().lower()
            if estado_norm not in ("disponible", "prestado"):
                raise ValueError("El estado debe ser 'disponible' o 'prestado'")
            self._disponible = (estado_norm == "disponible")
        else:
            self._disponible = bool(estado)
            
#=======Representación Legible=======      
    def __str__(self):
        estado_texto = "Disponible" if self._disponible else "Prestado"
        fecha = self._fecha_publicacion if self._fecha_publicacion != "" else "Desconocida"
        return f"{self._titulo} ({self._autor}, {fecha}, estado: {estado_texto})"           

📚 Gestor de Biblioteca en Python

Este proyecto es un sistema de gestión de biblioteca desarrollado en Python que permite administrar libros físicos y digitales, almacenando la información en un archivo de texto (biblioteca.txt).
El programa funciona a través de un menú interactivo en consola que permite al usuario agregar, buscar, prestar, devolver, listar y eliminar libros.

📌 Funcionalidades

Agregar libro: Permite registrar libros físicos o digitales, especificando título, autor, año de publicación, estado y formato (en caso de ser digital).
Eliminar libro: Elimina un libro del inventario buscando por título.
Listar libros:
  Todos los libros registrados.
  Solo los disponibles.
  Solo los prestados.
  Buscar libro: Busca un libro por su título y muestra sus detalles.
  Prestar libro: Cambia el estado de un libro de “disponible” a “prestado” (con manejo de error si ya está prestado).
  Devolver libro: Cambia el estado de un libro de “prestado” a “disponible”.
  Guardar y cargar desde archivo: Los cambios se almacenan en biblioteca.txt para conservar la información entre ejecuciones.

🛠️ Tecnologías utilizadas

Python 3
Manejo de archivos (open, read, write)
Programación Orientada a Objetos (POO)
Manejo de excepciones (incluyendo errores personalizados)
Uso de listas por comprensión para filtrado de datos

📌 Estructura del proyecto
```
📁 gestor_biblioteca
 ├── main.py                # Archivo principal con el menú interactivo
 ├── biblioteca.py          # Clase Biblioteca y sus métodos
 ├── libro.py               # Clase Libro (base)
 ├── libro_digital.py       # Clase LibroDigital (hereda de Libro)
 ├── errores.py             # Clases de errores personalizados
 ├── biblioteca.txt         # Archivo donde se guardan los libros
 └── README.md              # Documentación del proyecto
```
📌 Formato del archivo biblioteca.txt

Cada libro se guarda en una línea con el siguiente formato:
Para libros físicos:
```
  Título|Autor|Año de publicación|Estado
```
Para libros digitales:
```
  Título|Autor|Año de publicación|Estado|Formato
```
Ejemplo:
```
  Lo frágil y lo eterno|Bruno Puelles|2024|prestado
  La hipótesis del amor|Ali Hazelwood|2021|disponible|EPUB
```
📌 Cómo ejecutar el programa

Clonar este repositorio o descargar los archivos.
Asegurarse de tener Python 3 instalado.
Abrir una terminal en la carpeta del proyecto.

Ejecutar:
python main.py

Seguir las instrucciones del menú interactivo.

📌 Notas

Si el archivo biblioteca.txt no existe, el programa lo creará automáticamente.
Los cambios realizados (agregar, eliminar, prestar, devolver) se guardan automáticamente en el archivo.
Se incluyen errores personalizados para casos como libro no encontrado o libro ya prestado.

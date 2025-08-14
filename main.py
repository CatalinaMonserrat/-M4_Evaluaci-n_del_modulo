from gestor_biblioteca import Biblioteca
from errores import LibroNoDisponibleError, LibroYaPrestadoError, LibroNoEncontradoError, LibroNoPrestadoError
"""LLama a Gestor de Biblioteca y errores"""
def menu():
    """Muestra el menu de opciones"""
    print("\n=== GESTOR BIBLIOTECA ===")
    print("1) Agregar libro")
    print("2) Eliminar libro")
    print("3) Listar todos")
    print("4) Listar disponibles")
    print("5) Listar prestados")
    print("6) Buscar (exacto en archivo)")
    print("7) Prestar libro")
    print("8) Devolver libro")
    print("9) Salir")

def main():
    """Función principal del programa"""
    biblio = Biblioteca("biblioteca.txt")

    while True:
        menu()
        opcion = input("Elige una opción: ").strip()

        try:
            if opcion == "1":
                biblio.agregar_libro()
            elif opcion == "2":
                biblio.eliminar_libro()
            elif opcion == "3":
                biblio.listar_libros()
            elif opcion == "4":
                biblio.listar_libros_disponibles()
            elif opcion == "5":
                biblio.listar_libros_prestados()
            elif opcion == "6":
                biblio.buscar_libro()
            elif opcion == "7":
                biblio.prestar_libro()
            elif opcion == "8":
                biblio.devolver_libro()
            elif opcion == "9":
                print("Saliendo del programa...")
                break
            else:
                print("Opción invalida. Intenta nuevamente")

        except (LibroNoDisponibleError, LibroYaPrestadoError, LibroNoEncontradoError, LibroNoPrestadoError) as e:
            print(f"⚠️ {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
import time
from lector_csv import LectorCSV
from gestor_clientes import GestorClientes

# Función que muestra el menú de opciones al usuario
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Buscar cliente por ID")
    print("2. Listar por ciudad")
    print("3. Ordenar por edad")
    print("4. Salir")

# Función principal del programa
def main():
    ruta_csv = "clientes.csv"  # Ruta del archivo CSV con los datos de los clientes
    clientes, valido = LectorCSV.cargar_csv(ruta_csv)  # Carga los datos desde el CSV

    if not valido:
        return  # Si la carga no fue exitosa, se termina la ejecución

    gestor = GestorClientes(clientes)  # Se crea una instancia del gestor de clientes

    # Bucle principal del programa
    while True:
        mostrar_menu()  # Muestra las opciones del menú
        opcion = input("Seleccione una opción: ")  # Solicita la opción del usuario

        if opcion == "1":
            # Opción para buscar cliente por ID
            id_busqueda = input("Ingrese el ID del cliente: ")
            
            # Medir el tiempo de ejecución del método de búsqueda
            inicio = time.perf_counter()
            for _ in range(100):  # Repetir 100 veces para obtener tiempo promedio
                cliente = gestor.buscar_por_id(id_busqueda)
            fin = time.perf_counter()

            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")
            print(f"Tiempo promedio de búsqueda por ID: {(fin - inicio) / 100:.6f} segundos")

        elif opcion == "2":
            # Opción para listar clientes por ciudad
            ciudad = input("Ingrese la ciudad: ")
            
            # Medir el tiempo de ejecución del filtrado por ciudad
            inicio = time.perf_counter()
            for _ in range(100):  # Repetir 100 veces para obtener tiempo promedio
                resultados = gestor.listar_por_ciudad(ciudad)
            fin = time.perf_counter()

            if resultados:
                for c in resultados:
                    print(c)
            else:
                print("No se encontraron clientes para la ciudad ingresada.")
            print(f"Tiempo promedio de búsqueda por ciudad: {(fin - inicio) / 100:.6f} segundos")

        elif opcion == "3":
            # Opción para ordenar clientes por edad

            # Medir el tiempo de ejecución del ordenamiento
            inicio = time.perf_counter()
            for _ in range(100):  # Repetir 100 veces para obtener tiempo promedio
                ordenados = gestor.ordenar_por_edad()
            fin = time.perf_counter()

            for c in ordenados:
                print(c)
            print(f"Tiempo promedio de ordenamiento por edad: {(fin - inicio) / 100:.6f} segundos")

        elif opcion == "4":
            # Opción para salir del programa
            print("Saliendo del sistema...")
            break
        else:
            # Mensaje en caso de opción no válida
            print("Opción inválida. Intente nuevamente.")

# Punto de entrada del script
if __name__ == "__main__":
    main()

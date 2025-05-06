import csv
import os
import re
from cliente import Cliente

class LectorCSV:
    @staticmethod
    def contiene_tildes(texto):
        # Verifica si el texto contiene letras con tilde (mayúsculas o minúsculas)
        return bool(re.search(r"[áéíóúÁÉÍÓÚ]", texto))

    @staticmethod
    def cargar_csv(ruta_archivo):
        # Verifica si el archivo existe y no está vacío
        if not os.path.exists(ruta_archivo) or os.path.getsize(ruta_archivo) == 0:
            print("Archivo no encontrado o vacío. Verifique la ubicación del archivo.")
            return [], False

        clientes = []
        errores = 0

        try:
            # Abre el archivo CSV en modo lectura con codificación UTF-8
            with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)  # Lee el archivo como diccionario por fila

                # Verifica que el archivo contenga las columnas necesarias
                columnas_esperadas = {"id", "nombre", "email", "ciudad", "edad"}
                if not columnas_esperadas.issubset(lector.fieldnames):
                    print("Estructura del archivo inválida. Se requieren las columnas id, nombre, email, ciudad, edad.")
                    return [], False

                # Procesa cada fila del archivo
                for fila in lector:
                    try:
                        # Limpia espacios en blanco de cada campo
                        id_cliente = fila['id'].strip()
                        nombre = fila['nombre'].strip()
                        email = fila['email'].strip()
                        ciudad = fila['ciudad'].strip()
                        edad_str = fila['edad'].strip()
                        extra = fila.get('extra', '').strip().lower()  # Campo opcional 'extra'

                        # Validaciones personalizadas
                        if not nombre or not ciudad:
                            raise ValueError("Nombre o ciudad vacíos.")
                        if LectorCSV.contiene_tildes(nombre) or LectorCSV.contiene_tildes(ciudad):
                            raise ValueError("Nombre o ciudad con tildes.")
                        if extra == "dato_invalido":
                            raise ValueError("Campo 'extra' con dato inválido.")

                        edad = int(edad_str)  # Conversión de edad a entero

                        # Crea un objeto Cliente con los datos válidos
                        cliente = Cliente(id_cliente, nombre, email, ciudad, edad)
                        clientes.append(cliente)

                    except Exception as e:
                        # Captura y reporta errores en registros individuales
                        print(f"Registro inválido (ID: {fila.get('id', 'sin ID')}): {e}")
                        errores += 1

            if errores:
                print(f"\nSe ignoraron {errores} registros erróneos o inválidos.")

            # Devuelve la lista de clientes válidos y una bandera de éxito
            return clientes, True

        except Exception as e:
            # Captura errores generales al leer el archivo
            print(f"Error al leer el archivo: {e}")
            return [], False

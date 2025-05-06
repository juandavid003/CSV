import re

class Cliente:
    def __init__(self, id, nombre, email, ciudad, edad):
        # Validación: el nombre no puede estar vacío
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        
        # Validación: el email debe tener un formato válido
        if not email or not self.validar_email(email):
            raise ValueError("El email no es válido.")
        
        # Asignación de atributos
        self.id = id
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad
        self.edad = int(edad)  # Asegurarse de que la edad sea un entero

    def __str__(self):
        # Representación en forma de cadena del cliente
        return f"{self.id} - {self.nombre} - {self.email} - {self.ciudad} - {self.edad} años"

    def validar_email(self, email):
        # Expresión regular simple para validar el formato del email
        patron = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(patron, email) is not None  # Retorna True si el email es válido

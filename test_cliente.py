# test_cliente.py
import pytest  # Librería para escribir y ejecutar pruebas en Python
from cliente import Cliente  # Importa la clase Cliente desde el módulo cliente

# Test que verifica que un cliente se crea correctamente con todos los atributos válidos
def test_cliente_creation():
    """Test para verificar que un cliente se crea correctamente."""
    cliente = Cliente("1", "Juan Pérez", "juan@email.com", "Madrid", 30)
    # Se comprueba que cada atributo fue asignado correctamente
    assert cliente.id == "1"
    assert cliente.nombre == "Juan Pérez"
    assert cliente.email == "juan@email.com"
    assert cliente.ciudad == "Madrid"
    assert cliente.edad == 30

# Test que verifica que se lanza un error si el email no tiene un formato válido
def test_cliente_invalid_email():
    """Test para verificar que se lance un error con un email inválido."""
    # Se espera que al crear un cliente con email inválido se lance un ValueError
    with pytest.raises(ValueError):
        Cliente("2", "Ana García", "ana-email.com", "Barcelona", 25)

# Test que verifica que se lanza un error si el nombre está vacío
def test_cliente_empty_name():
    """Test para verificar que se lance un error si el nombre está vacío."""
    # Se espera que al crear un cliente sin nombre se lance un ValueError
    with pytest.raises(ValueError):
        Cliente("3", "", "ana@email.com", "Madrid", 25)

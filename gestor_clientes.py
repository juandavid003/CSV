class GestorClientes:
    def __init__(self, lista_clientes):
        # Inicializa el gestor con una lista de objetos Cliente
        self.clientes = lista_clientes

    def buscar_por_id(self, id_busqueda):
        # Busca un cliente por su ID utilizando una expresión generadora
        cliente = next((c for c in self.clientes if c.id == id_busqueda), None)
        if cliente is None:
            print("Cliente no encontrado.")  # Mensaje si no se encuentra el cliente
        return cliente  # Devuelve el cliente encontrado o None

    def listar_por_ciudad(self, ciudad):
        # Filtra los clientes que pertenecen a una ciudad específica
        resultados = [c for c in self.clientes if c.ciudad == ciudad]
        if not resultados:
            print("No se encontraron clientes para la ciudad ingresada.")
        return resultados  # Devuelve la lista (posiblemente vacía) de clientes filtrados

    def ordenar_por_edad(self):
        # Ordena la lista de clientes por edad de menor a mayor
        return sorted(self.clientes, key=lambda c: c.edad)

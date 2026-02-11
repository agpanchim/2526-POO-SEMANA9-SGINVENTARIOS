# Clase Inventario
# Gestiona la lista de productos

class Inventario:
    def __init__(self):
        # Lista principal donde se guardan los productos
        self.productos = []

    # Añadir producto (ID no repetido)
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: el ID ya existe.")
                return
        self.productos.append(producto)
        print(" Producto agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑️ Producto eliminado.")
                return
        print(" Producto no encontrado.")

    # Actualizar cantidad o precio por ID
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    # 🔍 BUSCAR PRODUCTO POR ID (CAMBIO QUE PEDISTE)
    def buscar_por_id(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                return p
        return None

    # Mostrar todos los productos
    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

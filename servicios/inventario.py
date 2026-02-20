# Clase Inventario
# Gestiona la lista de productos

class Inventario:
    def __init__(self, archivo="servicios/inventario.txt"):
        # Lista principal donde se guardan los productos
        self.productos = []
        # Nombre del archivo donde se almacenará el inventario
        self.archivo = archivo
        # Cargar datos automáticamente al iniciar
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")

                    # Verificamos que la línea tenga 4 datos
                    if len(datos) == 4:
                        from modelos.producto import Producto
                        producto = Producto(
                            datos[0],  # id
                            datos[1],  # nombre
                            int(datos[2]),  # cantidad
                            float(datos[3])  # precio
                        )
                        self.productos.append(producto)

            print(" Inventario cargado correctamente desde el archivo.")

        except FileNotFoundError:
            print(" Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()

        except PermissionError:
            print(" Error: No tienes permisos para leer el archivo.")

        except Exception as e:
            print(f" Error al cargar el archivo (posible archivo corrupto): {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)

            print(" Inventario guardado correctamente en el archivo.")

        except PermissionError:
            print(" Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print(f" Error inesperado al guardar: {e}")

    # Añadir producto (ID no repetido)
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: el ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(" Producto agregado correctamente.")


    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
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
                self.guardar_en_archivo()
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    # BUSCAR PRODUCTO POR ID (CAMBIO QUE PEDISTE)
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

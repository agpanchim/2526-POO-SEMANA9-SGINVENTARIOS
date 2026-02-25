# Clase Inventario
# Gestiona la lista de productos

import os

class Inventario:
    def __init__(self, archivo=None):

# Diccionario que almacena los productos usando el ID como clave
# Esto permite búsquedas rápidas y eficientes
        self.productos = {}

        # Ruta segura al archivo inventario.txt
        if archivo is None:
            ruta_base = os.path.dirname(__file__)
            archivo = os.path.join(ruta_base, "inventario.txt")

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
                        self.productos[producto.get_id()] = producto

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
                for p in self.productos.values():
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)

            print(" Inventario guardado correctamente en el archivo.")

        except PermissionError:
            print(" Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print(f" Error inesperado al guardar: {e}")

    # Añadir producto (ID no repetido)
    def agregar_producto(self, producto):
        # Verificar si el ID ya existe
        if producto.get_id() in self.productos:
            print("⚠️ Error: Ya existe un producto con ese ID.")
            return

        # Agregar el producto al diccionario usando el ID como clave
        self.productos[producto.get_id()] = producto
        # Guardar los cambios en el archivo
        self.guardar_en_archivo()
        # Mensaje de confirmación
        print("✅ Producto agregado correctamente.")


    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Actualizar cantidad o precio por ID
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:

            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)

            if precio is not None:
                self.productos[id_producto].set_precio(precio)

            self.guardar_en_archivo()
            print("Producto actualizado.")

        else:
            print("Producto no encontrado.")

    # BUSCAR PRODUCTO POR ID
    def buscar_por_id(self, id_producto):
        return self.productos.get(id_producto, None)

    # BUSCAR PRODUCTO POR NOMBRE
    # Permite encontrar uno o varios productos usando el nombre
    # Se utiliza una lista para almacenar los productos encontrados
    # Se compara el nombre sin importar mayúsculas o minúsculas
    def buscar_por_nombre(self, nombre):

        # Lista donde se guardarán los productos encontrados
        encontrados = []

        # Recorremos todos los productos del diccionario
        for producto in self.productos.values():

            # Comparación sin importar mayúsculas/minúsculas
            if producto.get_nombre().lower() == nombre.lower():
                # Se agrega el producto a la lista
                encontrados.append(producto)

        # Retorna la lista de productos encontrados
        return encontrados

    # Mostrar todos los productos del inventario
    def listar_productos(self):
        # Verificamos si el inventario está vacío
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")
            # Recorremos el diccionario de productos
            for producto in self.productos.values():
                print(producto)
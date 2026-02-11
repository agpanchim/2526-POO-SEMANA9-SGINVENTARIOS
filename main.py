from modelos.producto import Producto
from servicios.inventario import Inventario

# Mostrar menú
def mostrar_menu():
    print("\n    SISTEMA DE GESTION DE INVENTARIO ")
    print( )
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por ID")
    print("5. Listar inventario")
    print("6. Salir")

# Crear inventario
inventario = Inventario()

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Añadir producto
        try:
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        except ValueError:
            print(" Datos inválidos.")

    elif opcion == "2":
        # Eliminar producto
        id_producto = input("ID del producto a eliminar: ")
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
        # Actualizar producto
        id_producto = input("ID del producto: ")
        try:
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            inventario.actualizar_producto(
                id_producto,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )
        except ValueError:
            print(" Error en los datos.")

    elif opcion == "4":
        # 🔍 Buscar por ID
        id_producto = input("Ingrese el ID: ")
        producto = inventario.buscar_por_id(id_producto)
        if producto:
            print(producto)
        else:
            print(" Producto no encontrado.")

    elif opcion == "5":
        # Listar inventario
        inventario.listar_productos()

    elif opcion == "6":
        print(" Saliendo del sistema...")
        break

    else:
        print(" Opción inválida.")

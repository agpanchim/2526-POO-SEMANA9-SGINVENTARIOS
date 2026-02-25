# 📦 Sistema Avanzado de Gestión de Inventario
# Descripción del programa

Este sistema es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO), que permite gestionar el inventario de una tienda.
El programa permite:
- Añadir productos
- Eliminar productos
- Actualizar productos
- Buscar productos por ID
- Buscar productos por nombre
- Mostrar todos los productos

Toda la información se guarda automáticamente en un archivo, lo que permite mantener los datos incluso después de cerrar el programa.

## Funcionamiento del programa
El programa funciona mediante un menú interactivo en consola.
Cuando el usuario ejecuta el archivo `main.py`, el sistema:
1. Carga automáticamente los productos desde el archivo `inventario.txt`
2. Muestra un menú con opciones
3. El usuario selecciona una opción
4. El sistema ejecuta la operación correspondiente
5. Los cambios se guardan automáticamente en el archivo
Esto permite mantener un inventario persistente.

# Estructura del sistema

El sistema está dividido en tres partes principales:

### 1. Clase Producto (`modelos/producto.py`)

Representa un producto individual.
Atributos:
- id → identificador único
- nombre → nombre del producto
- cantidad → cantidad disponible
- precio → precio del producto

Métodos:
- get_id()
- get_nombre()
- get_cantidad()
- get_precio()
- set_cantidad()
- set_precio()

Esta clase permite crear y modificar productos.

### 2. Clase Inventario (`servicios/inventario.py`)
Gestiona todos los productos del inventario.
Utiliza un diccionario para almacenar los productos:

```python
self.productos = {}
Donde:
clave = ID del producto
valor = objeto Producto
Esto permite búsquedas rápidas.
Funciones principales:
agregar_producto()
eliminar_producto()
actualizar_producto()
buscar_por_id()
buscar_por_nombre()
listar_productos()
guardar_en_archivo()
cargar_desde_archivo()

3. Archivo principal (main.py)
Controla la interacción con el usuario mediante un menú interactivo.
Permite al usuario seleccionar opciones y ejecutar operaciones sobre el inventario.

Se utiliza un diccionario:
self.productos = {}
Ventajas:
Búsqueda rápida
Evita IDs duplicados
Mejor organización

También se usa una lista para resultados de búsqueda por nombre.
Almacenamiento en archivos
El sistema utiliza el archivo:
inventario.txt
Formato:
ID,nombre,cantidad,precio

El sistema:
Guarda automáticamente los productos
Carga automáticamente al iniciar

Interfaz interactiva
El sistema incluye un menú interactivo con emojis para mejorar la experiencia del usuario.
El usuario puede gestionar el inventario fácilmente desde la consola.


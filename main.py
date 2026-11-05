
from fastapi import FastAPI

# Crear la aplicacion FastAPI
app = FastAPI()


# Paso 3: Primer endpoint
@app.get("/")
def inicio():
    return {
        "mensaje": "Mi primera API con FastAPI"
    }


# Paso 6: Parametros de ruta (Path Parameters)
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    return {
        "producto_id": producto_id,
        "mensaje": "Producto solicitado"
    }


# Paso 7: Parametros de consulta (Query Parameters)
@app.get("/buscar")
def buscar_productos(nombre: str = "", precio_max: float = 0):
    return {
        "buscando": nombre,
        "precio_maximo": precio_max
    }


# Ejercicio 1: Consultar categoria por ID
@app.get("/categorias/{categoria_id}")
def obtener_categoria(categoria_id: int):
    return {
        "categoria_id": categoria_id,
        "mensaje": "Categoria solicitada"
    }


# Ejercicio 2: Saludo personalizado
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {
        "mensaje": f"Hola, {nombre}"
    }


# Ejercicio 3: Filtrar por categoria y disponibilidad
@app.get("/filtrar")
def filtrar_productos(categoria: str, disponible: bool):
    return {
        "categoria": categoria,
        "disponible": disponible
    }

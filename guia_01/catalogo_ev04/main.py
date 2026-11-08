
from fastapi import FastAPI, HTTPException

# Crear la aplicacion FastAPI
app = FastAPI(
    title="Mini-API de Catalogo",
    description="API REST para consultar productos de una tienda.",
    version="1.0.0"
)


# Base de datos temporal en memoria
productos = [
    {
        "id": 1,
        "nombre": "Teclado mecanico",
        "precio": 120000,
        "categoria": "Perifericos"
    },
    {
        "id": 2,
        "nombre": "Mouse gamer",
        "precio": 85000,
        "categoria": "Perifericos"
    },
    {
        "id": 3,
        "nombre": "Monitor 24",
        "precio": 650000,
        "categoria": "Pantallas"
    }
]


# Endpoint 1: Mensaje de bienvenida
@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a la Mini-API de Catalogo"
    }


# Endpoint 2: Listar todos los productos
@app.get("/productos")
def listar_productos():
    return productos


# Endpoint 3: Consultar producto por ID
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


# Endpoint 4: Listar categorias
@app.get("/categorias")
def listar_categorias():
    categorias = sorted({
        producto["categoria"]
        for producto in productos
    })
    return categorias


# Endpoint 5: Buscar productos por nombre
@app.get("/buscar")
def buscar_productos(nombre: str = ""):
    resultados = [
        producto
        for producto in productos
        if nombre.lower() in producto["nombre"].lower()
    ]
    return resultados

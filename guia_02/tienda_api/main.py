from fastapi import FastAPI
from guia_02.tienda_api.routers import productos, categorias

app = FastAPI(title="API de la Tienda", version="2.0.0")

app.include_router(productos.router)
app.include_router(categorias.router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "API de la Tienda funcionando. Visita /docs"}

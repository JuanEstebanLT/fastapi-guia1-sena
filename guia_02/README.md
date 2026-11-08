# Guía 2 — CRUD de tienda con FastAPI

**SENA · ADSO · Instructor: Mateo Arroyave · Duración de la guía: 12 horas**

Continuación de la Guía 1: la API pasa de consultas GET a operaciones CRUD y se organiza por módulos con `APIRouter`. La validación de cuerpos JSON se realiza mediante modelos `Pydantic` que heredan de `BaseModel`.

## Evidencias de la guía

| Evidencia | Requisito | Estado |
| --- | --- | --- |
| GA2-AA1-EV01 | Cuatro reflexiones sobre modularidad, validación, operaciones y CRUD | Pendiente de documento académico |
| GA2-AA1-EV02 | Tabla CRUD/HTTP/códigos y mapa conceptual | Pendiente de documento académico |
| GA2-AA2-EV03 | CRUD de productos con modelos, `APIRouter`, respuestas 201/404/422 y pruebas | Código implementado, capturas de `/docs` pendientes |
| GA2-AA3-EV04 | CRUD de categorías completo e integrado en `main.py` | Código implementado, capturas de `/docs` pendientes |

## Arquitectura

```text
guia_02/
├── tienda_api/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│       ├── __init__.py
│       ├── productos.py
│       └── categorias.py
├── evidencias/
│   └── README.md
└── README.md
```

Se usa el nombre `tienda_api` con guion bajo para que Python pueda importar el paquete desde el directorio raíz. Cumple la misma finalidad de la carpeta `tienda-api` propuesta por la guía.

- `main.py` crea la aplicación y registra los dos routers; también expone `GET /`.
- `productos.py` contiene el modelo `ProductoEntrada`, los datos y cinco endpoints.
- `categorias.py` contiene el modelo `CategoriaEntrada`, los datos y cinco endpoints.
- `__init__.py` identifica las carpetas como paquetes importables.

## Ejecución

Desde la **raíz del repositorio**, instalar dependencias y activar entorno virtual (ver [README principal](../README.md)):

```powershell
python -m uvicorn guia_02.tienda_api.main:app --reload
```

Abrir [Swagger UI](http://127.0.0.1:8000/docs) y comprobar las secciones **Productos** y **Categorias**.

## Endpoints de productos

| Operación | Método | Endpoint | Resultado |
| --- | --- | --- | --- |
| Listar | GET | `/productos` | 200 |
| Consultar por ID | GET | `/productos/{producto_id}` | 200 o 404 |
| Crear | POST | `/productos` | 201 |
| Actualizar | PUT | `/productos/{producto_id}` | 200 o 404 |
| Eliminar | DELETE | `/productos/{producto_id}` | 200 o 404 |

Cuerpo JSON de ejemplo para crear o actualizar:

```json
{"nombre":"Audifonos USB", "precio": 120000, "categoria":"Audio"}
```

`ProductoEntrada` recibe `nombre: str`, `precio: float` y `categoria: str`; el `id` lo asigna el servidor. Si falta un campo obligatorio o llega un precio no convertible a número, FastAPI responde `422`.

## Endpoints de categorías

| Operación | Método | Endpoint | Resultado |
| --- | --- | --- | --- |
| Listar | GET | `/categorias` | 200 |
| Consultar por ID | GET | `/categorias/{categoria_id}` | 200 o 404 |
| Crear | POST | `/categorias` | 201 |
| Actualizar | PUT | `/categorias/{categoria_id}` | 200 o 404 |
| Eliminar | DELETE | `/categorias/{categoria_id}` | 200 o 404 |

Cuerpo JSON de ejemplo para crear o actualizar:

```json
{"nombre":"Accesorios"}
```

`CategoriaEntrada` recibe `nombre: str`; el servidor genera el identificador. Un ID inexistente produce `404` y un cuerpo inválido produce `422`.

## Ejercicios de apropiación

Las actividades prácticas del instructor requieren:

1. Crear **dos productos** con `POST /productos` y listarlos con GET.
2. Actualizar un precio con `PUT` y volver a consultar el producto.
3. Eliminar un producto con `DELETE` y comprobar que no está en la lista.
4. Provocar y capturar errores `404` y `422` para productos.
5. Probar en Swagger UI las **cinco rutas de categorías**, incluidos errores `404` y `422`.

Los datos son **temporales en memoria**: reiniciar el servidor restaura los productos y categorías iniciales. No hay base de datos ni relación de integridad referencial entre ambos conjuntos en esta guía.

## Pruebas automatizadas

Desde la raíz:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest tests/test_guia_02.py -q
```

La suite verifica CRUD de productos y categorías, documentación OpenAPI, códigos `201`, `404` y `422`. Las pruebas automatizadas no sustituyen las capturas exigidas por la guía.

## Entrega académica pendiente

La carpeta [evidencias](evidencias/README.md) indica qué capturas y documentos faltan antes de entregar. También deberán incorporarse EV01 y EV02 en el informe grupal. La grabación de sustentación depende de las instrucciones de exposición del instructor.

**Integrantes:** Juan Esteban Lezcano Tejada, Mariana Suárez y Emanuel Villa.

[Regresar al índice de todas las guías](../README.md).

# Guía 2 — CRUD, validación Pydantic y organización modular

**SENA · ADSO · Instructor: Mateo Arroyave · Duración: 12 horas**  
**Integrantes:** Juan Esteban Lezcano Tejada, Mariana Suárez y Emanuel Villa.

Esta guía amplía la Mini-API de la Guía 1 para administrar **productos y categorías** con operaciones CRUD, validar datos recibidos en JSON mediante **Pydantic (BaseModel)** y separar recursos con **APIRouter**.

## Evidencias solicitadas

| Evidencia | Descripción | Estado de preparación |
| --- | --- | --- |
| GA2-AA1-EV01 | Reflexión inicial: cuatro respuestas | Desarrollada en el informe final |
| GA2-AA1-EV02 | Cuadro CRUD y mapa conceptual de seis términos | Desarrollados en el informe final |
| GA2-AA2-EV03 | CRUD de productos y capturas HTTP 201, 200, 404 y 422 | Código publicado y capturas incluidas en el informe |
| GA2-AA3-EV04 | CRUD de categorías, validación y pruebas en Swagger UI | Código publicado y capturas incluidas en el informe |

**Informe final (versión 1.0):** [Consultar PDF de las cuatro evidencias](evidencias/GA2_FastAPI_Informe_Final_APA7_v1.0.pdf). El enlace estará disponible cuando se incorporen las copias del informe al repositorio. [Carpeta personal](evidencias/README.md) · [Índice general](../evidencias/guia_02/README.md).

## Estructura del módulo

~~~text
guia_02/
├── __init__.py
├── README.md
├── tienda_api/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│       ├── __init__.py
│       ├── productos.py
│       └── categorias.py
└── evidencias/
    ├── README.md
    └── GA2_FastAPI_Informe_Final_APA7_v1.0.pdf
~~~

- [main.py](tienda_api/main.py): inicia FastAPI, registra los routers y publica la ruta de inicio.
- [productos.py](tienda_api/routers/productos.py): contiene el modelo ProductoEntrada, una lista de productos y cinco endpoints.
- [categorias.py](tienda_api/routers/categorias.py): contiene CategoriaEntrada, una lista de categorías y cinco endpoints.
- [Pruebas automatizadas](../tests/test_guia_02.py): utilizan FastAPI TestClient y pytest.

Se utiliza el nombre importable **tienda_api** en lugar de la carpeta **tienda-api** del ejemplo de la guía. El comportamiento exigido es equivalente y el comando de ejecución se adapta a esta estructura.

## Instalación y ejecución

Desde la raíz del repositorio, activar el entorno virtual e instalar dependencias según el [README principal](../README.md). Luego iniciar la aplicación:

~~~powershell
python -m uvicorn guia_02.tienda_api.main:app --reload
~~~

Visitar [Swagger UI](http://127.0.0.1:8000/docs). Allí se muestran las secciones **Productos**, **Categorias** e **Inicio**.

## Endpoints disponibles

| Recurso | Método | Ruta | Respuesta habitual |
| --- | --- | --- | --- |
| Inicio | GET | / | 200 |
| Productos | GET | /productos | 200 |
| Productos | GET | /productos/{producto_id} | 200 o 404 |
| Productos | POST | /productos | 201 o 422 |
| Productos | PUT | /productos/{producto_id} | 200, 404 o 422 |
| Productos | DELETE | /productos/{producto_id} | 200 o 404 |
| Categorías | GET | /categorias | 200 |
| Categorías | GET | /categorias/{categoria_id} | 200 o 404 |
| Categorías | POST | /categorias | 201 o 422 |
| Categorías | PUT | /categorias/{categoria_id} | 200, 404 o 422 |
| Categorías | DELETE | /categorias/{categoria_id} | 200 o 404 |

### Modelo de producto

ProductoEntrada hereda de BaseModel y requiere **nombre: str**, **precio: float** y **categoria: str**. El servidor asigna el identificador.

~~~json
{
  "nombre": "Webcam Full HD",
  "precio": 185000,
  "categoria": "Perifericos"
}
~~~

### Modelo de categoría

CategoriaEntrada hereda de BaseModel y exige **nombre: str**. El servidor genera el identificador.

~~~json
{
  "nombre": "Accesorios Gamer"
}
~~~

En ambos recursos, una entidad inexistente genera **404** mediante HTTPException. Un cuerpo JSON con campos obligatorios ausentes o datos incompatibles produce la validación automática **422**. Los registros se almacenan en listas de Python y se restablecen al reiniciar el servidor: esta guía **no implementa base de datos**.

## Procedimiento de comprobación en Swagger UI

1. Registrar dos productos con POST /productos y consultarlos con GET /productos.
2. Actualizar el precio de un producto con PUT y confirmarlo mediante GET /productos/{id}.
3. Eliminar un producto con DELETE y verificar que ya no aparece en el listado.
4. Probar un identificador inexistente para obtener 404 y datos inválidos para obtener 422.
5. Repetir la secuencia de consulta, creación, actualización, eliminación y errores con las categorías.

El informe académico contiene las capturas documentadas. Estas capturas se generaron durante la práctica; no se sustituyen por resultados artificiales.

## Pruebas automatizadas

~~~powershell
python -m pip install -r requirements-dev.txt
python -m pytest tests/test_guia_02.py -q
~~~

Para ejecutar todas las pruebas:

~~~powershell
python -m pytest tests -q
~~~

Las pruebas cubren rutas, esquema OpenAPI, operaciones CRUD y errores 404/422. Constituyen una comprobación técnica complementaria, no una sustitución de las evidencias solicitadas desde /docs.

## Entregables y sustentación

- **Informe:** [GA2_FastAPI_Informe_Final_APA7_v1.0.pdf](evidencias/GA2_FastAPI_Informe_Final_APA7_v1.0.pdf). Contiene las cuatro evidencias, tabla y mapa conceptual, pruebas manuales y explicaciones técnicas. Disponible tras la publicación del archivo.
- **Ubicación personal:** [guia_02/evidencias](evidencias/README.md).
- **Ubicación central:** [evidencias/guia_02](../evidencias/guia_02/README.md).
- **Video explicativo grupal:** pendiente de grabación; se añadirá un enlace cuando exista. La guía escrita no establece un video obligatorio.

[Volver al índice general](../README.md).

# Guía 1 de FastAPI — SENA

Proyecto académico desarrollado para la **Guía 1 de FastAPI** del programa Análisis y Desarrollo de Software (ADSO). El repositorio reúne el laboratorio introductorio de FastAPI (GA1-AA2-EV03) y una Mini-API de Catálogo (GA1-AA3-EV04).

## Información académica

- **Autor:** Juan Esteban Lezcano Tejada
- **Institución:** Servicio Nacional de Aprendizaje (SENA)
- **Programa:** Análisis y Desarrollo de Software (ADSO)
- **Instructor:** Mateo Arroyave

## Objetivo general

Aplicar los fundamentos de construcción de API REST con FastAPI mediante rutas, parámetros de ruta, parámetros de consulta, respuestas JSON, códigos de estado y documentación interactiva generada automáticamente.

## Tecnologías utilizadas

- Python 3.15.0
- FastAPI
- Uvicorn
- Swagger UI y ReDoc
- Git y GitHub

## Estructura del repositorio

```text
fastapi-guia1-sena/
├── catalogo_ev04/
│   └── main.py             # Mini-API de Catálogo (GA1-AA3-EV04)
├── laboratorio_ev03/
│   └── main.py             # Laboratorio de endpoints (GA1-AA2-EV03)
├── .gitignore
├── main.py                 # Archivo original del laboratorio
└── README.md
```

El entorno virtual y los directorios `__pycache__` se mantienen únicamente en el equipo local y están excluidos del control de versiones.

## Requisitos previos

- Python 3.15.0 o una versión compatible instalada.
- Git, si se desea clonar el repositorio.
- Una terminal de PowerShell o Símbolo del sistema en Windows.

Compruebe la instalación de Python:

```powershell
python --version
```

## Instalación en Windows

Clone el repositorio y entre en su directorio:

```powershell
git clone https://github.com/JuanEstebanLT/fastapi-guia1-sena.git
cd fastapi-guia1-sena
```

Cree el entorno virtual:

```powershell
python -m venv venv
```

Active el entorno virtual en PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Símbolo del sistema (`cmd`), utilice:

```bat
venv\Scripts\activate.bat
```

Instale FastAPI y Uvicorn:

```powershell
python -m pip install fastapi uvicorn
```

## Ejecución

Ejecute cada aplicación desde la raíz del repositorio.

### Evidencia GA1-AA2-EV03

```powershell
python -m uvicorn laboratorio_ev03.main:app --reload
```

### Evidencia GA1-AA3-EV04

```powershell
python -m uvicorn catalogo_ev04.main:app --reload
```

Ambas aplicaciones usan de forma predeterminada `http://127.0.0.1:8000`. Deben ejecutarse **por separado** para evitar conflictos de puerto. Si una está activa, deténgala con `Ctrl+C` antes de iniciar la otra.

## Endpoints de GA1-AA2-EV03

| Método | Ruta | Parámetros | Descripción |
| --- | --- | --- | --- |
| `GET` | `/` | Ninguno | Devuelve el mensaje inicial. |
| `GET` | `/productos/{producto_id}` | `producto_id` (entero, ruta) | Consulta un producto por identificador. |
| `GET` | `/buscar` | `nombre` (texto, opcional), `precio_max` (decimal, opcional) | Devuelve los criterios de búsqueda recibidos. |
| `GET` | `/categorias/{categoria_id}` | `categoria_id` (entero, ruta) | Consulta una categoría por identificador. |
| `GET` | `/saludo/{nombre}` | `nombre` (texto, ruta) | Genera un saludo personalizado. |
| `GET` | `/filtrar` | `categoria` (texto), `disponible` (booleano) | Devuelve los filtros de categoría y disponibilidad. |

Ejemplo de petición:

```http
GET http://127.0.0.1:8000/productos/15
```

Respuesta:

```json
{
  "producto_id": 15,
  "mensaje": "Producto solicitado"
}
```

Ejemplo con parámetros de consulta:

```http
GET http://127.0.0.1:8000/filtrar?categoria=Perifericos&disponible=true
```

Respuesta:

```json
{
  "categoria": "Perifericos",
  "disponible": true
}
```

## Endpoints de GA1-AA3-EV04

| Método | Ruta | Parámetros | Descripción |
| --- | --- | --- | --- |
| `GET` | `/` | Ninguno | Devuelve el mensaje de bienvenida. |
| `GET` | `/productos` | Ninguno | Lista todos los productos del catálogo en memoria. |
| `GET` | `/productos/{producto_id}` | `producto_id` (entero, ruta) | Devuelve el producto solicitado o un error `404`. |
| `GET` | `/categorias` | Ninguno | Lista las categorías disponibles en orden alfabético. |
| `GET` | `/buscar` | `nombre` (texto, opcional) | Busca coincidencias parciales sin distinguir mayúsculas. |

Ejemplo de petición exitosa:

```http
GET http://127.0.0.1:8000/productos/2
```

Respuesta:

```json
{
  "id": 2,
  "nombre": "Mouse gamer",
  "precio": 85000,
  "categoria": "Perifericos"
}
```

Ejemplo de recurso inexistente:

```http
GET http://127.0.0.1:8000/productos/99
```

Respuesta con estado `404 Not Found`:

```json
{
  "detail": "Producto no encontrado"
}
```

Ejemplo de búsqueda:

```http
GET http://127.0.0.1:8000/buscar?nombre=mouse
```

Respuesta:

```json
[
  {
    "id": 2,
    "nombre": "Mouse gamer",
    "precio": 85000,
    "categoria": "Perifericos"
  }
]
```

## Documentación interactiva

Con cualquiera de las aplicaciones en ejecución, FastAPI genera automáticamente:

- **Swagger UI:** <http://127.0.0.1:8000/docs>
- **ReDoc:** <http://127.0.0.1:8000/redoc>
- **Esquema OpenAPI:** <http://127.0.0.1:8000/openapi.json>

Swagger UI permite consultar la definición de cada endpoint, introducir parámetros y enviar peticiones desde el navegador.

## Resultados de las pruebas

Las dos evidencias fueron verificadas manualmente mediante Swagger UI durante su desarrollo. Antes de la publicación se comprobaron la estructura del proyecto, la sintaxis de los archivos `main.py`, la importación de las aplicaciones FastAPI y la cantidad de rutas propias de cada evidencia: seis en EV03 y cinco en EV04. Las rutas automáticas de documentación de FastAPI no se incluyen en esos conteos.

## Referencias

- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Primera aplicación con FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Parámetros de ruta](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Parámetros de consulta](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Documentación de Uvicorn](https://www.uvicorn.org/)


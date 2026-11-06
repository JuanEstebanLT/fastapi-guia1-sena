<div align="center">

# Guía 1 · Desarrollo de API REST con FastAPI

### Fundamentos, laboratorio de endpoints y Mini-API de Catálogo

[![Python](https://img.shields.io/badge/Python-3.15-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4051B5?style=flat-square)](https://www.uvicorn.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repositorio-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JuanEstebanLT/fastapi-guia1-sena)

**Servicio Nacional de Aprendizaje (SENA)** · **Análisis y Desarrollo de Software (ADSO)**

**Instructor:** Mateo Arroyave

[Informe académico (PDF)](evidencias/Guia_FastAPI_Final.pdf) · [Video de sustentación](https://youtu.be/39X68AKH1gg) · [Laboratorio EV03](laboratorio_ev03/main.py) · [Catálogo EV04](catalogo_ev04/main.py)

</div>

---

## Descripción

Repositorio académico de la **Guía 1 de FastAPI**, desarrollado para comprender el funcionamiento de las interfaces de programación de aplicaciones (API), las solicitudes HTTP, los parámetros de ruta y consulta, las respuestas JSON y los códigos de estado.

La entrega reúne dos componentes:

- **Fundamentación (EV01 y EV02):** reflexión inicial, comparación de Flask y FastAPI y mapa conceptual.
- **Implementación (EV03 y EV04):** laboratorio de seis endpoints y Mini-API de Catálogo con cinco endpoints de consulta.

Las dos aplicaciones se ejecutan **localmente y de forma independiente** con Python, FastAPI y Uvicorn. Sus operaciones fueron comprobadas manualmente mediante Swagger UI. El catálogo utiliza una lista en memoria; no requiere base de datos, autenticación ni despliegue en la nube.

> **Estado de entrega:** las cuatro evidencias, el informe y la sustentación audiovisual grupal están publicados.

## Tabla de contenido

- [Objetivo y alcance](#objetivo-y-alcance)
- [Evidencias académicas](#evidencias-académicas)
- [Tecnologías](#tecnologías)
- [Arquitectura](#arquitectura)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Instalación](#instalación)
- [Ejecución de los laboratorios](#ejecución-de-los-laboratorios)
- [API del laboratorio EV03](#api-del-laboratorio-ev03)
- [API del catálogo EV04](#api-del-catálogo-ev04)
- [Pruebas y resultados](#pruebas-y-resultados)
- [Documentación y evidencias](#documentación-y-evidencias)
- [Sustentación en video](#sustentación-en-video)
- [Equipo académico](#equipo-académico)
- [Referencias técnicas](#referencias-técnicas)

## Objetivo y alcance

**Objetivo general:** aplicar los fundamentos de las API REST mediante la creación, ejecución y validación de endpoints con FastAPI.

**Objetivos específicos:**

1. Comprender API, HTTP, JSON, endpoints, métodos y códigos de estado.
2. Comparar los enfoques de Flask y FastAPI en el desarrollo de servicios web.
3. Implementar y probar parámetros de ruta y de consulta con validación automática de tipos.
4. Construir un catálogo de consulta en memoria y controlar el caso de un recurso inexistente.

**Alcance implementado:** solicitudes GET, datos de prueba, respuestas JSON, validación de parámetros, error HTTP 404, documentación automática OpenAPI/Swagger UI y ejecución local.

**Fuera del alcance de esta guía:** persistencia en una base de datos, autenticación, operaciones de escritura (POST/PUT/DELETE), interfaz frontend y despliegue público de las API. Estos componentes no son necesarios para reproducir las prácticas documentadas.

## Evidencias académicas

| Código | Evidencia | Entregable | Estado |
| --- | --- | --- | --- |
| GA1-AA1-EV01 | Reflexión inicial sobre API y arquitectura web | Cuatro preguntas desarrolladas | Completa |
| GA1-AA1-EV02 | Comparación conceptual | Tabla Flask/FastAPI y mapa conceptual | Completa |
| GA1-AA2-EV03 | Laboratorio introductorio | Seis rutas GET, pruebas y código | Completa |
| GA1-AA3-EV04 | Mini-API de Catálogo | Cinco rutas GET, productos en memoria y pruebas | Completa |

El desarrollo, las capturas de pantalla y el análisis de las cuatro evidencias están consolidados en el [informe académico de la Guía 1](evidencias/Guia_FastAPI_Final.pdf).

## Tecnologías

| Tecnología | Función |
| --- | --- |
| **Python 3.15.0** | Lenguaje utilizado en el entorno de desarrollo |
| **FastAPI** | Definición de rutas HTTP, tipado y validación |
| **Uvicorn** | Servidor ASGI para ejecución local |
| **Pydantic** | Soporte de validación de datos integrado con FastAPI |
| **Swagger UI y ReDoc** | Documentación generada desde OpenAPI |
| **Git / GitHub** | Versionado y publicación de entregables |

No se necesita Supabase, PostgreSQL, Docker ni ninguna plataforma externa para ejecutar estas actividades.

## Arquitectura

Las prácticas siguen un flujo cliente–servidor sencillo. FastAPI procesa las solicitudes HTTP y devuelve respuestas JSON.

~~~mermaid
flowchart TD
    C[Cliente: navegador o Swagger UI] -->|Solicitud HTTP GET| U[Uvicorn - servidor ASGI]
    U --> A[Aplicación FastAPI]
    A --> D{Práctica ejecutada}
    D -->|EV03| E[Endpoints de laboratorio]
    D -->|EV04| F[Endpoints de catálogo]
    F --> M[Lista de productos en memoria]
    E --> R[Respuesta JSON y código HTTP]
    M --> R
    R --> C
~~~

**Separación de las aplicaciones:** <code>laboratorio_ev03/main.py</code> y <code>catalogo_ev04/main.py</code> contienen instancias independientes de FastAPI. Aunque algunas rutas tienen nombres iguales, no se ejecutan simultáneamente en el mismo puerto.

## Estructura del repositorio

~~~text
fastapi-guia1-sena/
├── catalogo_ev04/
│   └── main.py                # Mini-API de Catálogo: 5 endpoints
├── evidencias/
│   ├── Guia_FastAPI_Final.pdf # Informe académico: EV01 a EV04
│   └── Guia1 - FastAPI.mp4    # Video original de sustentación
├── laboratorio_ev03/
│   └── main.py                # Laboratorio básico: 6 endpoints
├── main.py                    # Archivo original del laboratorio
├── .gitignore
└── README.md
~~~

El entorno virtual <code>venv/</code> y la caché de Python <code>__pycache__/</code> son locales y están excluidos del control de versiones.

## Instalación

### Requisitos previos

- Python instalado y disponible mediante <code>py</code> o <code>python</code>.
- Git para clonar el repositorio.
- Terminal Windows (CMD o PowerShell).

### 1. Clonar el proyecto

~~~powershell
git clone https://github.com/JuanEstebanLT/fastapi-guia1-sena.git
cd fastapi-guia1-sena
~~~

### 2. Crear el entorno virtual

En Windows, utilizando el lanzador de Python:

~~~powershell
py -m venv venv
~~~

### 3. Activar el entorno

**CMD:**

~~~bat
venv\Scripts\activate.bat
~~~

**PowerShell:**

~~~powershell
.\venv\Scripts\Activate.ps1
~~~

Si PowerShell restringe la ejecución de scripts, puede activarse el entorno con la terminal CMD o ejecutar el intérprete de <code>venv</code> directamente.

### 4. Instalar dependencias

~~~powershell
python -m pip install fastapi uvicorn
~~~

Se utilizan las dependencias esenciales, sin el extra opcional <code>uvicorn[standard]</code>, porque en el entorno de Python 3.15 utilizado para la práctica este extra presentó un problema de compilación con PyYAML.

## Ejecución de los laboratorios

Ejecutar los comandos **desde la raíz del repositorio**, con el entorno virtual activado.

### EV03 — Laboratorio introductorio

~~~powershell
python -m uvicorn laboratorio_ev03.main:app --reload
~~~

### EV04 — Mini-API de Catálogo

~~~powershell
python -m uvicorn catalogo_ev04.main:app --reload
~~~

Por defecto, la aplicación activa queda disponible en <http://127.0.0.1:8000>. Para iniciar la otra práctica, detener primero el servidor con **Ctrl + C**. No deben iniciarse ambas en el puerto 8000 al mismo tiempo.

**Documentación local (con el servidor en ejecución):**

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- Esquema OpenAPI: <http://127.0.0.1:8000/openapi.json>

Estos enlaces son direcciones locales, no un despliegue público.

## API del laboratorio EV03

Archivo: [<code>laboratorio_ev03/main.py</code>](laboratorio_ev03/main.py)

| Método | Endpoint | Parámetros | Respuesta |
| --- | --- | --- | --- |
| GET | <code>/</code> | Ninguno | Mensaje inicial |
| GET | <code>/productos/{producto_id}</code> | <code>producto_id: int</code> | ID y mensaje |
| GET | <code>/buscar</code> | <code>nombre: str</code>, <code>precio_max: float</code> (opcionales) | Parámetros recibidos |
| GET | <code>/categorias/{categoria_id}</code> | <code>categoria_id: int</code> | ID de categoría y mensaje |
| GET | <code>/saludo/{nombre}</code> | <code>nombre: str</code> | Saludo personalizado |
| GET | <code>/filtrar</code> | <code>categoria: str</code>, <code>disponible: bool</code> | Filtros recibidos |

**Ejemplo: parámetro de ruta válido**

~~~http
GET /productos/5
~~~

~~~json
{
  "producto_id": 5,
  "mensaje": "Producto solicitado"
}
~~~

Si se envía un identificador no numérico, por ejemplo <code>GET /productos/abc</code>, FastAPI devuelve **HTTP 422** debido a la validación automática del tipo entero.

**Ejemplo: parámetros de consulta**

~~~http
GET /buscar?nombre=teclado&precio_max=150000
~~~

~~~json
{
  "buscando": "teclado",
  "precio_maximo": 150000
}
~~~

> En EV03, <code>/buscar</code> devuelve los valores recibidos; **no consulta ni filtra un catálogo**. El filtrado de productos se implementa en EV04.

## API del catálogo EV04

Archivo: [<code>catalogo_ev04/main.py</code>](catalogo_ev04/main.py)

| Método | Endpoint | Descripción | Respuesta esperada |
| --- | --- | --- | --- |
| GET | <code>/</code> | Mensaje de bienvenida | 200 |
| GET | <code>/productos</code> | Lista los productos | 200 |
| GET | <code>/productos/{producto_id}</code> | Busca por identificador | 200 / 404 |
| GET | <code>/categorias</code> | Obtiene categorías sin duplicados | 200 |
| GET | <code>/buscar?nombre=mouse</code> | Filtra por coincidencia parcial | 200 |

### Datos de prueba en memoria

| ID | Producto | Precio (COP) | Categoría |
| --- | --- | ---: | --- |
| 1 | Teclado mecanico | 120.000 | Perifericos |
| 2 | Mouse gamer | 85.000 | Perifericos |
| 3 | Monitor 24 | 650.000 | Pantallas |

Los datos están definidos en una lista de diccionarios Python y se reinician cuando se modifica o reinicia el proceso.

### Ejemplos de respuestas

**Producto existente**

~~~http
GET /productos/2
~~~

~~~json
{
  "id": 2,
  "nombre": "Mouse gamer",
  "precio": 85000,
  "categoria": "Perifericos"
}
~~~

**Producto inexistente**

~~~http
GET /productos/99
~~~

~~~json
{
  "detail": "Producto no encontrado"
}
~~~

La segunda solicitud devuelve **HTTP 404 Not Found** de forma controlada.

**Búsqueda por nombre**

~~~http
GET /buscar?nombre=mouse
~~~

~~~json
[
  {
    "id": 2,
    "nombre": "Mouse gamer",
    "precio": 85000,
    "categoria": "Perifericos"
  }
]
~~~

La búsqueda no distingue mayúsculas de minúsculas y admite coincidencias parciales.

## Pruebas y resultados

Las pruebas fueron ejecutadas manualmente en el entorno local, mediante el botón **Try it out → Execute** de Swagger UI. El informe conserva capturas donde se observan la petición, el código HTTP y la respuesta JSON.

| Componente | Pruebas documentadas | Resultado |
| --- | --- | --- |
| EV03 | Seis endpoints GET con entradas válidas | 200 OK |
| EV03 | Identificador no numérico (<code>/productos/abc</code>) | 422 |
| EV04 | Cinco endpoints GET con datos válidos | 200 OK |
| EV04 | Identificador inexistente (<code>/productos/99</code>) | 404 |

Estas son **pruebas manuales** respaldadas por capturas. El proyecto no incorpora por ahora una suite automatizada ni un flujo CI/CD.

Las rutas <code>/docs</code>, <code>/redoc</code> y <code>/openapi.json</code> son proporcionadas automáticamente por FastAPI; no se cuentan entre los endpoints de las evidencias.

## Documentación y evidencias

El [**informe final en PDF**](evidencias/Guia_FastAPI_Final.pdf) contiene:

- **EV01:** reflexión inicial sobre API, aplicaciones cliente–servidor, frontend y backend.
- **EV02:** comparación entre Flask y FastAPI y mapa conceptual de API, HTTP, métodos, endpoints, JSON y códigos de estado.
- **EV03:** explicación del laboratorio, código fuente, capturas de los endpoints y validación HTTP 422.
- **EV04:** diseño del catálogo, código, resultados de las cinco rutas y prueba HTTP 404.
- Portada grupal, índice, introducción, objetivos, conclusiones, referencias y control de versiones.

El PDF es el documento de revisión académica; los archivos Python de este repositorio son el código ejecutable de las evidencias prácticas.

**Archivo audiovisual de la entrega:** [Guia1 - FastAPI.mp4](evidencias/Guia1%20-%20FastAPI.mp4).

## Sustentación en video

**Estado: grabada y publicada.**

**[Ver sustentación grupal de la Guía 1 de FastAPI en YouTube](https://youtu.be/39X68AKH1gg)** · **[Descargar MP4 desde el repositorio](evidencias/Guia1%20-%20FastAPI.mp4)**

[![Ver video de sustentación](https://img.youtube.com/vi/39X68AKH1gg/hqdefault.jpg)](https://youtu.be/39X68AKH1gg)

La exposición corresponde al equipo integrado por **Juan Esteban Lezcano Tejada, Mariana Suárez y Emanuel Villa**. En el video se explican los conceptos fundamentales y se presentan las evidencias prácticas EV03 y EV04.

El video está publicado en YouTube y también se conserva una copia original en la carpeta [`evidencias/`](evidencias/), junto con el informe académico. El código fuente permanece disponible en las carpetas de cada laboratorio.

## Equipo académico

| Integrante | Participación |
| --- | --- |
| **Juan Esteban Lezcano Tejada** | Integrante del equipo |
| **Mariana Suárez** | Integrante del equipo |
| **Emanuel Villa** | Integrante del equipo |

**Instructor:** Mateo Arroyave  
**Institución:** Servicio Nacional de Aprendizaje (SENA)  
**Programa:** Análisis y Desarrollo de Software (ADSO)

## Referencias técnicas

- [FastAPI — Documentación oficial](https://fastapi.tiangolo.com/)
- [FastAPI — Primeros pasos](https://fastapi.tiangolo.com/es/tutorial/first-steps/)
- [FastAPI — Parámetros de ruta](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI — Parámetros de consulta](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Uvicorn — Documentación oficial](https://www.uvicorn.org/)
- [Flask — Documentación oficial](https://flask.palletsprojects.com/en/stable/)

---

<div align="center">

**Guía 1 de FastAPI · SENA · ADSO**

Repositorio de aprendizaje con código reproducible, documentación y evidencias de ejecución.

</div>

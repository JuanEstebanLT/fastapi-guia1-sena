<div align="center">

# FastAPI · SENA

**Desarrollo de API REST con Python | Guías de aprendizaje**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pytest](https://img.shields.io/badge/Pruebas-pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![CI](https://github.com/JuanEstebanLT/fastapi-sena/actions/workflows/pruebas-fastapi.yml/badge.svg)](https://github.com/JuanEstebanLT/fastapi-sena/actions/workflows/pruebas-fastapi.yml)

**Servicio Nacional de Aprendizaje (SENA)**  
**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Instructor:** Mateo Arroyave

**Integrantes:** Juan Esteban Lezcano Tejada · Mariana Suárez · Emanuel Villa

[Guías](#guías-de-aprendizaje) · [Arquitectura](#arquitectura-y-estructura) · [Instalación](#instalación) · [Pruebas](#pruebas-automatizadas) · [Evidencias](#organización-de-evidencias)

</div>

---

## Presentación

Repositorio académico que reúne el desarrollo progresivo de aplicaciones REST con **FastAPI**, conforme a las guías del curso. Cada guía se implementa en un módulo independiente, con sus propias instrucciones, ejemplos de ejecución y evidencias. Esta estructura facilita la revisión del instructor y permite continuar el proyecto sin alterar las actividades ya entregadas.

La **Guía 1** introduce las solicitudes HTTP de consulta, parámetros y documentación interactiva. La **Guía 2** amplía el proyecto mediante operaciones CRUD, validación de datos con **Pydantic** y separación de rutas mediante **APIRouter**. Las próximas guías se incorporarán a medida que se asignen.

> **Alcance:** las aplicaciones son prácticas locales independientes. Los datos CRUD de la Guía 2 se almacenan temporalmente en memoria; no hay persistencia en base de datos ni despliegue público.

## Guías de aprendizaje

| Guía | Contenido | Acceso al código y documentación | Evidencias | Sustentación |
| :--- | :--- | :--- | :--- | :--- |
| **01 · Fundamentos** | Endpoints GET, parámetros de ruta y consulta, Swagger UI | [README](guia_01/README.md) · [Laboratorio](guia_01/laboratorio_ev03/main.py) · [Catálogo](guia_01/catalogo_ev04/main.py) | [Informe PDF](evidencias/guia_01/Guia_01_Informe_Final_FastAPI.pdf) | [YouTube](https://youtu.be/39X68AKH1gg) · [MP4](evidencias/guia_01/Guia_01_Sustentacion_FastAPI.mp4) |
| **02 · CRUD modular** | POST, GET, PUT, DELETE; BaseModel, Pydantic y APIRouter | [README](guia_02/README.md) · [Productos](guia_02/tienda_api/routers/productos.py) · [Categorías](guia_02/tienda_api/routers/categorias.py) | [Evidencias de la Guía 2](evidencias/guia_02/README.md) | **Pendiente de grabación** |
| **03 · Próxima guía** | Por definir según el material del instructor | Aún no iniciada | [Espacio de evidencias](evidencias/guia_03/README.md) | No disponible |

El documento académico final de la **Guía 2** está preparado en formato Word, pero **todavía no está publicado en GitHub**. Por esa razón no se presenta un enlace a un archivo inexistente.

**[Consultar el índice central de evidencias](evidencias/README.md)**

## Arquitectura y estructura

Cada guía define su propia aplicación FastAPI. Se utilizan paquetes de Python para aislar el contenido de las prácticas y, en la segunda guía, routers para separar los recursos del catálogo.

~~~text
fastapi-sena/
├── README.md
├── requirements.txt                  # FastAPI y Uvicorn
├── requirements-dev.txt              # Dependencias de pruebas
├── .gitignore
├── guia_01/
│   ├── README.md
│   ├── main.py
│   ├── laboratorio_ev03/
│   │   └── main.py
│   ├── catalogo_ev04/
│   │   └── main.py
│   └── evidencias/
│       ├── README.md
│       ├── Guia_FastAPI_Final.pdf
│       └── Guia1 - FastAPI.mp4
├── guia_02/
│   ├── README.md
│   ├── tienda_api/
│   │   ├── main.py
│   │   └── routers/
│   │       ├── productos.py
│   │       └── categorias.py
│   └── evidencias/
│       └── README.md
├── evidencias/                       # Índice central, sin archivos sueltos
│   ├── README.md
│   ├── guia_01/
│   │   ├── README.md
│   │   ├── Guia_01_Informe_Final_FastAPI.pdf
│   │   └── Guia_01_Sustentacion_FastAPI.mp4
│   ├── guia_02/
│   │   └── README.md
│   └── guia_03/
│       └── README.md
├── tests/
│   ├── test_guia_01.py
│   └── test_guia_02.py
└── .github/workflows/
    └── pruebas-fastapi.yml
~~~

**Nota:** el árbol destaca los archivos principales. Las carpetas de paquetes Python también contienen archivos `__init__.py`.

### Archivos principales por guía

| Archivo | Función |
| :--- | :--- |
| [`guia_01/main.py`](guia_01/main.py) | Punto de partida de la primera guía |
| [`guia_01/laboratorio_ev03/main.py`](guia_01/laboratorio_ev03/main.py) | Laboratorio de seis endpoints GET |
| [`guia_01/catalogo_ev04/main.py`](guia_01/catalogo_ev04/main.py) | Catálogo de cinco endpoints GET |
| [`guia_02/tienda_api/main.py`](guia_02/tienda_api/main.py) | Aplicación principal; registra los routers |
| [`guia_02/tienda_api/routers/productos.py`](guia_02/tienda_api/routers/productos.py) | CRUD de productos y validación de entrada |
| [`guia_02/tienda_api/routers/categorias.py`](guia_02/tienda_api/routers/categorias.py) | CRUD de categorías y validación de entrada |
| [`tests/test_guia_01.py`](tests/test_guia_01.py) | Pruebas automatizadas de la Guía 1 |
| [`tests/test_guia_02.py`](tests/test_guia_02.py) | Pruebas automatizadas de la Guía 2 |

## Instalación

**Requisitos:** Python 3.12 o compatible, `pip` y Git. Los comandos siguientes están pensados para Windows; se ejecutan desde la raíz del repositorio.

**1. Clonar y crear un entorno virtual**

~~~powershell
git clone https://github.com/JuanEstebanLT/fastapi-sena.git
cd fastapi-sena
py -m venv venv
~~~

**2. Activar el entorno**

En PowerShell:

~~~powershell
.\venv\Scripts\Activate.ps1
~~~

En CMD:

~~~bat
venv\Scripts\activate.bat
~~~

**3. Instalar dependencias**

~~~powershell
python -m pip install -r requirements.txt
~~~

Para ejecutar las pruebas automatizadas:

~~~powershell
python -m pip install -r requirements-dev.txt
~~~

## Ejecutar las aplicaciones

Iniciar **una aplicación por vez** en el puerto 8000. Detenerla con **Ctrl + C** antes de iniciar otra.

**Guía 1 — Laboratorio de endpoints GET**

~~~powershell
python -m uvicorn guia_01.laboratorio_ev03.main:app --reload
~~~

**Guía 1 — Catálogo**

~~~powershell
python -m uvicorn guia_01.catalogo_ev04.main:app --reload
~~~

**Guía 2 — API de tienda con CRUD**

~~~powershell
python -m uvicorn guia_02.tienda_api.main:app --reload
~~~

Con el servidor activo:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **Especificación OpenAPI:** http://127.0.0.1:8000/openapi.json

La Guía 2 publica **cinco endpoints de productos y cinco de categorías**, además de una ruta de bienvenida. El servidor genera los identificadores y devuelve respuestas HTTP apropiadas, como 200, 201, 404 y 422.

## Pruebas automatizadas

La validación técnica utiliza `pytest` y `TestClient`. Para ejecutar las pruebas desde la raíz:

~~~powershell
python -m pytest tests/test_guia_01.py -q
python -m pytest tests/test_guia_02.py -q
python -m pytest tests -q
~~~

La ejecución también está configurada en [GitHub Actions](.github/workflows/pruebas-fastapi.yml) para comprobar los cambios enviados a `main`. Las pruebas cubren rutas, respuestas HTTP, CRUD y validación de solicitudes.

> Las pruebas automatizadas **complementan**, pero no reemplazan, las capturas reales de Swagger UI requeridas como evidencia práctica.

## Organización de evidencias

Las evidencias se presentan en **dos ubicaciones por guía**:

1. **Carpeta individual:** `guia_XX/evidencias/`. Contiene los documentos y las grabaciones correspondientes a la guía.
2. **Índice central:** `evidencias/guia_XX/`. Reúne una copia organizada para facilitar la consulta de todas las guías desde un mismo punto.

La carpeta `evidencias/` contiene únicamente el índice y las subcarpetas identificadas por guía; **no mantiene informes o videos sueltos**.

- [Evidencias generales — índice](evidencias/README.md)
- [Evidencias Guía 1 — carpeta central](evidencias/guia_01/README.md) · [carpeta individual](guia_01/evidencias/README.md)
- [Evidencias Guía 2 — carpeta central](evidencias/guia_02/README.md) · [carpeta individual](guia_02/evidencias/README.md)
- [Próximas evidencias — Guía 3](evidencias/guia_03/README.md)

**Estado de entrega:** la Guía 1 cuenta con informe y video publicados. La Guía 2 cuenta con su código, documentación y pruebas publicados, y conserva pendiente la carga del informe Word al repositorio y la futura grabación del video explicativo. La Guía 3 no se ha iniciado.

## Referencias técnicas

- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [FastAPI: aplicaciones en múltiples archivos](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Pydantic: modelos](https://docs.pydantic.dev/latest/concepts/models/)
- [Documentación de Uvicorn](https://www.uvicorn.org/)
- [Documentación de pytest](https://docs.pytest.org/)

---

<div align="center">

**Proyecto académico · SENA · ADSO**  
**Responsable del repositorio:** [JuanEstebanLT](https://github.com/JuanEstebanLT)

</div>

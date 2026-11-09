<div align="center">

# FastAPI · SENA
### Desarrollo progresivo de API REST con Python

**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Instructor:** Mateo Arroyave  
**Equipo:** Juan Esteban Lezcano Tejada · Mariana Suárez · Emanuel Villa

</div>

## Descripción del repositorio

Este repositorio contiene las actividades de aprendizaje del curso FastAPI. Cada guía tiene su propio código, instrucciones, pruebas y carpeta de evidencias, sin mezclar los endpoints de distintas prácticas. Se conserva un **índice central de evidencias** para consultar los informes y las grabaciones desde un solo lugar.

La Guía 2 utiliza memoria temporal; la persistencia de datos no forma parte de este laboratorio. No existe despliegue público de la API.

## Guías disponibles

| Guía | Tema | Documentación | Evidencias | Video explicativo |
| --- | --- | --- | --- | --- |
| **Guía 1** | Fundamentos, parámetros HTTP y consultas GET | [README Guía 1](guia_01/README.md) | [Informe PDF](guia_01/evidencias/Guia_FastAPI_Final.pdf) | [YouTube](https://youtu.be/39X68AKH1gg) · [MP4](guia_01/evidencias/Guia1%20-%20FastAPI.mp4) |
| **Guía 2** | CRUD, Pydantic, BaseModel y APIRouter | [README Guía 2](guia_02/README.md) | [Carpeta de evidencias](guia_02/evidencias/README.md) · informe Word finalizado fuera de GitHub, pendiente de carga | Pendiente de grabación |
| **Guía 3** | Próxima actividad | Se incorporará al iniciar la guía | [Carpeta general prevista](evidencias/guia_03/README.md) | Todavía no existe |

**Acceso central:** [Índice general de evidencias](evidencias/README.md).

## Organización del proyecto

~~~text
fastapi-sena/
├── README.md
├── requirements.txt
├── requirements-dev.txt
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
├── evidencias/
│   ├── README.md
│   ├── guia_01/
│   │   ├── Guia_01_Informe_Final_FastAPI.pdf
│   │   └── Guia_01_Sustentacion_FastAPI.mp4
│   ├── guia_02/
│   │   └── README.md
│   └── guia_03/
│       └── README.md
└── tests/
    ├── test_guia_01.py
    └── test_guia_02.py
~~~

Las carpetas Python contienen archivos de inicialización de paquetes; el esquema anterior resalta los componentes principales. Los archivos históricos de la Guía 1 en la carpeta de evidencias antigua de la raíz se mantienen para no romper enlaces existentes.

### Código y documentos por guía

**Guía 1**
- [Descripción y ejecución](guia_01/README.md)
- [Aplicación base](guia_01/main.py)
- [Laboratorio EV03](guia_01/laboratorio_ev03/main.py)
- [Catálogo EV04](guia_01/catalogo_ev04/main.py)
- [Pruebas automatizadas](tests/test_guia_01.py)
- [Evidencias individuales](guia_01/evidencias/README.md)
- [Copia en evidencias generales](evidencias/guia_01/README.md)

**Guía 2**
- [Descripción y ejecución](guia_02/README.md)
- [Aplicación modular](guia_02/tienda_api/main.py)
- [Router de productos](guia_02/tienda_api/routers/productos.py)
- [Router de categorías](guia_02/tienda_api/routers/categorias.py)
- [Pruebas automatizadas](tests/test_guia_02.py)
- [Evidencias individuales](guia_02/evidencias/README.md)
- [Evidencias generales](evidencias/guia_02/README.md)

**Próximas guías:** se agregará una carpeta propia por guía y se conservará una segunda copia de sus archivos de entrega dentro del índice general.

## Instalación

Desde la raíz del repositorio en Windows:

~~~powershell
git clone https://github.com/JuanEstebanLT/fastapi-sena.git
cd fastapi-sena
py -m venv venv
~~~

En **CMD**:

~~~bat
venv\Scripts\activate.bat
~~~

En **PowerShell**:

~~~powershell
.\venv\Scripts\Activate.ps1
~~~

Instalar las dependencias:

~~~powershell
python -m pip install -r requirements.txt
~~~

Para ejecutar también las pruebas:

~~~powershell
python -m pip install -r requirements-dev.txt
~~~

## Ejecutar las aplicaciones

Ejecutar solo una aplicación a la vez en el puerto 8000. Los comandos se utilizan desde la **raíz del repositorio**.

| Práctica | Comando |
| --- | --- |
| Guía 1 — Laboratorio | python -m uvicorn guia_01.laboratorio_ev03.main:app --reload |
| Guía 1 — Catálogo | python -m uvicorn guia_01.catalogo_ev04.main:app --reload |
| Guía 2 — Tienda CRUD | python -m uvicorn guia_02.tienda_api.main:app --reload |

Documentación interactiva: [Swagger UI](http://127.0.0.1:8000/docs) · [ReDoc](http://127.0.0.1:8000/redoc) · [OpenAPI JSON](http://127.0.0.1:8000/openapi.json).

Detener el servidor con **Ctrl + C** antes de cambiar de práctica.

## Pruebas automatizadas

~~~powershell
python -m pytest tests/test_guia_01.py -q
python -m pytest tests/test_guia_02.py -q
python -m pytest tests -q
~~~

Las pruebas verifican rutas, operaciones CRUD y errores HTTP. **Las capturas reales de Swagger UI son evidencia académica adicional** y no se sustituyen por estas pruebas.

## Gestión de evidencias

Cada guía guarda sus documentos y videos en su carpeta particular: por ejemplo, [Guía 1](guia_01/evidencias/README.md) y [Guía 2](guia_02/evidencias/README.md). La carpeta [evidencias/](evidencias/README.md) conserva otra copia por guía para facilitar la entrega y consulta global.

**Situación de la Guía 2:** el código y la documentación técnica están publicados. El informe académico final ya se preparó fuera del repositorio; falta cargar su archivo Word en las dos carpetas de evidencias. El video grupal se publicará después de grabarlo, por lo que no se presenta ningún enlace todavía.

## Referentes

- [FastAPI](https://fastapi.tiangolo.com/)
- [APIRouter y aplicaciones en varios archivos](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Uvicorn](https://www.uvicorn.org/)

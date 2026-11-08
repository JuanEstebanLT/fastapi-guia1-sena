# Guía 1 — Fundamentos de API con FastAPI

**SENA · ADSO · Instructor: Mateo Arroyave**

La primera guía está finalizada y documentada. Contiene cuatro evidencias: reflexión inicial, comparación Flask/FastAPI y mapa conceptual, laboratorio introductorio de seis endpoints GET, y catálogo de cinco endpoints GET.

## Componentes

| Evidencia | Código | Endpoints |
| --- | --- | --- |
| GA1-AA2-EV03 | [Laboratorio](laboratorio_ev03/main.py) | `GET /`, `/productos/{producto_id}`, `/buscar`, `/categorias/{categoria_id}`, `/saludo/{nombre}`, `/filtrar` |
| GA1-AA3-EV04 | [Catálogo](catalogo_ev04/main.py) | `GET /`, `/productos`, `/productos/{producto_id}`, `/categorias`, `/buscar` |

La reflexión inicial **GA1-AA1-EV01** y el cuadro comparativo y mapa conceptual **GA1-AA1-EV02** están incluidos en el informe académico.

## Ejecución

Desde la **raíz del repositorio**, con FastAPI y Uvicorn instalados:

**Laboratorio EV03**

```powershell
python -m uvicorn guia_01.laboratorio_ev03.main:app --reload
```

**Catálogo EV04**

```powershell
python -m uvicorn guia_01.catalogo_ev04.main:app --reload
```

Iniciar una sola aplicación a la vez y visitar <http://127.0.0.1:8000/docs> para probar sus rutas. Para cambiar de aplicación, detener el servidor con **Ctrl + C**.

Para ejecutar las pruebas automatizadas de la Guía 1:

```powershell
python -m pytest tests/test_guia_01.py -q
```

## Evidencias

- [Informe final PDF de la Guía 1](evidencias/Guia_FastAPI_Final.pdf).
- [Grabación MP4 de la sustentación](evidencias/Guia1%20-%20FastAPI.mp4).
- [Video de la sustentación en YouTube](https://youtu.be/39X68AKH1gg).

**Integrantes:** Juan Esteban Lezcano Tejada, Mariana Suárez y Emanuel Villa.

[Regresar al índice de todas las guías](../README.md).

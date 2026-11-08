from fastapi.testclient import TestClient
from guia_01.laboratorio_ev03.main import app as app_laboratorio
from guia_01.catalogo_ev04.main import app as app_catalogo

laboratorio = TestClient(app_laboratorio)
catalogo = TestClient(app_catalogo)

def test_laboratorio_seis_endpoints_y_validacion():
    rutas = {ruta.path for ruta in app_laboratorio.routes if getattr(ruta, 'include_in_schema', False) and getattr(ruta, 'methods', None) and 'GET' in ruta.methods}
    assert rutas == {'/', '/productos/{producto_id}', '/buscar', '/categorias/{categoria_id}', '/saludo/{nombre}', '/filtrar'}
    assert laboratorio.get('/').status_code == 200
    assert laboratorio.get('/productos/5').json()['producto_id'] == 5
    assert laboratorio.get('/buscar', params={'nombre': 'Teclado', 'precio_max': 200000}).status_code == 200
    assert laboratorio.get('/categorias/2').status_code == 200
    assert laboratorio.get('/saludo/Mariana').status_code == 200
    assert laboratorio.get('/filtrar', params={'categoria': 'Perifericos', 'disponible': 'true'}).status_code == 200
    assert laboratorio.get('/productos/abc').status_code == 422

def test_catalogo_cinco_endpoints_y_error_404():
    rutas = {ruta.path for ruta in app_catalogo.routes if getattr(ruta, 'include_in_schema', False) and getattr(ruta, 'methods', None) and 'GET' in ruta.methods}
    assert rutas == {'/', '/productos', '/productos/{producto_id}', '/categorias', '/buscar'}
    assert catalogo.get('/').status_code == 200
    assert len(catalogo.get('/productos').json()) == 3
    assert catalogo.get('/productos/2').json()['nombre'] == 'Mouse gamer'
    assert 'Perifericos' in catalogo.get('/categorias').json()
    assert len(catalogo.get('/buscar', params={'nombre': 'mouse'}).json()) == 1
    assert catalogo.get('/productos/99').status_code == 404

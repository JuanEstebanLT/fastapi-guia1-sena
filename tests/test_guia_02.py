import pytest
from fastapi.testclient import TestClient
from guia_02.tienda_api.main import app
from guia_02.tienda_api.routers import productos as mod_productos, categorias as mod_categorias

client = TestClient(app)

@pytest.fixture(autouse=True)
def restaurar_datos():
    original_productos = [p.copy() for p in mod_productos.productos]
    original_categorias = [c.copy() for c in mod_categorias.categorias]
    yield
    mod_productos.productos[:] = original_productos
    mod_categorias.categorias[:] = original_categorias

def test_rutas_modulares_y_docs():
    assert client.get('/').status_code == 200
    assert client.get('/docs').status_code == 200
    schema = client.get('/openapi.json').json()
    assert {"Productos", "Categorias"}.issubset({x for methods in schema['paths'].values() for operation in methods.values() for x in operation.get('tags', [])})
    assert len(schema['paths']) == 5  # ruta de inicio, 2 rutas de productos y 2 de categorías

def test_productos_crear_consultar_actualizar_eliminar():
    assert len(client.get('/productos').json()) == 3
    datos = {'nombre': 'Webcam', 'precio': 75000, 'categoria': 'Perifericos'}
    r = client.post('/productos', json=datos)
    assert r.status_code == 201
    nuevo_id = r.json()['producto']['id']
    assert client.get(f'/productos/{nuevo_id}').json()['nombre'] == 'Webcam'
    assert len(client.get('/productos').json()) == 4
    datos['precio'] = 81000
    r = client.put(f'/productos/{nuevo_id}', json=datos)
    assert r.status_code == 200
    assert client.get(f'/productos/{nuevo_id}').json()['precio'] == 81000
    assert client.delete(f'/productos/{nuevo_id}').status_code == 200
    assert client.get(f'/productos/{nuevo_id}').status_code == 404

def test_productos_error_404_y_422():
    assert client.get('/productos/999').status_code == 404
    assert client.put('/productos/999', json={'nombre':'x','precio':5,'categoria':'a'}).status_code == 404
    assert client.delete('/productos/999').status_code == 404
    assert client.post('/productos', json={'nombre': 'Webcam', 'categoria': 'Perifericos'}).status_code == 422
    assert client.post('/productos', json={'nombre': 'Webcam', 'precio': 'no es un número', 'categoria': 'Perifericos'}).status_code == 422

def test_categorias_crud_y_validacion():
    assert len(client.get('/categorias').json()) == 3
    assert client.get('/categorias/1').json()['nombre'] == 'Perifericos'
    r = client.post('/categorias', json={'nombre': 'Computadores'})
    assert r.status_code == 201
    id_categoria = r.json()['categoria']['id']
    assert client.get(f'/categorias/{id_categoria}').status_code == 200
    r = client.put(f'/categorias/{id_categoria}', json={'nombre': 'Portátiles'})
    assert r.status_code == 200
    assert client.get(f'/categorias/{id_categoria}').json()['nombre'] == 'Portátiles'
    assert client.delete(f'/categorias/{id_categoria}').status_code == 200
    assert client.get(f'/categorias/{id_categoria}').status_code == 404
    assert client.get('/categorias/999').status_code == 404
    assert client.put('/categorias/999', json={'nombre': 'A'}).status_code == 404
    assert client.delete('/categorias/999').status_code == 404
    assert client.post('/categorias', json={}).status_code == 422
    assert client.post('/categorias', json={'nombre': ['invalido']}).status_code == 422

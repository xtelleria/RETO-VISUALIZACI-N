from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import random

# Configura la conexión a Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Listas de marcas y modelos
marcas = ['Marca_A', 'Marca_B', 'Marca_C', 'Marca_D', 'Marca_E']
modelos_por_marca = {
    'Marca_A': ['Modelo_1A', 'Modelo_2A', 'Modelo_3A'],
    'Marca_B': ['Modelo_1B', 'Modelo_2B', 'Modelo_3B'],
    'Marca_C': ['Modelo_1C', 'Modelo_2C', 'Modelo_3C'],
    'Marca_D': ['Modelo_1D', 'Modelo_2D', 'Modelo_3D'],
    'Marca_E': ['Modelo_1E', 'Modelo_2E', 'Modelo_3E']
}

# Generar 100 datos de ejemplo para indexar
data = []
for i in range(100):
    # Seleccionar aleatoriamente una marca y un modelo de esa marca
    marca = random.choice(marcas)
    modelo = random.choice(modelos_por_marca[marca])
    
    # Generar datos aleatorios para el almacén
    cantidad_disponible = random.randint(0, 1000)
    precio_unitario = round(random.uniform(1, 100), 2)
    fecha_actualizacion = datetime.now() - timedelta(days=random.randint(1, 30))
    
    # Construir el documento
    doc = {
        'marca': marca,
        'modelo': modelo,
        'cantidad_disponible': cantidad_disponible,
        'precio_unitario': precio_unitario,
        'fecha_actualizacion': fecha_actualizacion
    }
    data.append(doc)

# Indexar los datos en un índice específico
index_name = 'stock'
doc_type = '_doc'  # Elasticsearch 7.x y superior recomienda '_doc' como tipo de documento

# Indexar los datos en Elasticsearch
for i, doc in enumerate(data):
    es.index(index=index_name, body=doc, id=i+1)

print("Datos de stock indexados correctamente en Elasticsearch.")



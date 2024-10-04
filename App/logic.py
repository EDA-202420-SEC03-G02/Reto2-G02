import time
import json
import csv
from DataStructures import array_list as array


csv.field_size_limit(2147483647)
data_dir = 'C:\\Users\\dfeli\\Downloads\\Universidad Segundo Semestre\\Estructura De Datos Y Algoritmos\\Retos\\Reto 1\\reto1-G02\\Data\\movies-large.csv'#cambien las rutas si necesitan



def create_genre(genre_id, genre_name):
    return {"id": genre_id, "name": genre_name}

def create_production_company(company_id, company_name):
    return {"id": company_id, "name": company_name}

def process_genres():
    genres_list = []
    with open(data_dir, encoding='utf-8') as file:
        movies = csv.DictReader(file)
        for movie in movies:
            genres_data = json.loads(movie["genres"])
            for genre in genres_data:
                genre_obj = create_genre(genre["id"], genre["name"])
                genres_list.append(genre_obj)
    return genres_list

def process_production_companies():
    production_companies_list = []
    with open(data_dir, encoding='utf-8') as file:
        movies = csv.DictReader(file)
        for movie in movies:
            companies_data = json.loads(movie["production_companies"])
            for company in companies_data:
                company_obj = create_production_company(company["id"], company["name"])
                production_companies_list.append(company_obj)
    return production_companies_list
  

def new_logic_ar():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog_array = {'id': None,
            'title': None,
            'original_language': None,
            'release_date': None,
            'revenue': None,
            'runtime': None,
            'status': None,
            'vote_average': None,
            'vote_count': None,
            'budget': None,
            'genres': None,
            'production_companies': None,
            }

    catalog_array['id'] = array.new_list()
    catalog_array['title'] = array.new_list() 
    catalog_array['original_language'] = array.new_list()
    catalog_array['release_date'] = array.new_list()
    catalog_array['revenue'] = array.new_list() 
    catalog_array['runtime'] = array.new_list()
    catalog_array['status'] = array.new_list()
    catalog_array['vote_average'] = array.new_list()
    catalog_array['vote_count'] = array.new_list() 
    catalog_array['budget'] = array.new_list()
    genres_data = process_genres()
    production_companies_data = process_production_companies()
    array.add_all(catalog_array['genres'], genres_data)
    array.add_all(catalog_array['production_companies'], production_companies_data)   
    return catalog_array

pass


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
     with open(filename, encoding='utf-8') as file:
        movies = csv.DictReader(file)
        for movie in movies:
            array.add_last(catalog_array['id'], movie['id'])
            array.add_last(catalog_array['title'], movie['title'])
            array.add_last(catalog_array['original_language'], movie['original_language'])
            array.add_last(catalog_array['release_date'], movie['release_date'])
            array.add_last(catalog_array['revenue'], movie['revenue'] if movie['revenue'] else "Indefinido")
            array.add_last(catalog_array['runtime'], movie['runtime'] if movie['runtime'] else 0)
            array.add_last(catalog_array['status'], movie['status'])
            array.add_last(catalog_array['vote_average'], movie['vote_average'])
            array.add_last(catalog_array['vote_count'], movie['vote_count'])
            array.add_last(catalog_array['budget'], movie['budget'] if movie['budget'] else "Indefinido")
   


pass

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    for i in range(array.size(catalog_array['id'])):
        if array.get_element(catalog_array['id'], i) == id:
            pelicula = {
                'runtime': array.get_element(catalog_array['runtime'], i),
                'release_date': array.get_element(catalog_array['release_date'], i),
                'title': array.get_element(catalog_array['title'], i),
                'budget': array.get_element(catalog_array['budget'], i),
                'revenue': array.get_element(catalog_array['revenue'], i),
                'vote_average': array.get_element(catalog_array['vote_average'], i),
                'vote_count': array.get_element(catalog_array['vote_count'], i),
                'genres': array.get_element(catalog_array['genres'], i),
                'production_companies': array.get_element(catalog_array['production_companies'], i),
                'original_language': array.get_element(catalog_array['original_language'], i),
            }
            return pelicula
    return None  
pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

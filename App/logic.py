import time
import json  
import csv
from DataStructures import array_list as array
from datetime import datetime

csv.field_size_limit(2147483647)
data_dir = "C:/Users/danie/Downloads/reto 2/Reto2-G02/Data/movies-large.csv"
#cambien las rutas si necesitan



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

def cmp_movie(movie1, movie2):
    """
    Función de comparación que verifica si dos películas son iguales basadas
    en el nombre y el idioma original.
    
    :param movie1: Una tupla con (nombre, idioma)
    :param movie2: Otra tupla con (nombre, idioma)
    :return: 0 si son iguales, 1 si movie1 > movie2, -1 si movie1 < movie2
    """
    if movie1[0] == movie2[0] and movie1[1] == movie2[1]:
        return 0
    return -1
        
def req_1(catalog,movie_name, movie_language):
    """
    Retorna el resultado del requerimiento 1
    """
    """
    Encuentra una película por su nombre y su idioma original de publicación.
    
    :param catalog: Estructura del catálogo
    :param movie_name: Nombre de la película
    :param movie_language: Idioma original de la película
    :return: Diccionario con la información de la película, o None si no se encuentra
    """
    encontrar_pelicula = (movie_name, movie_language)
    
    for pos in range(len(catalog['title'])):
        current_movie = (catalog['title'][pos], catalog['original_language'][pos])
        
        if cmp_movie(encontrar_pelicula, current_movie) == 0:
            return {
                'title': get_element(catalog['title'], pos),
                'original_language': get_element(catalog['original_language'], pos),
                'runtime': get_element(catalog['runtime'], pos),
                'release_date': get_element(catalog['release_date'], pos),
                'budget': get_element(catalog['budget'], pos),
                'revenue': get_element(catalog['revenue'], pos),
                'profit': float(get_element(catalog['revenue'], pos)) - float(get_element(catalog['budget'], pos)),
                'vote_average': get_element(catalog['vote_average'], pos)
            }
    
    return None  # Si no encuentra la película

def cmp_by_date(movie1, movie2):
    """ Función de comparación por fecha de publicación para orden descendente """
    # Convertir las fechas de las películas a objetos datetime para comparar
    date1 = datetime.strptime(movie1['release_date'], '%Y-%m-%d')
    date2 = datetime.strptime(movie2['release_date'], '%Y-%m-%d')
    return date1 > date2  # Orden descendente (más reciente primero)


def req_2(catalog, n, original_language):
    """
    Retorna el resultado del requerimiento 2

    Lista las últimas N películas publicadas en un idioma específico.
    
    :param catalog: Estructura de datos que contiene las películas
    :param n: Número de películas a listar
    :param original_language: Idioma original de las películas
    :return: Lista de las últimas N películas en orden cronológico
    """
    # Paso 1: Filtrar películas por el idioma original
    filtar_peliculas = []
    
    for pos in range(len(catalog['title'])):
        if catalog['original_language'][pos] == original_language:
            movie = {
                'title': array.get_element(catalog['title'], pos),
                'original_language': array.get_element(catalog['original_language'], pos),
                'release_date': array.get_element(catalog['release_date'], pos),
                'budget': float(array.get_element(catalog['budget'], pos)) if array.get_element(catalog['budget'], pos) != 'Indefinido' else 0.0,
                'revenue': float(array.get_element(catalog['revenue'], pos)) if array.get_element(catalog['revenue'], pos) != 'Indefinido' else 0.0,
                'runtime': array.get_element(catalog['runtime'], pos),
                'vote_average': array.get_element(catalog['vote_average'], pos)
            }
            movie['profit'] = movie['revenue'] - movie['budget']  # Calcular la ganancia
            filtar_peliculas.append(movie)
    
    # Total de películas encontradas en ese idioma
    total_movies = len(filtar_peliculas)

    if total_movies == 0:
        return f"No se encontraron películas en el idioma {original_language}."

    # Paso 2: Ordenar las películas por fecha de publicación (de más reciente a más antigua)
    sorted_movies = array.merge_sort(filtar_peliculas, cmp_by_date)

    # Paso 3: Tomar las primeras N películas
    latest_n_movies = sorted_movies[:n]

    # Preparar la respuesta con los datos requeridos
    resp = {
        'total_movies_in_language': total_movies,
        'latest_n_movies': []
    }

    for movie in latest_n_movies:
        movie_info = {
            'release_date': movie['release_date'],
            'title': movie['title'],
            'budget': movie['budget'],
            'revenue': movie['revenue'],
            'profit': movie['profit'],
            'runtime': movie['runtime'],
            'vote_average': movie['vote_average']
        }
        resp['latest_n_movies'].append(movie_info)

    return resp

def esta_en_rango(movie_date, start_date, end_date):
    """
    Verifica si una fecha de la película está dentro del rango de fechas dado.
    """
    movie_date = datetime.strptime(movie_date, '%Y-%m-%d')
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    return start_date <= movie_date <= end_date

def req_3(catalog, original_language, start_date, end_date):
    """
    Retorna el resultado del requerimiento 3
    Lista las películas publicadas en un idioma específico dentro de un rango de fechas.
    
    :param catalog: Estructura del catálogo con las películas
    :param original_language: Idioma original de las películas a buscar
    :param start_date: Fecha inicial del periodo a consultar (formato '%Y-%m-%d')
    :param end_date: Fecha final del periodo a consultar (formato '%Y-%m-%d')
    :return: Información sobre las películas que cumplen con los criterios.
    """
    # Paso 1: Filtrar películas por idioma y por rango de fechas
    filtrar_peliculas = []
    
    for pos in range(len(catalog['title'])):
        movie_language = array.get_element(catalog['original_language'], pos)
        movie_date = array.get_element(catalog['release_date'], pos)
        
        if (movie_language == original_language and 
            esta_en_rango(movie_date, start_date, end_date)):
            
            movie = {
                'title': array.get_element(catalog['title'], pos),
                'release_date': movie_date,
                'budget': float(array.get_element(catalog['budget'], pos)) if array.get_element(catalog['budget'], pos) != 'Indefinido' else 0.0,
                'revenue': float(array.get_element(catalog['revenue'], pos)) if array.get_element(catalog['revenue'], pos) != 'Indefinido' else 0.0,
                'runtime': array.get_element(catalog['runtime'], pos),
                'vote_average': array.get_element(catalog['vote_average'], pos),
                'status': array.get_element(catalog['status'], pos)
            }
            movie['profit'] = movie['revenue'] - movie['budget']  # Calcular ganancia
            filtrar_peliculas.append(movie)
    
    # Si no se encuentran películas
    if array.size(filtrar_peliculas) == 0:
        return f"No se encontraron películas en el idioma {original_language} entre {start_date} y {end_date}."
    
    # Paso 2: Calcular el tiempo promedio de duración usando get_element
    total_runtime = 0
    for pos, movie in enumerate(filtrar_peliculas):
        runtime = array.get_element(catalog['runtime'], pos)  # Obtener el tiempo de duración usando get_element
        total_runtime += runtime

    promedio_runtime = total_runtime / len(filtrar_peliculas)  # Calcular el promedio

    # Paso 3: Ordenar las películas por fecha de publicación (de más antigua a más reciente)
    filtrar_peliculas = array.merge_sort(filtrar_peliculas, lambda m1, m2: datetime.strptime(m1['release_date'], '%Y-%m-%d') < datetime.strptime(m2['release_date'], '%Y-%m-%d'))

    # respuesta
    resp = {
        'total_movies': len(filtrar_peliculas),
        'average_runtime': promedio_runtime,
        'movies': []
    }

    for movie in filtrar_peliculas:
        movie_info = {
            'release_date': movie['release_date'],
            'title': movie['title'],
            'budget': movie['budget'],
            'revenue': movie['revenue'],
            'profit': movie['profit'],
            'runtime': movie['runtime'],
            'vote_average': movie['vote_average'],
            'status': movie['status']
        }
        resp['movies'].append(movie_info)

    return resp


def req_4(catalog, status, start_date, end_date):
    """
    Lista las películas publicadas con un estado específico dentro de un rango de fechas.
    
    :param catalog: Estructura del catálogo con las películas
    :param status: Estado de publicación de las películas a buscar (ej: "Released", "Rumored")
    :param start_date: Fecha inicial del periodo a consultar (formato '%Y-%m-%d')
    :param end_date: Fecha final del periodo a consultar (formato '%Y-%m-%d')
    :return: Información sobre las películas que cumplen con los criterios.
    """
    # Paso 1: Filtrar películas por estado y rango de fechas
    filtrar_peliculas = []

    for pos in range(array.size(catalog['title'])):
        movie_status = array.get_element(catalog['status'], pos)
        movie_date = array.get_element(catalog['release_date'], pos)
        
        if (movie_status == status and 
           esta_en_rango(movie_date, start_date, end_date)):
            
            movie = {
                'title': array.get_element(catalog['title'], pos),
                'release_date': movie_date,
                'budget': float(array.get_element(catalog['budget'], pos)) if array.get_element(catalog['budget'], pos) != 'Indefinido' else 0.0,
                'revenue': float(array.get_element(catalog['revenue'], pos)) if array.get_element(catalog['revenue'], pos) != 'Indefinido' else 0.0,
                'runtime': array.get_element(catalog['runtime'], pos),
                'vote_average': array.get_element(catalog['vote_average'], pos),
                'original_language': array.get_element(catalog['original_language'], pos),
            }
            movie['profit'] = movie['revenue'] - movie['budget']  # Calcular ganancia
            filtrar_peliculas.append(movie)
    
    if array.size(filtrar_peliculas) == 0:
        return f"No se encontraron películas con estado {status} entre {start_date} y {end_date}."
    
    # Paso 2: Calcular el tiempo promedio de duración usando get_element
    total_runtime = 0
    for pos in range(array.size(filtrar_peliculas)):  # Usamos el tamaño de las películas filtradas
        total_runtime += array.get_element(catalog['runtime'], pos)  # Usamos get_element para obtener el runtime

    promedio_runtime = total_runtime / array.size(filtrar_peliculas)  # Calcular el promedio de duración

    # Paso 3: Ordenar las películas por fecha de publicación (de más antigua a más reciente)
    filtrar_peliculas = array.merge_sort(filtrar_peliculas, lambda m1, m2: datetime.strptime(m1['release_date'], '%Y-%m-%d') < datetime.strptime(m2['release_date'], '%Y-%m-%d'))

    # respuesta
    response = {
        'total_movies': array.size(filtrar_peliculas),
        'average_runtime': promedio_runtime,
        'movies': filtrar_peliculas
    }

    return response

def budget_range(movie_budget, budget_range):
    """
    Verifica si el presupuesto de una película está dentro del rango de presupuesto dado.
    
    :param movie_budget: Presupuesto de la película
    :param budget_range: Rango de presupuesto en formato 'min-max' (ej: '1000-1999')
    :return: True si el presupuesto está dentro del rango, False en caso contrario
    """
    min_budget, max_budget = map(int, budget_range.split('-'))
    return min_budget <= movie_budget <= max_budget

def req_5(catalog, budget_range, start_date, end_date):
    """
    Lista las películas publicadas dentro de un rango de presupuesto y fechas.
    
    :param catalog: Estructura del catálogo con las películas
    :param budget_range: Rango de presupuesto en formato 'min-max' (ej: '1000-1999')
    :param start_date: Fecha inicial del periodo a consultar (formato '%Y-%m-%d')
    :param end_date: Fecha final del periodo a consultar (formato '%Y-%m-%d')
    :return: Información sobre las películas que cumplen con los criterios.
    """
    # Paso 1: Filtrar películas por presupuesto y rango de fechas
    filtrar_peliculas = []

    for pos in range(array.size(catalog['title'])):
        movie_budget = float(array.get_element(catalog['budget'], pos))
        movie_date = array.get_element(catalog['release_date'], pos)

        # Verificar si el presupuesto está en el rango y la fecha dentro del periodo
        if budget_range(movie_budget, budget_range) and esta_en_rango(movie_date, start_date, end_date):
            
            movie = {
                'title': array.get_element(catalog['title'], pos),
                'release_date': movie_date,
                'budget': movie_budget,
                'revenue': float(array.get_element(catalog['revenue'], pos)) if array.get_element(catalog['revenue'], pos) != 'Indefinido' else 0.0,
                'runtime': array.get_element(catalog['runtime'], pos),
                'vote_average': array.get_element(catalog['vote_average'], pos),
                'original_language': array.get_element(catalog['original_language'], pos),
            }
            movie['profit'] = movie['revenue'] - movie['budget']  # Calcular ganancia
            filtrar_peliculas.append(movie)
    
    if array.size(filtrar_peliculas) == 0:
        return f"No se encontraron películas con presupuesto en el rango {budget_range} entre {start_date} y {end_date}."
    
    # Paso 2: Calcular el presupuesto promedio usando get_element
    total_budget = 0
    for movie in filtrar_peliculas:
        total_budget += movie['budget']

    avg_budget = total_budget / array.size(filtrar_peliculas)  # Calcular el promedio de presupuesto

    # Paso 3: Ordenar las películas por fecha de publicación (de más antigua a más reciente)
    filtrar_peliculas = array.merge_sort(filtrar_peliculas, lambda m1, m2: datetime.strptime(m1['release_date'], '%Y-%m-%d') < datetime.strptime(m2['release_date'], '%Y-%m-%d'))

# colocar la respuesta
    resp = {
        'total_movies': array.size(filtrar_peliculas),
        'average_budget': avg_budget,
        'movies': filtrar_peliculas
    }

    return resp


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

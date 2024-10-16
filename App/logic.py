import time
import json  
import csv
from DataStructures import array_list as array
from DataStructures import map_linear_probing as lp
from datetime import datetime


def new_logic():
    """
    Crea el catálogo para almacenar las estructuras de datos
    """
   
    catalog = {
        "movies": lp.new_map(90000,0.5)
    }
    return catalog




def load_data(catalog, filename):
    """
    Carga los datos del reto desde un archivo CSV y reporta el total de películas y 
    detalles de las cinco primeras y cinco últimas películas cargadas.
    """
    filename="C:\\Users\\dfeli\\Downloads\\Universidad Segundo Semestre\\Estructura De Datos Y Algoritmos\\Retos\\Reto 2\\Reto2-G02\\Data\\Challenge-2\\movies-large.csv"
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    movies_list = []
    
    for movie in input_file:
        # Manejo de los campos numéricos y JSON
        movie["budget"] = int(movie["budget"]) if movie["budget"] != "0" else "Undefined"
        movie["revenue"] = int(movie["revenue"]) if movie["revenue"] != "0" else "Undefined"
        movie["earnings"] = int(movie["revenue"]) - int(movie["budget"]) if movie["revenue"] != "Undefined" and movie["budget"] != "Undefined" else "Undefined"
        
        movie["genres"] = json.loads(movie["genres"]) if movie["genres"] else []
        movie["production_companies"] = json.loads(movie["production_companies"]) if movie["production_companies"] else []
        
        movie["vote_average"] = float(movie["vote_average"]) if movie["vote_average"] else "Undefined"
        movie["vote_count"] = int(movie["vote_count"]) if movie["vote_count"] else "Undefined"
        
        # Si no hay valores, asignamos "Unknown"
        movie["id"] = movie["id"] if movie["id"] else "Unknown"
        movie["title"] = movie["title"] if movie["title"] else "Unknown"
        movie["original_language"] = movie["original_language"] if movie["original_language"] else "Unknown"
        movie["release_date"] = datetime.strptime(movie["release_date"], "%Y-%m-%d").date() if movie["release_date"] else "Unknown"
        movie["status"] = movie["status"] if movie["status"] else "Unknown"
        movie["runtime"] = int(float(movie["runtime"])) if movie["runtime"] else "Unknown"
        
        # Añadir la película al catálogo
        movie_id = movie["id"]
        movies_list.append(movie)
        lp.put(catalog["movies"], movie_id, movie)

    # Reportar el total de películas cargadas
    total_movies = lp.size(catalog["movies"])
    
    # Primeras y últimas cinco películas
    first_five = movies_list[:5]
    last_five = movies_list[-5:]
    
    return total_movies, first_five, last_five

# Funciones de consulta sobre el catálogo

def get_data(catalog, movie_id):
    """
    Retorna una película por su ID.
    """
    return lp.get(catalog["movies"], movie_id)
pass

        
def req_1(catalog, title, original_language):
    """Busca una película por su nombre y idioma original.
    
    :param catalog: Catálogo que contiene la lista de películas
    :type catalog: dict
    :param title: Nombre de la película a buscar
    :type title: str
    :param original_language: Idioma original de la película
    :type original_language: str
    :return: Detalles de la película encontrada o un mensaje de no encontrado
    :rtype: dict
    """
    # Obtener la lista de películas
    movies_list = lp.value_set(catalog["movies"])
    
    # Buscar la película que coincida con el título y el idioma
    for movie in movies_list:
        if movie['title'].lower() == title.lower() and movie['original_language'] == original_language:

                

            return {
                "duration": movie["runtime"],
                "release_date": movie["release_date"],
                "original_title": movie["title"],
                "budget": movie["budget"],
                "revenue": movie["revenue"],
                "profit": movie["earnings"],
                "rating": movie["vote_average"],
                "original_language": movie["original_language"]
            }

    return None



def date_sort_criteria(element1, element2):
    return element1['release_date'] > element2['release_date']
def req_2(catalog, n, original_language):
    """Lista las últimas N películas publicadas en un idioma original específico.
    
    :param catalog: Catálogo que contiene la lista de películas
    :type catalog: dict
    :param n: Número de películas a listar
    :type n: int
    :param original_language: Idioma original de la película
    :type original_language: str
    :return: Detalles de las últimas N películas encontradas
    :rtype: dict
    """

    movies_list = lp.value_set(catalog["movies"])

    # Filtrar películas por idioma original
    filtered_movies = []

    for movie in movies_list:
        if movie['original_language'] == original_language:
            filtered_movies.append(movie)

    # Crear una lista para usar con el algoritmo de ordenamiento
    my_list = array.new_list()
    for movie in filtered_movies:
        array.add_last(my_list, movie)#se añaden las películas filtradas a esta lista usando

    # Ordenar películas por fecha de publicación usando merge_sort
    sorted_movies = array.merge_sort(my_list, date_sort_criteria)

    
    response = {
        "total_movies": array.size(my_list),
        "movies": []
    }

    # Limitar a las últimas N películas
    for movie in sorted_movies['elements'][:n]:  # Acceder a los elementos de la lista ordenada

        response["movies"].append({
            "release_date": movie["release_date"],
            "original_title": movie["title"],
            "budget": movie["budget"],
            "revenue": movie["revenue"],
            "profit": movie["earnings"],
            "runtime": movie["runtime"],
            "rating": movie["vote_average"]
        })

    return response

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
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Filtrar películas por idioma original y rango de fechas
    filtered_movies = []
    
    for movie in catalog["movies"]:
        if movie['original_language'] == original_language:
            release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
            if start_date <= release_date <= end_date:
                filtered_movies.append(movie)

    # Crear una lista para usar con el algoritmo de ordenamiento
    my_list = array.new_list()
    for movie in filtered_movies:
        array.add_last(my_list, movie)

    # Ordenar películas por fecha de publicación usando merge_sort
    sorted_movies = array.merge_sort(my_list, date_sort_criteria)

    # Calcular el total de películas y el tiempo promedio de duración
    total_movies = array.size(my_list)
    average_duration = sum(movie['runtime'] for movie in sorted_movies['elements']) / total_movies if total_movies > 0 else 0

    # Preparar la respuesta
    response = {
        "total_movies": total_movies,
        "average_duration": average_duration,
        "movies": []
    }

    # Limitar a las primeras 10 películas si hay más de 20
    for movie in sorted_movies['elements'][:10]:
        response["movies"].append({
            "release_date": movie["release_date"],
            "original_title": movie["title"],
            "budget": movie["budget"],
            "revenue": movie["revenue"],
            "profit": movie["earnings"],
            "runtime": movie["runtime"],
            "rating": movie["vote_average"],
            "status": movie.get("status", "Undefined")
        })

    return response


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

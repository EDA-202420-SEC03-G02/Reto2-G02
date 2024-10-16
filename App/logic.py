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
    start_time = get_time()
    # Buscar la película que coincida con el título y el idioma
    for movie in movies_list:
        if movie['title'].lower() == title.lower() and movie['original_language'] == original_language:

            end_time = get_time()
            delta = delta_time(start_time, end_time)                

            return {
                "duration": movie["runtime"],
                "release_date": movie["release_date"],
                "original_title": movie["title"],
                "budget": movie["budget"],
                "revenue": movie["revenue"],
                "profit": movie["earnings"],
                "rating": movie["vote_average"],
                "original_language": movie["original_language"]
            }, delta
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return None, delta



def date_sort_criteria(element1, element2):
    return element1['release_date'] > element2['release_date']# peliculas mas recientes de primeras
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
    start_time = get_time()
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
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response,delta

def req_3(catalog, original_language, start_date, end_date):#est-1
    """
    Retorna el resultado del requerimiento 3
    Lista las películas publicadas en un idioma específico dentro de un rango de fechas.
    
    :param catalog: Estructura del catálogo con las películas
    :param original_language: Idioma original de las películas a buscar
    :param start_date: Fecha inicial del periodo a consultar (formato '%Y-%m-%d')
    :param end_date: Fecha final del periodo a consultar (formato '%Y-%m-%d')
    :return: Información sobre las películas que cumplen con los criterios.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    movies_list = lp.value_set(catalog["movies"])
    start_time = get_time()
    # Filtrar películas por idioma original y rango de fechas
    filtered_movies = []#lista para guardar peliculas filtradas
    
    for movie in movies_list:
        if movie['original_language'] == original_language:           
            if start_date <= movie["release_date"] <= end_date:
                filtered_movies.append(movie)

    # Crear una lista para usar con el algoritmo de ordenamiento
    my_list = array.new_list()
    for movie in filtered_movies:
        array.add_last(my_list, movie)

    # Ordenar películas por fecha de publicación usando merge_sort
    sorted_movies = array.merge_sort(my_list, date_sort_criteria)

    # Calcular el total de películas y el tiempo promedio de duración
    total_movies = array.size(my_list)
    total_runtime = 0

    # Calcular la duración total de las películas
    for movie in sorted_movies['elements']:
        total_runtime += movie['runtime']  # Acumular la duración de cada película

    # Calcular la duración promedio
    average_duration = total_runtime / total_movies if total_movies > 0 else 0


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
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response,delta


def req_4(catalog, status, start_date, end_date):#est-2
    """
    Lista las películas publicadas con un estado específico dentro de un rango de fechas.
    
    :param catalog: Estructura del catálogo con las películas
    :param status: Estado de publicación de las películas a buscar (ej: "Released", "Rumored")
    :param start_date: Fecha inicial del periodo a consultar (formato '%Y-%m-%d')
    :param end_date: Fecha final del periodo a consultar (formato '%Y-%m-%d')
    :return: Información sobre las películas que cumplen con los criterios.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    movies_list = lp.value_set(catalog["movies"])
    start_time = get_time()
    # Filtrar películas por estado de producción y rango de fechas
    filtered_movies = []

    for movie in movies_list:
        if movie['status'] == status:
            if start_date <= movie["release_date"] <= end_date:
                filtered_movies.append(movie)

    # Crear una lista para usar con el algoritmo de ordenamiento
    my_list = array.new_list()
    for movie in filtered_movies:
        array.add_last(my_list, movie)

    # Ordenar películas por fecha de publicación usando merge_sort
    sorted_movies = array.merge_sort(my_list, date_sort_criteria)

    # Calcular el total de películas y el tiempo promedio de duración
    total_movies = array.size(my_list)
    total_runtime = 0

    for movie in sorted_movies['elements']:
        total_runtime += movie['runtime']  # Acumular la duración de cada película

    # Calcular la duración promedio
    average_duration = total_runtime / total_movies if total_movies > 0 else 0

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
            "original_language": movie["original_language"]
        })
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response,delta



def req_5(catalog, budget_range, start_date, end_date):#est-3
    """
    Lista las películas publicadas dentro de un rango de presupuesto y fechas.
    
    :param catalog: Estructura del catálogo con las películas
    :param budget_range: Rango de presupuesto en formato 'min-max' (ej: '1000-1999')
    :param start_date: Fecha inicial del periodo a consultar (formato '%Y-%m-%d')
    :param end_date: Fecha final del periodo a consultar (formato '%Y-%m-%d')
    :return: Información sobre las películas que cumplen con los criterios.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    start_time = get_time()
    budget_range_str = budget_range.split('-')# split es para separar en subcadenas teniendo en cuenta un parametro en este caso el -

    min_budget = int(budget_range_str[0])
    max_budget = int(budget_range_str[1])
    movies_list = lp.value_set(catalog["movies"])

    filtered_movies = []

    for movie in movies_list:
        budget = movie.get('budget', 0)  # Considerar presupuesto como 0 si no está definido
        if budget is not None and isinstance(budget, (int, float)):
            if min_budget <= budget < max_budget:
                if start_date <= movie["release_date"] <= end_date:
                    filtered_movies.append(movie)

    # Crear una lista para usar con el algoritmo de ordenamiento
    my_list = array.new_list()
    for movie in filtered_movies:
        array.add_last(my_list, movie)

    # Ordenar películas por fecha de publicación usando merge_sort
    sorted_movies = array.merge_sort(my_list, date_sort_criteria)

    total_movies = array.size(my_list)
    total_runtime = 0
    total_budget = 0

    for movie in sorted_movies['elements']:
        total_runtime += movie['runtime']  # Acumular la duración de cada película
        total_budget += movie.get('budget', 0)  # Acumular el presupuesto

    average_duration = total_runtime / total_movies if total_movies > 0 else 0
    average_budget = total_budget / total_movies if total_movies > 0 else 0

    response = {
        "total_movies": total_movies,
        "average_budget": average_budget,
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
            "original_language": movie["original_language"]
        })
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response,delta


def req_6(catalog, language, start_year, end_year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_year = int(start_year)
    end_year = int(end_year)
    movies_list = lp.value_set(catalog["movies"])
    start_time = get_time()

    # Diccionario para almacenar estadísticas por año
    year_stats = {}

    for movie in movies_list:
        # Verificar si la película está publicada y en el idioma correcto
        if movie['status'] == 'Released' and movie.get('original_language') == language:
            release_year = movie["release_date"].year # Extraer el año de la fecha

            # Filtrar por el rango de años
            if start_year <= release_year <= end_year:
                if release_year not in year_stats:
                    year_stats[release_year] = {# ir agregando años que faltan 
                        "total_movies": 0,
                        "total_runtime": 0,
                        "total_revenue": 0,
                        "total_rating": 0,
                        "best_movie": None,
                        "worst_movie": None
                    }

                # Acumular estadísticas
                year_stats[release_year]["total_movies"] += 1
                year_stats[release_year]["total_runtime"] += movie.get('runtime', 0)
                earnings = movie.get('earnings', 0)
                if isinstance(earnings, int):  #verificar que no sea str es decir unknown
                    earnings = earnings
                else:
                    earnings=0    
                year_stats[release_year]["total_revenue"] += earnings
                year_stats[release_year]["total_rating"] += movie.get('vote_average', 0)

                # Determinar la mejor y peor película
                current_rating = movie.get('vote_average', 0)
                if year_stats[release_year]["best_movie"] is None or current_rating > year_stats[release_year]["best_movie"]["vote_average"]:
                    year_stats[release_year]["best_movie"] = {
                        "title": movie["title"],
                        "vote_average": current_rating
                    }
                if year_stats[release_year]["worst_movie"] is None or current_rating < year_stats[release_year]["worst_movie"]["vote_average"]:
                    year_stats[release_year]["worst_movie"] = {
                        "title": movie["title"],
                        "vote_average": current_rating
                    }

    
    response = []
    
    for year in range(end_year, start_year - 1, -1):  # Desde el año más reciente al más antiguo
        if year in year_stats:
            stats = year_stats[year]
            total_movies = stats["total_movies"]
            average_runtime = stats["total_runtime"] / total_movies if total_movies > 0 else 0
            total_revenue = stats["total_revenue"]

            # Calcular el promedio de votación
            average_rating = stats["total_rating"] / total_movies if total_movies > 0 else 0

            response.append({
                "year": year,
                "total_movies": total_movies,
                "average_rating": average_rating,
                "average_runtime": average_runtime,
                "total_revenue": total_revenue,
                "best_movie": {
                    "title": stats["best_movie"]["title"] if stats["best_movie"] else "Undefined",
                    "rating": stats["best_movie"]["vote_average"] if stats["best_movie"] else "Undefined"
                },
                "worst_movie": {
                    "title": stats["worst_movie"]["title"] if stats["worst_movie"] else "Undefined",
                    "rating": stats["worst_movie"]["vote_average"] if stats["worst_movie"] else "Undefined"
                }
            })
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response, delta    
    pass


def req_7(catalog, production_company, start_year, end_year):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_year = int(start_year)
    end_year = int(end_year)
    movies_list = lp.value_set(catalog["movies"])
    start_time = get_time()

    # Diccionario para almacenar estadísticas por año
    year_stats = {}

    for movie in movies_list:
        # Verificar si la película está publicada
        if movie['status'] == 'Released':
            # Comprobar si la compañía productora está en la lista de compañías de la película
            production_found = False
            for company in movie.get('production_companies', []):
                if company['name'] == production_company:
                    production_found = True
                    break
            
            # Solo continuar si se encontró la compañía productora
            if production_found:
                
                release_year = movie["release_date"].year

                # Filtrar por el rango de años
                if start_year <= release_year <= end_year:
                    if release_year not in year_stats:
                        year_stats[release_year] = {
                            "total_movies": 0,
                            "total_runtime": 0,
                            "total_revenue": 0,
                            "total_rating": 0,
                            "best_movie": None,
                            "worst_movie": None
                        }

                    # Acumular estadísticas
                    year_stats[release_year]["total_movies"] += 1
                    year_stats[release_year]["total_runtime"] += movie.get('runtime', 0)
                    earnings = movie.get('earnings', 0)
                    if isinstance(earnings, int):  #verificar que no sea str es decir unknown
                        earnings = earnings
                    else:
                        earnings=0    
                    year_stats[release_year]["total_revenue"] += earnings
                    year_stats[release_year]["total_rating"] += movie.get('vote_average', 0)

                    # Determinar la mejor y peor película
                    current_rating = movie.get('vote_average', 0)
                    if year_stats[release_year]["best_movie"] is None or current_rating > year_stats[release_year]["best_movie"]["vote_average"]:
                        year_stats[release_year]["best_movie"] = {
                            "title": movie["title"],
                            "vote_average": current_rating
                        }
                    if year_stats[release_year]["worst_movie"] is None or current_rating < year_stats[release_year]["worst_movie"]["vote_average"]:
                        year_stats[release_year]["worst_movie"] = {
                            "title": movie["title"],
                            "vote_average": current_rating
                        }

    
    response = []
    
    for year in range(end_year, start_year - 1, -1):  # Desde el año más reciente al más antiguo
        if year in year_stats:
            stats = year_stats[year]
            total_movies = stats["total_movies"]
            average_runtime = stats["total_runtime"] / total_movies if total_movies > 0 else 0
            total_revenue = stats["total_revenue"]

            # Calcular el promedio de votación
            average_rating = stats["total_rating"] / total_movies if total_movies > 0 else 0

            response.append({
                "year": year,
                "total_movies": total_movies,
                "average_rating": average_rating,
                "average_runtime": average_runtime,
                "total_revenue": total_revenue,
                "best_movie": {
                    "title": stats["best_movie"]["title"] if stats["best_movie"] else "Undefined",
                    "rating": stats["best_movie"]["vote_average"] if stats["best_movie"] else "Undefined"
                },
                "worst_movie": {
                    "title": stats["worst_movie"]["title"] if stats["worst_movie"] else "Undefined",
                    "rating": stats["worst_movie"]["vote_average"] if stats["worst_movie"] else "Undefined"
                }
            })
    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response,delta    
    pass


def req_8(catalog, start_year, genre):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_year = int(start_year)
    movies_list = lp.value_set(catalog["movies"])
    start_time = get_time()

    # Inicializar estadísticas
    stats = {
        "total_movies": 0,
        "total_runtime": 0,
        "total_revenue": 0,
        "total_rating": 0,
        "best_movie": None,
        "worst_movie": None
    }

    for movie in movies_list:
        # Verificar si la película está publicada y pertenece al género especificado
        if movie['status'] == 'Released' and start_year == movie["release_date"].year:
            # Extraer los géneros de la película
            genres_list = movie.get('genres', [])
            genres = []
            for g in genres_list:
                genres.append(g['name'])  # Agregar el nombre del género a la lista

            # Comprobar si el género está en la lista de géneros de la película
            if genre in genres:
                stats["total_movies"] += 1
                stats["total_runtime"] += movie.get('runtime', 0)

                # Calcular ganancias 
                earnings = movie.get('earnings', 0)
                if isinstance(earnings, int):  #verificar que no sea str es decir unknown
                     earnings = earnings
                else:
                    earnings=0    
                total_revenue= earnings

                # Acumular estadísticas
                if total_revenue != "Undefined":
                    stats["total_revenue"] += total_revenue
                stats["total_rating"] += movie.get('vote_average', 0)

                # Determinar la mejor y peor película
                current_rating = movie.get('vote_average', 0)
                if stats["best_movie"] is None or current_rating > stats["best_movie"]["vote_average"]:
                    stats["best_movie"] = {
                        "title": movie["title"],
                        "vote_average": current_rating
                    }
                if stats["worst_movie"] is None or current_rating < stats["worst_movie"]["vote_average"]:
                    stats["worst_movie"] = {
                        "title": movie["title"],
                        "vote_average": current_rating
                    }

    # Calcular promedios
    average_runtime = stats["total_runtime"] / stats["total_movies"] if stats["total_movies"] > 0 else 0
    average_rating = stats["total_rating"] / stats["total_movies"] if stats["total_movies"] > 0 else 0

    response = {
        "year": start_year,
        "genre": genre,
        "total_movies": stats["total_movies"],
        "average_rating": average_rating,
        "average_runtime": average_runtime,
        "total_revenue": stats["total_revenue"],
        "best_movie": {
            "title": stats["best_movie"]["title"] if stats["best_movie"] else "Undefined",
            "rating": stats["best_movie"]["vote_average"] if stats["best_movie"] else "Undefined"
        },
        "worst_movie": {
            "title": stats["worst_movie"]["title"] if stats["worst_movie"] else "Undefined",
            "rating": stats["worst_movie"]["vote_average"] if stats["worst_movie"] else "Undefined"
        }
    }

    end_time = get_time()
    delta = delta_time(start_time, end_time)
    return response, delta
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

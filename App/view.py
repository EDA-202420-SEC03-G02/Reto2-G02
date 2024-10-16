import sys
import App.logic as lg
from tabulate import tabulate
from DataStructures import array_list
from datetime import datetime
default_limit=1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return lg.new_logic()
    pass

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos de las películas y muestra el total de películas cargadas,
    así como las cinco primeras y cinco últimas películas.
    """    
    print("Cargando información de las películas...")
    total_movies, first_five, last_five = lg.load_data(control, 'movies-large.csv')

    print(f"\nTotal de películas cargadas: {total_movies}")
    
    print("\nPrimeras cinco películas cargadas:")
    display_movies(first_five)
    
    print("\nÚltimas cinco películas cargadas:")
    display_movies(last_five)

def display_movies(movies):
    """
    Muestra la información requerida de un conjunto de películas en formato tabular.
    """
    table = []
    for movie in movies:
        table.append([
            movie["id"] if movie["id"] else "Unknown",
            movie["title"] if movie["title"] else "Unknown",
            movie["original_language"] if movie["original_language"] else "Unknown",
            movie["release_date"] if movie["release_date"] else "Unknown",
            movie["status"] if movie["status"] else "Unknown",
            movie["vote_average"] if movie["vote_average"] != "Undefined" else "Unknown",
            movie["vote_count"] if movie["vote_count"] != "Undefined" else "Unknown",
            movie["runtime"] if movie["runtime"] != "Unknown" else "Unknown",
            movie["budget"] if movie["budget"] != "Undefined" else "Unknown",
            movie["revenue"] if movie["revenue"] != "Undefined" else "Unknown",
            movie["earnings"] if movie["earnings"] != "Undefined" else "Unknown",
            ', '.join([genre['name'] for genre in movie['genres']]) if movie['genres'] else "Unknown",
            ', '.join([company['name'] for company in movie['production_companies']]) if movie['production_companies'] else "Unknown"
        ])
    
    # Usamos tabulate para imprimir los resultados en formato tabular
    print(tabulate(table, headers=[
        "ID", "Título", "Idioma", "Fecha de Publicación", "Estado", "Puntaje Promedio", 
        "Número de Votos", "Duración (min)", "Presupuesto", "Ingresos", "Ganancias", 
        "Géneros", "Compañías Productoras"
    ], tablefmt="fancy_grid"))
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    title = input("Ingrese el nombre de la película: ")
    original_language = input("Ingrese el idioma original de la película: ")

    result,time = lg.req_1(control, title, original_language)
    
    if isinstance(result, dict):
            print("Detalles de la película:")
            table = [
                ["Título", result['original_title']],
                ["Idioma original", result['original_language']],
                ["Duración", f"{result['duration']} minutos"],
                ["Fecha de publicación", result['release_date'].strftime('%Y-%m-%d') if isinstance(result['release_date'], datetime) else result['release_date']],
                ["Presupuesto", result['budget']],
                ["Ingresos netos", result['revenue']],
                ["Ganancia", result['profit']],
                ["Puntaje", result['rating']]
            ]
            print(tabulate(table, headers=["Columna", "Valor"], tablefmt="grid"))
            print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")
    else:
        print("Ninguna película fue encontrada")
        print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    n = int(input("Ingrese el número de películas a listar (N): "))
    original_language = input("Ingrese el idioma original de la película (ej.: en, fr, zh): ")
    movies_info,time=lg.req_2(control,n,original_language)
    print(f"Total de películas en idioma original: {movies_info['total_movies']}")
    print("Últimas N películas:")
    
    table = []
    for movie in movies_info['movies']:
        table.append([
            movie['release_date'],
            movie['original_title'],
            movie['budget'],
            movie['revenue'],
            movie['profit'],
            f"{movie['runtime']} minutos",
            movie['rating']
        ])

    headers = ["Fecha de publicación", "Título original", "Presupuesto", "Ingresos", "Ganancia", "Duración", "Puntaje"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    original_language = str(input("Ingrese el idioma original de la película (ej.: en, fr, zh): "))
    start_date = input("Ingrese la fecha de inicio (formato: YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (formato: YYYY-MM-DD): ")

    # Llamar a req_3 con los parámetros proporcionados
    movies_info,time = lg.req_3(control, original_language, start_date, end_date)

    # Imprimir el total de películas y el tiempo promedio
    print(f"Total de películas en idioma original: {movies_info['total_movies']}")
    print(f"Tiempo promedio de duración: {movies_info['average_duration']:.2f} minutos\n")
    print("Últimas películas:")

    # Preparar la tabla para imprimir
    table = []
    for movie in movies_info['movies']:
        table.append([
            movie['release_date'],
            movie['original_title'],
            movie['budget'],
            movie['revenue'],
            movie['profit'],
            f"{movie['runtime']} minutos",
            movie['rating'],
            movie["status"]
        ])

    # Definir los encabezados de la tabla
    headers = ["Fecha de publicación", "Título original", "Presupuesto", "Ingresos", "Ganancia", "Duración", "Puntaje","Status"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")   
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    production_status = str(input("Ingrese el estado de producción de la película (ej.: Released, Rumored): "))
    start_date = input("Ingrese la fecha de inicio (formato: YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (formato: YYYY-MM-DD): ")

   
    movies_info,time = lg.req_4(control, production_status, start_date, end_date)

    # Imprimir el total de películas y el tiempo promedio
    print(f"Total de películas con estado '{production_status}': {movies_info['total_movies']}")
    print(f"Tiempo promedio de duración: {movies_info['average_duration']:.2f} minutos\n")
    print("Últimas películas:")

    # Preparar la tabla para imprimir
    table = []
    for movie in movies_info['movies']:
        table.append([
            movie['release_date'],
            movie['original_title'],
            movie['budget'],
            movie['revenue'],
            movie['profit'],
            f"{movie['runtime']} minutos",
            movie['rating'],
            movie['original_language']
        ])

    # Definir los encabezados de la tabla
    headers = ["Fecha de publicación", "Título original", "Presupuesto", "Ingresos", "Ganancia", "Duración", "Puntaje", "Idioma original"]
    print(tabulate(table, headers=headers, tablefmt="grid"))  
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")  
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    budget_range = input("Ingrese el rango de presupuesto (ej.: 0-999, 1000-1999): ")
    start_date = input("Ingrese la fecha de inicio (formato: YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (formato: YYYY-MM-DD): ")

    # Obtener la información de las películas que cumplen con el criterio
    movies_info,time = lg.req_5(control, budget_range, start_date, end_date)

    # Imprimir el total de películas y el presupuesto promedio
    print(f"Total de películas en el rango de presupuesto '{budget_range}': {movies_info['total_movies']}")
    print(f"Presupuesto promedio: {movies_info['average_budget']:.2f} dólares")
    print(f"Tiempo promedio de duración: {movies_info['average_duration']:.2f} minutos\n")
    print("Últimas películas:")

    # Preparar la tabla para imprimir
    table = []
    for movie in movies_info['movies']:
        table.append([
            movie['release_date'],
            movie['original_title'],
            movie['budget'],
            movie['revenue'],
            movie['profit'],
            f"{movie['runtime']} minutos",
            movie['rating'],
            movie['original_language']
        ])

    # Definir los encabezados de la tabla
    headers = ["Fecha de publicación", "Título original", "Presupuesto", "Ingresos", "Ganancia", "Duración", "Puntaje", "Idioma original"]
    print(tabulate(table, headers=headers, tablefmt="grid"))    
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
     
    language = input("Ingrese el idioma de las películas (ej.: 'en' para inglés): ")
    start_year = input("Ingrese el año de inicio (formato: YYYY): ")
    end_year = input("Ingrese el año de fin (formato: YYYY): ")

    # Obtener la información de las películas que cumplen con el criterio
    movies_info,time = lg.req_6(control, language, start_year, end_year)

    # Imprimir el total de películas y el presupuesto promedio
    print(f"Total de películas en el idioma '{language}' entre {start_year} y {end_year}: {len(movies_info)}")
    
    # Preparar la tabla para imprimir
    table = []
    for year_info in movies_info:
        table.append([
            year_info['year'],
            year_info['total_movies'],
            year_info['average_rating'],
            year_info['average_runtime'],
            year_info['total_revenue'],
            year_info['best_movie']['title'] if year_info['best_movie'] else "Undefined",
            year_info['best_movie']['rating'] if year_info['best_movie'] else "Undefined",
            year_info['worst_movie']['title'] if year_info['worst_movie'] else "Undefined",
            year_info['worst_movie']['rating'] if year_info['worst_movie'] else "Undefined"
        ])

    # Definir los encabezados de la tabla
    headers = ["Año", "Total de Películas", "Rating Promedio", "Duración Promedio", "Ingresos Totales", 
               "Mejor Película", "Rating Mejor Película", "Peor Película", "Rating Peor Película"]
    
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    production_company = input("Ingrese el nombre de la compañía productora: ")
    start_year = input("Ingrese el año de inicio (formato: YYYY): ")
    end_year = input("Ingrese el año de fin (formato: YYYY): ")

    # Obtener la información de las películas que cumplen con el criterio
    movies_info,time = lg.req_7(control, production_company, start_year, end_year)

    # Imprimir el total de películas por año
    print(f"Estadísticas de películas publicadas por '{production_company}' entre {start_year} y {end_year}:\n")

    # Preparar la tabla para imprimir
    table = []
    for year_info in movies_info:
        table.append([
            year_info['year'],
            year_info['total_movies'],
            year_info['average_rating'],
            year_info['average_runtime'],
            year_info['total_revenue'],
            year_info['best_movie']['title'] if year_info['best_movie'] else "Undefined",
            year_info['best_movie']['rating'] if year_info['best_movie'] else "Undefined",
            year_info['worst_movie']['title'] if year_info['worst_movie'] else "Undefined",
            year_info['worst_movie']['rating'] if year_info['worst_movie'] else "Undefined"
        ])

    # Definir los encabezados de la tabla
    headers = ["Año", "Total de Películas", "Rating Promedio", "Duración Promedio", "Ingresos Totales", 
               "Mejor Película", "Rating Mejor Película", "Peor Película", "Rating Peor Película"]
    
    print(tabulate(table, headers=headers, tablefmt="grid"))  
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")  
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    start_year = input("Ingrese el año (formato: YYYY): ")
    genre = input("Ingrese el género: ")

    # Obtener la información de las películas que cumplen con el criterio
    movies_info, time = lg.req_8(control, start_year, genre)

    # Imprimir las estadísticas de películas por género y año
    print(f"Estadísticas de películas del género '{genre}' publicadas en el año {start_year}:\n")

    # Preparar la tabla para imprimir
    table = []
    table.append([
        movies_info['year'],
        movies_info['total_movies'],
        movies_info['average_rating'],
        movies_info['average_runtime'],
        movies_info['total_revenue'],
        movies_info['best_movie']['title'] if movies_info['best_movie'] else "Undefined",
        movies_info['best_movie']['rating'] if movies_info['best_movie'] else "Undefined",
        movies_info['worst_movie']['title'] if movies_info['worst_movie'] else "Undefined",
        movies_info['worst_movie']['rating'] if movies_info['worst_movie'] else "Undefined"
    ])

    # Definir los encabezados de la tabla
    headers = ["Año", "Total de Películas", "Rating Promedio", "Duración Promedio", "Ingresos Totales", 
               "Mejor Película", "Rating Mejor Película", "Peor Película", "Rating Peor Película"]
    
    print(tabulate(table, headers=headers, tablefmt="grid"))  
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]") 
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

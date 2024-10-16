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

    result = lg.req_1(control, title, original_language)
    
    if isinstance(result, dict):
        print("Detalles de la película:")
        print(f"Título: {result['original_title']}")
        print(f"Idioma original: {result['original_language']}")
        print(f"Duración: {result['duration']} minutos")
        
        # Mostrar la fecha de publicación, verificando si es válida
        if isinstance(result['release_date'], datetime):
            print(f"Fecha de publicación: {result['release_date'].strftime('%Y-%m-%d')}")
        else:
            print(f"Fecha de publicación: {result['release_date']}")
        
        print(f"Presupuesto: {result['budget']}")
        print(f"Ingresos netos: {result['revenue']}")
        print(f"Ganancia: {result['profit']}")
        print(f"Puntaje: {result['rating']}")
    else:
        print("Ninguna pelicula fue encontrada")
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
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

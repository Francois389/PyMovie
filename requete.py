import requests

def get_api_key():
    with open("api_key.txt") as f:
        return f.readline().strip()

def get_film_info(film_name):
    """
    Renvoie les informations d'un film à partir de son nom
    :param film_name: Le nom du film
    :return: Un JSON contenant les informations du film
    """
    api_key = get_api_key()
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={film_name}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    film_name = input("Enter a film name: ")
    film_info = get_film_info(film_name)
    print(film_info)
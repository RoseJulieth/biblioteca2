import requests

class APIRepository:
    BASE_URL = "https://poo.nsideas.cl/api/libros"

    # Obtener todos los libros desde la API
    def get_books_from_api(self):
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Lanza excepción si hay error
            return response.json()
        except requests.RequestException as e:
            print(f"Error al consultar la API: {e}")
            return None

    # Obtener un libro por ISBN
    def get_book_by_isbn(self, isbn: str):
        try:
            url = f"{self.BASE_URL}/{isbn}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error al consultar la API para ISBN {isbn}: {e}")
            return None


from infraestructure.connection import Connection
from models.book import Book
from typing import List

class BookRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    # Crear un libro
    def create_book(self, book: Book) -> int:
        sql = """
        INSERT INTO libros (titulo, autor, isbn, disponibilidad)
        VALUES (%s, %s, %s, %s)
        """
        self.__conn.execute(sql, (
            book.get_title(),
            book.get_author(),
            book.get_isbn(),
            book.is_available()
        ))
        self.__conn.commit()
        return self.__conn.get_last_row_id()

    # Obtener todos los libros
    def get_all_books(self) -> List[Book]:
        sql = "SELECT id, titulo, autor, isbn, disponibilidad FROM libros"
        self.__conn.execute(sql)
        results = self.__conn.fetchall()
        books = []
        for item in results:
            book = Book()
            book.set_id(item[0])
            book.set_title(item[1])
            book.set_author(item[2])
            book.set_isbn(item[3])
            book.set_availability(item[4])
            books.append(book)
        return books

    # Obtener un libro por ID
    def get_book_by_id(self, book_id: int) -> Book:
        sql = "SELECT id, titulo, autor, isbn, disponibilidad FROM libros WHERE id = %s"
        self.__conn.execute(sql, (book_id,))
        result = self.__conn.fetchone()
        if result:
            book = Book()
            book.set_id(result[0])
            book.set_title(result[1])
            book.set_author(result[2])
            book.set_isbn(result[3])
            book.set_availability(result[4])
            return book
        return None

    # Actualizar un libro
    def update_book(self, book: Book):
        sql = """
        UPDATE libros 
        SET titulo = %s, autor = %s, isbn = %s, disponibilidad = %s 
        WHERE id = %s
        """
        self.__conn.execute(sql, (
            book.get_title(),
            book.get_author(),
            book.get_isbn(),
            book.is_available(),
            book.get_id()
        ))
        self.__conn.commit()

    # Eliminar un libro
    def delete_book(self, book_id: int):
        sql = "DELETE FROM libros WHERE id = %s"
        self.__conn.execute(sql, (book_id,))
        self.__conn.commit()

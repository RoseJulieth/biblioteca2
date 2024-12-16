class Book:
    def __init__(self) -> None:
        self.__id = -1
        self.__title = ""
        self.__author = ""
        self.__isbn = ""
        self.__availability = True

    # Métodos Getter y Setter para los atributos

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int):
        self.__id = id

    def get_title(self) -> str:
        return self.__title
    
    def set_title(self, title: str):
        self.__title = title

    def get_author(self) -> str:
        return self.__author
    
    def set_author(self, author: str):
        self.__author = author

    def get_isbn(self) -> str:
        return self.__isbn
    
    def set_isbn(self, isbn: str):
        self.__isbn = isbn

    def is_available(self) -> bool:
        return self.__availability
    
    def set_availability(self, availability: bool):
        self.__availability = availability

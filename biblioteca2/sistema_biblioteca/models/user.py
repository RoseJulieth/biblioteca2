import bcrypt

class User:
    def __init__(self) -> None:
        self.__id = -1
        self.__name = ""
        self.__username = ""
        self.__password = ""

    def get_id(self):
        return self.__id
    
    def set_id(self, id: int):
        self.__id = id

    def get_name(self):
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name

    def get_username(self):
        return self.__username
    
    def set_username(self, username: str):
        self.__username = username

    def get_password(self):
        return self.__password
    
    def set_password(self, password: str):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.__password = hashed.decode("utf-8")
    
    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.__password.encode("utf-8"))

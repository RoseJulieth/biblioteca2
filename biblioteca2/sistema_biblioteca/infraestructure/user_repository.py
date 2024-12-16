from infraestructure.connection import Connection
from models.user import User

class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_user(self, user: User):
        sql = "INSERT INTO usuarios (nombre, username, password) VALUES (%s, %s, %s)"
        self.__conn.execute(sql, (user.get_name(), user.get_username(), user.get_password()))
        self.__conn.commit()

    def get_user_by_username(self, username: str) -> User:
        sql = "SELECT id, nombre, username, password FROM usuarios WHERE username = %s"
        self.__conn.execute(sql, (username,))
        result = self.__conn.fetchone()
        if result:
            user = User()
            user.set_id(result[0])
            user.set_name(result[1])
            user.set_username(result[2])
            user._User__password = result[3]  # Asignación directa para evitar hashing redundante
            return user
        return None

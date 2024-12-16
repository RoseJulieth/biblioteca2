from infraestructure.connection import Connection
from models.loan import Loan
from typing import List

class LoanRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    # Crear un préstamo
    def create_loan(self, loan: Loan) -> int:
        sql = """
        INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo, fecha_devolucion)
        VALUES (%s, %s, %s, %s)
        """
        self.__conn.execute(sql, (
            loan.get_user_id(),
            loan.get_book_id(),
            loan.get_loan_date(),
            loan.get_return_date()
        ))
        self.__conn.commit()
        return self.__conn.get_last_row_id()

    # Obtener todos los préstamos
    def get_all_loans(self) -> List[Loan]:
        sql = "SELECT * FROM prestamos"
        self.__conn.execute(sql)
        results = self.__conn.fetchall()
        loans = []
        for item in results:
            loan = Loan()
            loan.set_id(item[0])
            loan.set_user_id(item[1])
            loan.set_book_id(item[2])
            loan.set_loan_date(item[3])
            loan.set_return_date(item[4])
            loans.append(loan)
        return loans

    # Actualizar préstamo (devolución)
    def update_loan_return(self, loan_id: int, return_date):
        sql = """
        UPDATE prestamos 
        SET fecha_devolucion = %s 
        WHERE id = %s
        """
        self.__conn.execute(sql, (return_date, loan_id))
        self.__conn.commit()

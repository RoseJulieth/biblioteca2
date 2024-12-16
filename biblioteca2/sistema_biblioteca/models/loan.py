from datetime import date

class Loan:
    def __init__(self) -> None:
        self.__id = -1
        self.__user_id = -1
        self.__book_id = -1
        self.__loan_date = date.today()
        self.__return_date = None

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int):
        self.__id = id

    def get_user_id(self) -> int:
        return self.__user_id
    
    def set_user_id(self, user_id: int):
        self.__user_id = user_id

    def get_book_id(self) -> int:
        return self.__book_id
    
    def set_book_id(self, book_id: int):
        self.__book_id = book_id

    def get_loan_date(self) -> date:
        return self.__loan_date
    
    def set_loan_date(self, loan_date: date):
        self.__loan_date = loan_date

    def get_return_date(self) -> date:
        return self.__return_date
    
    def set_return_date(self, return_date: date):
        self.__return_date = return_date

from infraestructure.mysqlconnection import MySQLConnection
from infraestructure.user_repository import UserRepository
from infraestructure.book_repository import BookRepository
from infraestructure.loan_repository import LoanRepository
from models.user import User
from models.book import Book
from models.loan import Loan
from credentials_db import host, user, password, database
import getpass
from datetime import date

# Configuración de la conexión
conn = MySQLConnection(host, user, password, database)
user_repo = UserRepository(conn)
book_repo = BookRepository(conn)
loan_repo = LoanRepository(conn)

# Inicio de sesión global
current_user = None

# Registro de Nuevo Usuario
def registrar_usuario():
    nombre = input("Ingrese el nombre completo: ")
    username = input("Ingrese el nombre de usuario: ")
    passwd = getpass.getpass("Ingrese la contraseña: ")

    new_user = User()
    new_user.set_name(nombre)
    new_user.set_username(username)
    new_user.set_password(passwd)
    user_repo.create_user(new_user)
    print("Usuario registrado exitosamente.\n")

# Inicio de Sesión
def iniciar_sesion():
    global current_user
    username = input("Ingrese su nombre de usuario: ")
    passwd = getpass.getpass("Ingrese su contraseña: ")

    user = user_repo.get_user_by_username(username)
    if user and user.verify_password(passwd):
        current_user = user
        print(f"\nBienvenido, {user.get_name()}!")
        menu_principal()
    else:
        print("\nAcceso denegado. Intente de nuevo.\n")

# Gestión de Libros (CRUD)
def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")

    new_book = Book()
    new_book.set_title(titulo)
    new_book.set_author(autor)
    new_book.set_isbn(isbn)
    new_book.set_availability(True)

    book_repo.create_book(new_book)
    print("Libro registrado exitosamente.\n")

def mostrar_libros():
    books = book_repo.get_all_books()
    print("ID\tTítulo\t\tAutor\t\tISBN\t\tDisponibilidad")
    for book in books:
        disponibilidad = "Disponible" if book.is_available() else "No disponible"
        print(f"{book.get_id()}\t{book.get_title()}\t{book.get_author()}\t{book.get_isbn()}\t{disponibilidad}")

def actualizar_libro():
    mostrar_libros()
    book_id = int(input("Ingrese el ID del libro a actualizar: "))
    titulo = input("Ingrese el nuevo título: ")
    autor = input("Ingrese el nuevo autor: ")
    isbn = input("Ingrese el nuevo ISBN: ")
    disponibilidad = input("¿Está disponible? (sí/no): ").lower() == "sí"

    book = book_repo.get_book_by_id(book_id)
    if book:
        book.set_title(titulo)
        book.set_author(autor)
        book.set_isbn(isbn)
        book.set_availability(disponibilidad)
        book_repo.update_book(book)
        print("Libro actualizado con éxito.")
    else:
        print("Libro no encontrado.")

def eliminar_libro():
    mostrar_libros()
    book_id = int(input("Ingrese el ID del libro a eliminar: "))
    book_repo.delete_book(book_id)
    print("Libro eliminado con éxito.\n")

# Préstamos de Libros
def registrar_prestamo():
    mostrar_libros()
    book_id = int(input("Ingrese el ID del libro a prestar: "))
    book = book_repo.get_book_by_id(book_id)

    if book and book.is_available():
        loan = Loan()
        loan.set_user_id(current_user.get_id())
        loan.set_book_id(book_id)
        loan.set_loan_date(date.today())
        loan_repo.create_loan(loan)
        book.set_availability(False)
        book_repo.update_book(book)
        print("Préstamo registrado con éxito.\n")
    else:
        print("El libro no está disponible.\n")

def registrar_devolucion():
    prestamos = loan_repo.get_loans_by_user_id(current_user.get_id())
    if not prestamos:
        print("No tiene préstamos pendientes.\n")
        return

    print("ID\tTítulo\tFecha Préstamo\tFecha Devolución")
    for prestamo in prestamos:
        libro = book_repo.get_book_by_id(prestamo.get_book_id())
        print(f"{prestamo.get_id()}\t{libro.get_title()}\t{prestamo.get_loan_date()}\t{prestamo.get_return_date() or 'Pendiente'}")

    prestamo_id = int(input("Ingrese el ID del préstamo a devolver: "))
    prestamo = loan_repo.get_loan_by_id(prestamo_id)

    if prestamo:
        prestamo.set_return_date(date.today())
        loan_repo.update_loan_return(prestamo_id, prestamo.get_return_date())

        libro = book_repo.get_book_by_id(prestamo.get_book_id())
        libro.set_availability(True)
        book_repo.update_book(libro)
        print("Devolución registrada con éxito.\n")
    else:
        print("Préstamo no encontrado.\n")

# Menú Principal
def menu_principal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Registrar Préstamo")
        print("2. Registrar Devolución")
        print("3. Gestión de Libros (CRUD)")
        print("4. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            registrar_devolucion()
        elif opcion == "3":
            gestion_libros()
        elif opcion == "4":
            print("Sesión cerrada.\n")
            menu_inicio()
            break

# Menú de Gestión de Libros
def gestion_libros():
    while True:
        print("\nGESTIÓN DE LIBROS (CRUD)")
        print("1. Registrar Libro")
        print("2. Mostrar Libros")
        print("3. Actualizar Libro")
        print("4. Eliminar Libro")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            break

# Menú de Inicio
def menu_inicio():
    while True:
        print("\n===== MENÚ DE INICIO =====")
        print("1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Salir del Sistema")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Gracias por usar el Sistema de Biblioteca. ¡Hasta luego!\n")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu_inicio()



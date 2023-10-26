from Banco import User
from Banco import Bank

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="banco_poo",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

print("=========== BANCO POO =======\n\n")

opciones = int(input("""Menu:
                     1- Registrar Usuario 
                     2 - Iniciar Sesión\n"""))



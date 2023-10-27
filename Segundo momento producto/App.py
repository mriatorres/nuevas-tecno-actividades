from Banco import Bank
from User import User
import mysql.connector

'''from getpass import getpass
from mysql.connector import connect, Error'''

'''try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="banco_poo",
    ) as connection:
        print(connection)
except Error as e:
    print(e)
'''

mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        passwd="password"
    )
mycursor = mydb.cursor()

'''mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)'''

print("=========== BANCO POO =======\n\n")

opciones = int(input("""Menu:
                     1- Registrar Usuario 
                     2 - Iniciar Sesión\n"""))

if opciones == 1:
    usuario = User( name = None,
                    age = None,
                    gender = None,
                    password= None
                    )
    usuario.registrar_usuario()
    opciones = int(input("""Menu:
                     1- Iniciar Sesión 
                     2 - Salir\n"""))
    if opciones == 1:
        usuario = User( name = None,
                    age = None,
                    gender = None,
                    password= None
                    )
        usuario.iniciar_sesion()
        


elif opciones == 2:
     usuario = User( name = None,
                    age = None,
                    gender = None,
                    password= None
                    )
     usuario.iniciar_sesion()

else:
     print("Escoja una opción valida")
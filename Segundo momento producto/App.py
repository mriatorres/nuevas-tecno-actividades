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

#Se crea un objeto de la clase User
usuario = User( name = None,
                age = None,
                gender = None,
                password= None
                )
#Se crea un objeto de la clase Bank
banco =   Bank( name = None,
                age = None,
                gender = None,
                password= None,
                amount=None,
                balance=None
                )


print("=========== BANCO POO =======\n\n")

opciones = int(input("""Menu:
                     1- Registrar Usuario 
                     2 - Iniciar Sesión\n"""))

if opciones == 1:
    usuario.registrar_usuario()
    opciones = int(input("""Menu:
                     1- Iniciar Sesión 
                     2 - Salir\n"""))
    if opciones == 1:
        usuario.iniciar_sesion()
        opciones = int(input('''Menu:
                    1- Retirar
                    2 - Depositar
                    3- Ver estado de la cuenta
                    '''))
        if opciones == 1:
            banco.withdraw()
        elif opciones == 2:
            banco.deposit()
        elif opciones == 3:
            banco.view_balance()
        else:
            print("Por favor, escoja una opción valida")
    
    elif opciones == 2:
         print("Gracias por utilizar nuestros servicios...")
    else:
         print("Por favor, escoja una opción valida")


elif opciones == 2:
     usuario.iniciar_sesion()
     opciones = int(input('''Menu:
                    1- Retirar
                    2 - Depositar
                    3- Ver estado de la cuenta
                    '''))
     if opciones == 1:
          banco.withdraw()
     elif opciones == 2:
          banco.deposit()
     elif opciones == 3:
          banco.view_balance()
     else:
        print("Por favor, escoja una opción valida")
    
     

else:
     print("Escoja una opción valida")
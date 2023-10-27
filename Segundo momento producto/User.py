#Clase Padre
class User():
      #van a ser encapsulados (_):
    def __init__(self, name, age, gender, password):
        self._name = name
        self._age = age
        self._gender = gender
        self._password = password
    
        #Se generan los Getters y los Setters
        @property
        def name(self):
            return self._name

        #SET
        @name.setter
        def name(self,name):
            self._name = name
        
        @property
        def age(self):
            return self._age

        #SET
        @age.setter
        def age(self,age):
            self._age = age

        @property
        def gender(self):
            return self._gender

        #SET
        @gender.setter
        def gender(self,gender):
            self._gender = gender

        @property
        def password(self):
            return self._password

        #SET
        @password.setter
        def password(self,password):
            self._password = password

        #Se generan los metodos
        #para registrar a los usuarios e imprimir el registro
    def registrar_usuario(self):
        name = input(f"Ingrese su nombre de usuario: ")
        age = input(f"Ingrese su edad: ")
        gender = input(f"Ingrese su genero: ")
        password = input(f"Ingrese su contraseña: ")

    def imprimir_registro(self):
        print(f"Nombre: {self._name} Edad: {self._age} Genero: {self._gender} Contraseña: {self._password}")
    
    def iniciar_sesion(self):
        name = input(f"Ingrese su nombre de usuario: ")
        password = input(f"Ingrese su contraseña: ")
        select_query = 'SELECT * FROM `Login_table` WHERE `username`'


        

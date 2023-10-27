from User import User

#Clase hija
class Bank(User):
    def __init__(self, name, age, gender, password, amount, balance):
        #llama atributos de la clase padre
        super().__init__(name, age, gender, password)
        self._amount = amount
        self._balance = balance

         #GET
        @property
        def amount(self, amount):
            return self._amount
        
        #SET
        @amount.setter
        def amount(self, amount):
            self._amount = amount

         #GET
        @property
        def balance(self, balance):
            return self._balance
        
        #SET
        @balance.setter
        def balance(self, balance):
            self._balance = balance

        #Se sobrescriben los metodos

    def registrar_usuario(self, name, password, age, gender):
         name = input(f"Ingrese su nombre de usuario: ")
         age = input(f"Ingrese su edad: ")
         gender = input(f"Ingrese su genero: ")
         password = input(f"Ingrese su contraseña: ")
         print("El usuario se ha registrado exitosamente con los siguientes datos : \n", "Nombre: ",self._name,", Edad: ",self._age,", Genero: ",self._gender)

        #Hacer un deposito a la cuenta
    def deposit (self):
        amount = int(input(f"Ingrese el monto a consignar: "))
        balance = int(amount + balance)
        print("El saldo de la cuenta ha sido actualizado : $", self._balance)

    def withdraw(self, amount):
        self.amount = amount
        if (self.amount > self.balance):
            print("Fondos insuficientes : Saldo disponible : $", self.balance)
        else: 
            self.balance = self.balance - self.amount
            print("El saldo de la cuenta ha sido actualizado : $", self.balance)
        
    def view_balance(self):
        self.show_details()
        print("El saldo de la cuenta ha sido actualizado : $", self.balance)
#Clase Padre
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Detalles Personales")
        print("")
        print("Nombre: ", self.name)
        print("Edad: ", self.age)
        print("Genero: ", self.gender)

#Case hija
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit (self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("El saldo de la cuenta ha sido actualizado : $", self.balance)

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
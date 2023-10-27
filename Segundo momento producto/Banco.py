from User import User

#Clase hija
class Bank(User):
    def __init__(self, name, age, gender, password, amount, balance, noCuenta):
        #llama atributos de la clase padre
        super().__init__(name, age, gender, password)
        self._amount = amount
        self._balance = balance
        self._noCuenta = noCuenta

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

         #GET
        @property
        def noCuenta(self, noCuenta):
            return self._noCuenta
        
        #SET
        @noCuenta.setter
        def noCuenta(self, noCuenta):
            self._noCuenta = noCuenta

        #Se sobrescriben los metodos

    def registrar_usuario(self):
            name = int(input(f"Ingrese su nombre de usuario: "))
            age = int(input(f"Ingrese su edad: "))
            gender = int(input(f"Ingrese su genero: "))
            password = int(input(f"Ingrese su contraseña: "))
            noCuenta=int(input(f"Ingrese el numero de su cuenta: "))

            mycursor.execute("""
            INSERT INTO usuario(user_name,user_age,user_gender,user_password,user_acc)
            VALUES(?,?,?,?)""", (name,age,gender,password,noCuenta))
            mydb.commit()
            print("El usuario se ha registrado exitosamente con los siguientes datos : \n", "Nombre: ",self._name,", Edad: ",self._age,", Genero: ",self._gender)
            for i in mycursor:
                print(i)
            

        #Hacer un deposito a la cuenta
    def deposit (self):
        account = int(input("Ingrese el numero de su cuenta: "))
        amount = float(input(f"Ingrese el monto a consignar: "))
        self.balance += amount
        #Insertar en la tabla
        mycursor.execute("""
        INSERT INTO account_table (user_acc, balance)
        VALUES(?)""", (account, amount))
        print("El monto consignado fue de : $", amount)
        for i in mycursor:
            print(i)

    def withdraw(self):
        account = int(input("Ingrese el numero de su cuenta: "))
        amount = float(input("Ingrese la cantidad a retirar : "))
        if self.balance >= amount:
            self.balance -= amount
            print("El monto retirado fue de : $", amount)
            mycursor.execute("""
            INSERT INTO account_table (user_acc, balance)
            VALUES(?,?)""",(account, amount))
            for i in mycursor:
                print(i)
        else: 
            self.balance = self.balance - self.amount
            print("Fondos insuficientes...")
        
    def view_balance(self):
        account = int(input("Ingrese el numero de su cuenta: "))
        mycursor.execute("""SELECT * FROM account_table WHERE user_acc=%s""",(account)
        )
        print("Saldo de la cuenta : $", self.balance)
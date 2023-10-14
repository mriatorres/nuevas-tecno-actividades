class Persona:
    def __init__(self, id, nombre, apellido, correo, contraseña):

        #van a ser encapsulados (_):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contraseña = contraseña

    #Se generan los Getters y los Setters
    #decorador:
    #es un GET
    @property
    def id(self):
        return self._id

    #SET
    @id.setter
    def id(self,id):
        self._id = id

    #GET
    @property
    def nombre(self):
        return self._nombre
    #SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # GET
    @property
    def apellido(self):
        return self._apellido

    # SET
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # GET
    @property
    def correo(self):
        return self._correo

    # SET
    @correo.setter
    def correo(self, correo):
        self._correo = correo

    # GET
    @property
    def contraseña(self):
        return self._contraseña

    # SET
    @contraseña.setter
    def contraseña(self, contraseña):
        self._contraseña = contraseña

    #Se generan los metodos
    #para registrar a los usuarios e imprimir el registro

    def registrar_usuario(self):
        id = input(f"Ingrese el id del usuario: ")
        nombre = input(f"Ingrese el nombre del usuario: ")
        apellido = input(f"Ingrese el apellido del usuario: ")
        correo = input(f"Ingrese el correo del usuario: ")
        contraseña = input(f"Ingrese la contraseña del usuario: ")

    def imprimir_registro(self):
        print(f"Id: {self._id} Nombre: {self._nombre} Apellido: {self._apellido} Correo: {self._correo} Contraseña: {self._contraseña}")
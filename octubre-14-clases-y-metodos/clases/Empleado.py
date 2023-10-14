from persona import Persona


class Empleado(Persona):
    def __init__(self, id, nombre, apellido, correo, contraseña,cargo, salario, tipo_contrato):
        #llama atributos de la clase padre
        super().__init__(id,nombre,apellido,correo,contraseña)
        self._cargo = cargo
        self._salario = salario
        self._tipo_contrato = tipo_contrato
        
    #GET
    @property
    def cargo(self, cargo):
        return self._cargo
    
    #SET
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    # GET
    @property
    def salario(self, salario):
        return self._salario

    # SET
    @salario.setter
    def cargo(self, salario):
        self._salario = salario

    # GET
    @property
    def tipo_contrato(self, tipo_contrato):
        return self._tipo_contrato

    # SET
    @tipo_contrato.setter
    def cargo(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato
    
    #Se sobre escriben los metodos
    
    def registrar_usuario(self):
        id = input(f"Ingrese el id del usuario: ")
        nombre = input(f"Ingrese el nombre del usuario: ")
        apellido = input(f"Ingrese el apellido del usuario: ")
        correo = input(f"Ingrese el correo del usuario: ")
        contraseña = input(f"Ingrese la contraseña del usuario: ")
        cargo = input(f"Ingrese el cargo del usuario: ")
        salario = input(f"Ingrese el salario del usuario: ")
        tipo_contrato = input(f"Ingrese el tipo de contrato del usuario: ")
        
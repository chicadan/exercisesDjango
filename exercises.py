#Ejercicio 1: MCD

#Ejercicio 2: MC


#Ejercicio 3: 

#Ejercicio 4

#Ejercicio 5

#Ejercicio 6 - 7 - 8

class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def nombre(self,nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni = nuevo_dni
    
    
    

class Cuenta:
    def __init__(self, titular, cantidad):
        super()
        self.titular = titular
        self.cantidad = cantidad

class CuentaJoven:
    def __init__(self,bonificacion):
        self.bonificacion = bonificacion

   # def titularValido(self):
   #     if self>18 & self < 25
   #         True
   #         else False

   # def retirarDinero(self):
   #     if titularValido(self)
   #     True


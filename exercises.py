
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
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nuevaEdad):
        if nuevaEdad > 18:
            self.__edad = nuevaEdad
        else:
            print("Eres menor de edad")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,nuevoDni):
        self.__dni = nuevoDni


    def mostrar(self):
        return( f"Nombre: {self.__nombre} Edad: {self.__edad} DNI: {self.__dni}")

    def esMAyorDeEdad(self):
        return self.__edad
    
    
    

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = (Persona)
        self.cantidad = cantidad



class CuentaJoven:
    def __init__(self,bonificacion):
        self.bonificacion = bonificacion

   # def titularValido(self):
   #     if self>18 & self < 25
   #         True
   #     else 
   #        False

   # def retirarDinero(self):
   #     if titularValido(self)
   #        True


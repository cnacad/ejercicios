python manageclass Cuenta(): # ejercicio 7
    def __init__(self,titular): 
        self.__titular = titular
        self.__cantidad= 0.0
                
    @property        # version de branch carlos 
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
        
    @property        
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter    
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        return self.__cantidad

    def ingresar(self,cantidadIngreso):
        if (cantidadIngreso>0):
            self.__cantidad = self.__cantidad+cantidadIngreso

    def retirar(self,cantidadRetiro):
        self.__cantidad=self.__cantidad-cantidadRetiro

class CuentaJoven(Cuenta): # ejercicio 8
    def __init__(self, titular, bonificacion):
        super().__init__(titular)
        self.__bonificacion = bonificacion    

    @property        
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter    
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self,edad):
        if (edad>=18 == edad<25):
            return True
        else:
            return False
    
    def retira_valido(self,titular,importe):
        if (titular==self.titular):
            super().retirar(importe)                

    def mostrar(self):
        return "Cuenta Joven",self.__bonificacion
                
                

class Zona:
    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, animales): 
        self._animales.append(animales)
    
    def cantidadAnimales(self): 
        return len(self._animales)  

    def getNombre(self): 
        return self._nombre

    def setNombre(self, nombre): 
        self._nombre = nombre

    def getUbicacion(self,): 
        return self._ubicacion

    def setUbicacion(self, ubicacion): 
        self._ubicacion = ubicacion

    def getZona(self): 
        return self._zonas

    def setZona(self, animales): 
        self._animales = animales
from zooAnimales.animal import Animal

class Pez(Animal):
	_listado = []
	salmones = 0
	bacalaos = 0

	def __init__(self,nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
		super().__init__(nombre, edad, habitat, genero)
		self._colorEscamas = colorEscamas
		self._cantidadAletas = cantidadAletas
		Pez._listado.append(self)

	@classmethod
	def crearSalmon(cls,nombre,edad,genero):
		Pez.salmones+=1
		return Pez(nombre,edad,"oceano",genero, "rojo", 6)

	@classmethod
	def crearBacalao(cls,nombre,edad,genero):
		Pez.bacalaos+=1
		return Pez(nombre,edad,"oceano", genero, "gris", 6)

	@classmethod
	def cantidadPeces(cls):
		return len(Pez._listado)

	def isColorEscamas(self):
		return self._colorEscamas

	def setColorEscamas(self,colorEscamas):
		self._colorEscamas = colorEscamas

	def getCantidadAletas(self):
		return self.cantidadAletas

	def setCantidadAletas(self,cantidadAletas):
		self._cantidadAletas = cantidadAletas

	
	def getListado(cls):
		return Pez._listado

	
	def setListado(cls,listado):
		Pez._listado = listado
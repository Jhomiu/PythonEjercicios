class Serie:
    def __init__(self,titulo="",temporadas=3,entregado=False,genero="",creador=""):
        self.titulo = titulo
        self.temporadas = temporadas
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

def entregar(serie1):  
	serie1.entregado = True

class Videojuego:
	def __init__(self,titulo="",horasEstimadas=10,entregado=False, genero="",compañia=""):
		self.titulo = titulo
		self.horasEstimadas = horasEstimadas
		self.entregado = entregado
		self.genero = genero
		self.compañia = compañia

	def entregarVideojuego(self, v):
		self.entregado = True


serie1 = Serie("Serie1", 2,False,"Drama", "creador1")
serie2 = Serie("Serie2", 4,True,"Terror", "creador2")
serie3 = Serie("Serie3", 1,False,"Comedia", "creador3")
serie4 = Serie("Serie4", 9 ,False,"Anime", "creador4")
serie5 = Serie("Serie5", 3,True,"Infantil", "creador5")


videojuego1 = Videojuego("Videojuego1", 250, False, "Tiros", "Compañia 1")
videojuego2 = Videojuego("Videojuego2", 100, True, "Multiplataforma", "Compañia 2")
videojuego3 = Videojuego("Videojuego3", 700, True, "Miedo", "Compañia 3")
videojuego4 = Videojuego("Videojuego4", 300, True, "Online", "Compañia 4")
videojuego5 = Videojuego("Videojuego5", 7000, False, "Survival", "Compañia 5")


entregar(serie1)
if serie1.entregado:
    	print("Serie entregada")

videojuego1.entregarVideojuego(videojuego1)
if videojuego1.entregado:
    	print("Videojuego entregado")

contSeries=0
contVideojuego=0

horasJuego=0
tempSeries=0
videojuegoMax = videojuego1
serieMax = serie1
listaSeries=[serie1,serie2,serie3,serie4,serie5]
listaJuegos=[videojuego1,videojuego2,videojuego3,videojuego4,videojuego5]

for i in listaSeries:
	if i.entregado == True:
		contSeries = contSeries + 1

	if i.temporadas > tempSeries:
		tempSeries = i.temporadas
		serieMax = i		

for i in listaJuegos:
	if i.entregado == True:
		contVideojuego = contVideojuego + 1

	if i.horasEstimadas > maxHorasJuego:
		maxHorasJuego = i.horasEstimadas
		videojuegoMax = i		

print("Series entregadas: " , contSeries)	
print("Juegos entregadas: " , contVideojuego)
print("Serie con mas temp:", serieMax.titulo)	
print("Videojuego con mas horas:", videojuegoMax.titulo)

import random
from random import choice

class Persona:
	def __init__(self, nombre="Sin nombre", edad=0, dni="", sexo='M', peso=0.0, altura=0.0):
		self.nombre = nombre
		self.edad = edad
		self.dni = dni
		self.sexo = sexo
		self.peso = peso
		self.altura = altura

def calcularImc(persona1):
	try:
		imc = (persona1.peso / persona1.altura**2)

		if (imc<18.5):
			print("Tiene infrapeso")
		if (imc>=18.5 and imc<25):
			print("Esta en su peso")
		if (imc >= 25):
			print("Tiene sobrepeso")
	except:
		print("Faltan datos")

def esMayorDeEdad(persona1): 
        if (persona1.edad>=18):
        	return True
        else:
        	return False	

def insertarSexo(): 
	sexo = input("Introduce sexo:")
	if sexo == 'H' or 'h':
		return sexo
	else:
		return 'M'

def toString(persona1): 
	print("Nombre:", persona1.nombre, "\nEdad:", persona1.edad, "\nDNI:", persona1.dni, "\nSexo:", persona1.sexo, "\nPeso:", persona1.peso,
	 "\nAltura:", persona1.altura,"\n\n")

def generarDni(): 
	num = random.randint(70000000,79999999)
	letra = choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	dni = str(num) + letra
	return dni

def ejecutar():
    nombre = input("Introduzca su nombre:")
    edad = int (input("Introduzca su edad:"))
    sexo = insertarSexo()
    altura = float (input("Introduzca su altura:"))
    peso = float (input("Introduzca su peso:"))
    dni1 = generarDni()
    dni2 = generarDni()
    persona1 = Persona(nombre,edad,dni1,sexo,peso,altura)
    persona2 = Persona(nombre,edad,dni2,sexo)
    persona3 = Persona()

    personas = [persona1,persona2,persona3]
    for i in personas:
        if esMayorDeEdad(i) == True:
            print ("Es mayor de edad")
        else:
            print ("Es menor de edad")
        toString(i)
        calcularImc(i)        

ejecutar()


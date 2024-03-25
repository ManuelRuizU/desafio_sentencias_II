""" 
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:
𝑉𝑒 = √2𝑔𝑟
Ve : corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s2].
r: Corresponde al radio del planeta en [m].

Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
"""
#import math
from math import sqrt


#paso 1
#capturar y almacenar dato ingresado por el usuario (por default el input lo almacena como string)
radio = input("Ingrese el radio en Kilómetros:\n")
#6371 -> "6371"

#paso 2
#transformar string a numero
radio = float(radio)# la funcion float(), transforma un string a float
#radio = float("6371") -> radio = 6371

#paso 3
#transformar kilometros a metros (multiplicar por 1000) 
radio = radio * 1000 # radio = 6371 * 1000 -> radio = 6371000

# paso 1 para g
#capturar y almacenar dato ingresado por el usuario
constante_gravitacional = input("Ingrese la constante gravitacional:\n")
#9.8 -> "9.8"
#paso 2
#transformar string a numero(float)
constante_gravitacional = float(constante_gravitacional)
#constante_gravitacional = float("9.8") -> constante_gravitacional = 9.8

#calculo formula 𝑉𝑒 = √2𝑔𝑟
multiplicacion = 2 * constante_gravitacional * radio

velocidad_escape = sqrt(multiplicacion)

print(f"La velocidad de Escape es {round(velocidad_escape,1)} [m/s]")


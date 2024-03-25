"""
i = 0
while i < 10:
    print(f"El valor de i es: {i}")
    i = i + 1 #incremento en 1
    
print("fuera del while")
"""
'''
import sys, time

print(sys.argv) #['dia7/bomba.py', '8']
print(sys.argv[0])
print(sys.argv[1])

i = int(sys.argv[1])

while i > 0:
    print(f"El valor de i {i}")
    time.sleep(1)#tiempo de espera 1 segundo
    i -= 1 #decrementando (restando 1)
    
    cant_notas = int(input("ingrese cantidad de notas"))
i = 0
suma_notas = 0
while i < cant_notas:
    nota = float(input(f"Ingresa tu {i+1} nota\n"))
    suma_notas = suma_notas + nota
    i += 1

print(f"el promedio de notas es: {round(suma_notas/cant_notas,2)}")
'''
import random

def juego_adivinanza():
    while True:
        numero_secreto = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 100
        intentos = 0
        max_intentos = 5  # Define el número máximo de intentos permitidos
        print (' ')
        print("¡Bienvenido al juego de adivinanzas!")
        print("Estoy pensando en un número entre 1 y 10. Adivina cuál es.")

        while intentos < max_intentos:
            intento = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if intento < numero_secreto:
                print("El número que estoy pensando es más grande.")
            elif intento > numero_secreto:
                print("El número que estoy pensando es más pequeño.")
            else:
                print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
                break

        if intento != numero_secreto:
            print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {numero_secreto}.")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            break

juego_adivinanza()


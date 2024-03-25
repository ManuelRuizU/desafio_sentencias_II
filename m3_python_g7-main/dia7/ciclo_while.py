""" 
while condicion:
    #codigo a ejercutar

"""
#import getpass
"""
password = input("Ingrese su contraseña:\n")

while len(password) < 6:
    password = input("Ingrese su contraseña con largo superior o igual a 6 caracteres:\n")

while password != "Hola Mundo":
    password = input("no adivinaste la contraseña, Ingrese su contraseña nuevamente:\n")

print("\nContraseña correcta!")
#resto del programa
print("Fin del programa")
"""
#Iteracionde n veces
i = 0
while i < 10:
    print(f"El valor de i es: {i}")
    i += 1 #i = i + 1 #incremento en 1

    
print(f"fuera del while, valor de i= {i}")

"""
while True:
    print("acciones infinitas")
    if condicion:
    else:
        break #salir del bucle
"""

saludo = "Hola"
saludo = saludo + " Mundo"
print(saludo)
saludo += "chao"
print(saludo)

"""
CONDICIONAL IF    
Si se cumple la condicion, entonces se ejecuta el codigo

if condicion:
    #Codigo a ejecutar si es verdadero
elif  otra_condicion:
    #Codigo a ejecutar si la primera no se cumple
else:
    #codigo por defaul si no se ejecutan otros codigos

"""
edad = int(input("Ingrese su edad: \n"))
if edad == 18 :
    print("Tienes 18 años")
elif  edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n")

if edad == 0:
    print("La edad es cero")
elif edad%2 == 0:
    print("La edad es par")
else:
    print("La edad es impar")

print("\n")
print("Fin del programa")

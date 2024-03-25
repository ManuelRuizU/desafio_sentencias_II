import sys,random

numero_buscar = int(sys.argv[1])

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) #desordenar la lista, permanentemente
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print(f"El numero {numero_buscar} se encontro en la posición {posicion}")
        break
    else:
        print(f"El numero no se encuentra en la posición {posicion}\n")    

print("Fin del programa")

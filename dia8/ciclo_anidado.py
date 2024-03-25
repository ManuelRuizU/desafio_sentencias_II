
#en este caso el range toma como primer numero 1 y termina en el 10
#for numero in range(1,11):
#    print(f'5 * {numero} = {5 * numero}')

# En los ciclos anidados se resuelven desde adentro hacia afuera.
for tabla in range(1,11):
    print(f'tabla del numero: {tabla}') # este for me da el numero de la tabla
    
    for numero in range(1,11): # Este for me da el numero por el cual se multiplica el num de la tabla
        print(f'{tabla} * {numero} = {tabla * numero}')
    print(' ')    
        
        
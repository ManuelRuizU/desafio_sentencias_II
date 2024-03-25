
# en for siempre considera el 0 por lo tanto si mi range es(10)
#el ciclo for comienza en 0 y termina en 9
for i in range (10):
    print (i)
    
    

datos_personales = {
    'Nombre': 'Manuel',
    'Apellido': 'Ruiz',
    'Edad':  51
}
print(' ')

#imprime las claves
for clave in datos_personales:
    print(clave)
print(' ')

#imprime los valores
for clave in datos_personales:
    print(datos_personales[clave])
print(' ')  

for clave, valor in datos_personales.items():
    print(f'clave: {clave} - valor: {valor}')
print(' ')

#imprime claves y valores
for clave, valor in datos_personales.items():
    print(f'{clave}: {valor}')
print(' ')

#Break termina el ciclo donde yo le indico, en este caso le indique 3
numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:
    print(numero)
    if numero == 3:
        break
print(' ')    


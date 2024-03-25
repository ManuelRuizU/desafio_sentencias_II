# Claudio Mendez
#Juan Torres
#Diego Larenas
#Manuel Ruiz

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)
print('*****************')
#Transformarlo en un List Comprehension

resultado_filtrado = [elemento for elemento in a if elemento >= 1000]
print(resultado_filtrado)

print('*****************')

minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
bien_o_mal = ['Bien' if tiempo < 90 else 'Mal' for tiempo in minutos]
print(bien_o_mal)

print('*****************')

# Transformando segundos a minutos
segundos = [100, 50, 1000, 5000, 1000, 500]
minutos = [segundo // 60 for segundo in segundos]
print (minutos)

print('*****************')



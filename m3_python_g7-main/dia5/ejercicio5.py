edad = 27

#¿Juan es mayor de edad?
print(edad >= 18)#True
print(edad < 18) #False

#¿Juan se graduó del colegio antes de los 18 años?
edad_graduacion_colegio = 17
print(edad_graduacion_colegio < 18)#True
print(edad_graduacion_colegio == 18)#False
print(edad_graduacion_colegio > 18)#False
print(edad_graduacion_colegio >= 18)#False  -> Mayor O Igual

#¿Juan NO tiene 4 años de experiencia laboral?
experiencia_laboral= 4
print(experiencia_laboral != 4)#False
print(experiencia_laboral == 4)#True
print(experiencia_laboral < 4 or experiencia_laboral > 4)#False

#¿Juan tiene hijos?
numero_hijos=0
print(numero_hijos > 0)#False
print(numero_hijos < 1)#True
print(numero_hijos == 0)#True
print(numero_hijos != 0)#False

nombre= "Mijail"

#comparacion entre = y ==
me_llamo_juan= (nombre == "Juan") #False; True



""" edad > 18 y duracion_pololeo > 0

P = edad > 18 
Q = duracion_pololeo > 0
R = 

p = T ; p = F
q = T ; q = F
r = T ; r = F

cantidad de combinaciones
2^2= 4
2^3= 8

y (and) -> SI AMBAS SON VERDADERAS, EL RESULTADO ES VERDADERO (TRUE)

P   Q   AND
V   V =  V *
V   F =  F
F   V =  F
F   F =  F
------------------------------------
o (or) -> SI AMBOS SON FALSOS, TODO EL RESULTADO ES FALSO

P   Q   OR
V   V = V 
V   F = V 
F   V = V 
F   F = F *

"""
#soy estudiante y ingreso a clases todos los dias
# True and False -> False

#me gusta comer fruta o me gusta comer verduras 
# True or True   => True
# False or False => False

#ser o no ser
#True or False => True
#False or True => True 

"""
-[-(-V)]=
-[-(F)]
-[V]
False
""" 

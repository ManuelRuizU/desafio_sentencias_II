
from string import ascii_lowercase
from getpass import getpass

# Solicitar al usuario que ingrese la contraseña a adivinar
password = getpass("Ingrese la contraseña a adivinar: ")
password = password.lower()  # Convertir la contraseña a minúsculas

intentos = 0

# Recorrer cada letra de la contraseña
for i, letra in enumerate(password):
    if letra not in ascii_lowercase:
        print("La contraseña contiene caracteres no válidos.")
        quit()  # Salir del programa si la contraseña contiene caracteres no válidos
    
    intentos += 1  # Incrementar el contador de intentos
    
    # Calcular los intentos necesarios para llegar a la letra actual
    intentos_letra_actual = ord(letra) - ord('a') + 1
    
    # Restar 1 a los intentos ya que la primera comparación no cuenta como intento
    intentos += intentos_letra_actual - 1

# Mostrar el número total de intentos
print(f"Se adivinó la contraseña en {intentos} intentos.")




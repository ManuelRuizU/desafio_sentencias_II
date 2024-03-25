
print("Primeros auxilios")

# Definimos la funcion primeros auxilios.
def primeros_auxilios():
    #  útilizamos 'upper()' para normaliza las respuestas del usuario
    respuesta = input("¿Responde a estímulos? (SI/NO): ").upper()
    if respuesta == "SI":
        print("Valorar llevarlo al hospital.")
        return
    elif respuesta == "NO":
        print("Abrir vía aérea.")
        respira = input("¿Respira? (SI/NO): ").upper()
        if respira == "SI":
            print("Permitir posición de suficiente ventilación.")
            return
        elif respira == "NO":
            print("Administrar 5 ventilaciones y llamar a la ambulancia.")
            signos_vida = input("¿Signos de vida? (SI/NO): ").upper()
            if signos_vida == "SI":
                print("Reevaluar la espera de la ambulancia.")
                return
            elif signos_vida == "NO":
                print("Administrar compresiones torácicas.")
                ambulancia_llego = input("¿Llegó la ambulancia? (SI/NO): ").upper()
                if ambulancia_llego == "SI":
                    print("La ambulancia ha llegado. Fin del programa.")
                    return
                elif ambulancia_llego == "NO":
                    print("Reevaluar los signos de vida.")
                    primeros_auxilios()

primeros_auxilios()
print("Fin del programa")


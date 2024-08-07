# JUEGO DEL AHORCADO
import random
def obtener_palabra() -> str:
    lista_palabras = ["perro","gato","elefante","tiburon","mono"]
    return random.choice(lista_palabras)


def mostrar_avanze(palabra_secreta, letras_adivinadas) -> str: #p, y, t
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"  
    return adivinado          
           

def juego_ahoracodo():
    palabra_secreta = obtener_palabra()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("Bienvenido al Juego del Ahorcado")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_avanze(palabra_secreta, letras_adivinadas))

    while not juego_terminado:
        letra_usuario = input("Ingrese una letra, por favor:").lower()

        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Por favor ingrese un valor valido!!")

        elif letra_usuario in letras_adivinadas:
            print("Ya haz usado esta letra, intenta con otra.")    

        else:
            letras_adivinadas.append(letra_usuario)

            if letra_usuario in palabra_secreta:
                print(f"Bien la letra se encuentra")
            else:
                intentos -= 1
                print("La letra no se encuentra")
                print(f"La cantidad de intentos que te quedan son {intentos}")  


        progreso = mostrar_avanze(palabra_secreta, letras_adivinadas)
        print(progreso + "\n")

        if intentos == 0:
            print("HAZ PERDIDO, JUEGO FINALIZADO!!\n")
            break
        
        if "_" not in progreso:
            print("HAZ GANADO, JUEGO FINALIZADO!!")
            print(f"La palabra completa es {palabra_secreta}\n")
            juego_terminado = True
        
            
    finalizacion = input(f"Ha finalizado el juego , deseas jugar otra vez? (SI/NO)\n").upper()
    if finalizacion == "SI":
        juego_ahoracodo()
    elif finalizacion == "NO":
        print("Hasta la proxima!")
    return


juego_ahoracodo()
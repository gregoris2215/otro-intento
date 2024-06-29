import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        intentos += 1
        try:
            numero_adivinado = int(input("Adivina el número (entre 1 y 100): "))
            if numero_adivinado < numero_secreto:
                print("Muy bajo!")
            elif numero_adivinado > numero_secreto:
                print("Muy alto!")
            else:
                print(f"Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()

import random


def guess_number(x):

    print("========================")
    print("  ¡Welcome to the game! ")
    print("========================")
    print("You need to guess the number produced by computer.")

    random_number = random.randint(1, x) # numero aleatorio entre 1 y x 

    prediction = 0 # se define esta variable como 0 para que el numero aleatorio no vaya a caer ya que tenemos un rango que empieza desde 1 hasta x

    while prediction != random_number:# por que while y no for, necesitamos que se repita una secuencia de instrucciones un numero no especifico de veces
        prediction = int(input(f"Guess number between 1 and {x}: "))# recordar poner int para que sea numero y no caracter

        if prediction < random_number:
            print("Try again. This number is lower")
        elif prediction > random_number:
            print("Try again. This number is greater")

    print(f"¡Congrats! You guess the number {random_number}, you're great.")


guess_number(10)
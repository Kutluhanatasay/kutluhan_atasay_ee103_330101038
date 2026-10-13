from secret_number import secretNum


x = float(input("ENTER X to guess the secret number"))

if x < secretNum :

    print("guess is low")

elif x > secretNum :

    print("guess is too high")

elif x == secretNum :

    print(secretNum) 


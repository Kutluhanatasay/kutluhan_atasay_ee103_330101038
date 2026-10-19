from secret_number import secretNum


for i in range(5):
    
    x = float(input("ENTER X to guess the secret number"))

    if x < secretNum :

        print("guess is low")

    elif x > secretNum :

        print("guess is high")

    elif x == secretNum :
        print(secretNum)
        break
else:

    while True:
        print ("error: all five chances are wrong!")

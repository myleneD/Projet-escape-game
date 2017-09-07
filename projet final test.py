from time import sleep


mdp = [6504]


response = False

while response is not True:
    respond = []
    print("Quel est le code ?")
    for i in range(1):
        ask = input()
        respond.append(ask)
    if mdp == respond:
        print("Bravo, vous avez reussi, la bombe est desamorcer, vous pouvez sortir !")
        response = True
    else:
        print("Mauvais mot de passe, veuillez reesayer !")

sleep(60)

import random
#Created by Wolf

print("Hello ! Let's play a game =) \nType numbers 0 - 9 and try to find the treasure.")

def main():
    finePartita = False
    Campo = list(range(0, 10))
    posizionedeltesoro = random.randint(0, 9)
    tentativi = 3

    while finePartita == False:
        print(*Campo)
        userInput = int(input("Your Guess ? : "))

        if Campo[userInput] == '_':
            print("You already tried this field")
            continue
        elif userInput != posizionedeltesoro:
            Campo[userInput] = '_'
            tentativi = tentativi - 1
            if tentativi == 0:
                print("You lost beacause you don't have any more attempts")
                finePartita = True
            else:
                print("You suck ! Try again !!")
            continue
        else:
            Campo[userInput] = '*'
            print("Congratulations, you won !")
            finePartita = True
            break
main()
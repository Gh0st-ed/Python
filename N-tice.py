import random

print("Ahoj, zahrajeme si hru =). \nZkus hádát známé značky automobilů.\nMáte pouze 3 pokusy.")

myTuple = tuple(("Ford", "BMW", "Audi", "Ferrari", "Lamborghini"))
tries = 3
gameOver = False
word = random.choice(myTuple)

print(word)

while gameOver == False:
  if tries == 0:
    print("Už nemáš pokusy")
    gameOver = True

  print(*myTuple)

  userInput = str(input(""))
  if userInput == word:
    print("Uhadl jsi to")
    gameOver = True
  else:
    tries -= 1
    print("Špatně, už máš jen {} pokusů".format(tries))



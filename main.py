import random
import webbrowser

def credits():
  print("Coder: sgysh3nka")
  webbrowser.open("https://github.com/sgysh3nka")

def dice():
  random_dice = random.randinat(1, 31)
  print(random_dice)

def vibor():
  print("1. Dice.")
  print("2. Credits.")
  vibor228 = input('')
  if vibor228 == "1":
    dice()
    vibor()
  elif vibor228 == "2":
    credits()
    vibor()
  else:
    print("404")
    vibor()

vibor()

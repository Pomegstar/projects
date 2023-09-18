import random
while True:
    x = print(random.randrange(1,6))  #randrange or randint
    z = input("Do you want to roll again?: ")
    if z == "yes":
        continue
    else:
      print("you are exited.")
      break
while True:
  x = input("Do you want to play this game? if you want write 'yes'... ")
  if x == "yes":
    y  = input("where are you want to go?: 'jungle' or 'cave' ")
    if y == "jungle":
      z = input("you will see the tiger on the jungle. you heve to do fight with the tiger. \n"
                "or you have to go away. do yo want to fight?: ")
      if z == "yes":
        print("Great, You are brave!")
      else:
        print("you are a cowerd.")
    else:
      w = input("you will see a bear on the cave. Do you want to go there?: ")
      if w == "yes":
        e = input("The bear can be angry and there is a possibility to eat you. \n"
                  "do you want to fight with the bear?: ")
        if e == "yes":
          print("you are really a brave.")
        else:
          print("you will be alive.")
  else:
    print("you are exited.")
    break
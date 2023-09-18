while True: 
    x = input("enter your name: ")
    y = input("what class do you read in? ")
    z = input("what are you doing now? ")
    i = input("what is your hobby? ")
    s = input("what is your favourite food? ")
    w = input("do you wan to exit?: ")
    if x == "zakia":
     print(f"{x} is a good girl,\n"
      f"she reads in {y}, \n"
      f"she is {z}ing now, \n"
       f"her hobby is {i}, \n"
       f"{x}'s favourite food is {s} ")
    elif x == "nazmul":
       print(f"{x} is a good boy,\n"
        f"he reads in {y}, \n"
        f"he is {z}ing now, \n"
        f"his hobby is {i}, \n"
        f"{x}'s favourite food is {s} ")
    else:
       print(f"My servant name is {x}, \n"
       f"he/she reads in {y}, \n"
       f"he/she is {z}ing now, \n"
       f"his/her hobby is {i}, \n"
       f"{x}'s favourite food is {s} ")
    if w == "yes":
        break
    else:
        continue



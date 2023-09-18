import random
x = random.randrange(1,10)
m = random.randrange(1,20)
dm = random.randrange(1,40)
cm = random.randrange(1,80)
fn = random.randrange(1,160)

while True:
    y = int(input("guess a number from 1-10: "))
    if y > x:
        print("your guessing number is too high.")
    elif x > y:
        print("your guessing number is too low.")
    else:
        print("Congratulation! your guess is right.")
        i = input("Do you want to go the next level? ")
        if i == "yes":
            while True:
              y = int(input("guess a number from 1-20: "))
              if y > m:
                print("your guessing number is too high.")
              elif m > y:
                print("your guessing number is too low.")
              else:
                print("Congratulation! your guess is right.")
                i = input("Do you want to go the next level? ")
                if i == "yes":
                   while True:
                     y = int(input("guess a number from 1-40: "))
                     if y > dm:
                      print("your guessing number is too high.")
                     elif dm > y:
                      print("your guessing number is too low.")
                     else:
                      print("Congratulation! your guess is right.")
                      i = input("Do you want to go the next level? ")
                      if i == "yes":
                        while True:
                          y = int(input("guess a number from 1-80: "))
                          if y > cm:
                            print("your guessing number is too high.")
                          elif cm > y:
                            print("your guessing number is too low.")
                          else:
                            print("Congratulation! your guess is right.")
                            i = input("Do you want to go the next level? ")
                            if i == "yes":
                              while True:
                                 y = int(input("guess a number from 1-160: "))
                                 if y > fn:
                                   print("your guessing number is too high.")
                                 elif fn > y:
                                   print("your guessing number is too low.")
                                 else:
                                   print("Congratulation! your have finished all the level")
                                  
                                   raise SystemExit
                            else: 
                              raise SystemExit

                      else:
                       raise SystemExit

                else:
                  raise SystemExit                

        else:
          break
 
        
contact = {}
 
def showContact():
    print("your contact is", contact.items())
    print("name \t contact")
    for key in contact:
        print("{} \t {}", format(key, contact.get(key)))

while True:
    x =  int(input("1. add new contact: \n"
             "2. search the contact: \n"
             "3. display the contact: \n"
             "4. edit contact: \n"
             "5. delete contact: \n"
             "6. exit\n"      
             "choose one from the avobe. write (1-6) which one you want."))
    if x == 1:
        name = input("enter the name of the number: ")
        number = input("enter the number: ")
        contact[name] = number
    elif x == 2:
        y = input("which name do you want to search: ")
        if y in contact:
          print(f"your searched number is {contact[y]}")
        else:
            print("your name is not found.")
    elif x == 3:
        if not contact:
            print("your contact is empty")
        else:
            showContact()
    elif x == 4:
        c = input("which number do you want to edit: ")
        if c in contact:
          number = input("give the new number: ")
          contact[c] = number
          showContact()
        else:
            print("your name is not found.")
    elif x == 5:
        f = input("which number do you want to delete?: ")
        if f in contact:
            k = input("Are you sure? yes or no: ")
            if k == "yes":
             contact.pop(f)
            showContact()
        else:
            print("your number is not found.")
    else:
        break

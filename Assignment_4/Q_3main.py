age = 0,

for a in age:
    a = int(input("Enter Your Age "))

    if a <= 3 :
        print("The ticket is free for you.")

    elif a > 3 and a <= 12 :
        print("Your ticket charges are $10.")

    elif a >12 :
        print("Your ticket charges are $15.")
        
    else:
        print ("Sorry ,you are not allowed")
import random
num = random.randrange(1,30)
chances = ["1st guess ","2nd guess","3rd guess"]

print("You have three chances to guess the number generated by computer between 1 to 30 \n")

for a in chances:
   
    gnum = int(input("Guess the Number "))
    
    if num != gnum:
        if num > gnum:
            print("\nGiven number is less than the hidden number.")
            print(a, "is over\n")
        if num < gnum:
            print("\nGiven number is greater than the hidden number.")
            print(a, "is over\n")
if num == gnum:
        print("\nYou have done this it",a)
        print("Congratulations, Your guess is correct.")
        print("Yeah You Won \n")
if num != gnum:      
    print("\nYou Lost, no more chances left\nHidden number is ",num)
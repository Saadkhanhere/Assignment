def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

fact = factorial(8) 
print("Factorial of inserted number is: ", fact
     )
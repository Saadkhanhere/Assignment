def check_prime(pnum):
    if pnum > 1:
        for p in range(2, pnum): 
            if pnum % p == 0:
                print(pnum, " is not a Prime Number")
                print(p,"x",pnum//p, " = ",pnum)
                break
            else:
                print(pnum, " is a Prime Number")
                break
                
    else:
        print(pnum, " is not a Prime Number")
        
chnum = int(input("Enter a number to Check whether the number is prime or not: "))
check_prime(chnum)
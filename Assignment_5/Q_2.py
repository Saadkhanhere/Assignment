def str_test(s):
    d = {"UP" : 0, "LOW" : 0}
    for b in s:
        if b.isupper():
            d["UP"]+=1
        elif b.islower():
            d["LOW"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No: Upper-Case = ", d["UP"])
    print("No: lower-Case = ", d["LOW"])
Ostr = str(input("Enter String to Check the  No. of upper and lower case letters: ")) 
str_test(Ostr)
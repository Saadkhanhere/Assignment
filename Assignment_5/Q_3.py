nolist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def enum(num):
    for lst in num:
        if lst%2 == 0:
            print(lst)
        else:
            pass
print("Even Numbers are: ")
enum(nolist)
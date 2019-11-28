'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Function to print sum 
def returnSum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  
# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
print("Dictionary", dict)
print("Sum :", returnSum(dict)) 
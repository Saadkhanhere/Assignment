'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Let's create a dictionary, the functional way 

# Create your dictionary class 
class my_dictionary(dict): 

	# __init__ function 
	def __init__(self): 
		self = dict() 
		
	# Function to add key:value 
	def add(self, key, value): 
		self[key] = value 

# Main Function 
dict_obj = my_dictionary() 

dict_obj.add(1, 'Geeks') 
dict_obj.add(2, 'forGeeks') 

print(dict_obj) 


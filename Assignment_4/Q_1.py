person = {
        "First Name" : "Saad",
        "Last Name" : "Khan",
        "Age" : 22,
        "City" : "Hyderabad"
}
for key, value in person.items():
    print("Friend's " + key + ": " + str(value)) 
print("\n",person,"\n")

person["Qualification"] = "Undergraduate"
print(person,"\n")


person["Qualification"] = "Post Graduate"
print(person,"\n")

del person["Qualification"]
print(person)
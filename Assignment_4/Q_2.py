cities = {
    "Karachi" : {
        
        "Country" : "Pakistan",
        "Population" : "14.91 million",
        "Fact" : "City of Lights "
        
        },
    "Kuala Lumpur" : {
            
        "Country" : "Malaysia",
        "Population" : "32.66 million",
        "Fact" : "It is worst known for traffic. "
        
        },
    "Ankara" : {
            
        "Country" : "Turkey",
        "Population" : "5.024 Million",
        "Fact" : "Ankara is roughly 4 times the size of Greater Manchester."
        
        }
}
for key in cities.keys():
    print("City Name: ",key,"\n")
    
    for ekey,evalue in cities[key].items():
        print(ekey+" of "+key+": "+evalue)
    print("\n")
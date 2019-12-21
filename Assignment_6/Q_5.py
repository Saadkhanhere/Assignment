class Car:
    def __init__(self, name, brand, model, color, doors):
        self.name = name
        self.brand = brand
        self.model = model
        self.color =  color
        self.doors = doors
    def printCar(self):
        print(self.name,self.brand, self.model, self.color, self.doors)
    def drive(self):
        print(self.name, "is now being drived.")
    def stop(self):
        print(self.name, "is stopped.")
car1 = Car("Mehran", "Suzuki", "2009", "White", 4)
car2 = Car("Lamborghini", "Lambo", "2010", "Blue", 2)
car3 = Car("Fe22", "Ferrari", "2011", "Green", 4)
car4 = Car("Corolla", "Toyota", "2012", "Red", 2)
car5 = Car("Vitz", "Honda", "2019", "Gray", 4)
car5.printCar()
car1.stop()
car4.drive()
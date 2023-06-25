from Car import Car

Car.color = "black"


car1 = Car("Ford","Fusion",2012,30.5)
car2 = Car("Honda", "Civic", 2010, 32.5)

car1.wheels = 3

print("Car 1 has "+str(car1.wheels)+"Wheels")
print("We have two "+car1.color+" & "+car2.color+"   color cars")

car1.start()
car2.stop()
class Car:


    wheels = 4
    color = "red"

    def __init__(self,Make,Model,Year,Mileage):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Mileage = Mileage

    def start(self):
        print("Car "+self.Model+" Started!!")

    def stop(self):
        print("Car "+self.Model+" Stopped!!")
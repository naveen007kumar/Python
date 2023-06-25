## MultipleInheritance and Overriding

class Biryani:
    def biryani(self):
        print("Spicy food!!!!")

class Restaurant():
    def biryani(self):
        print("This place has biryani.")  #Overriding

class Hyderabad(Restaurant, Biryani):
    def temp(self):
        print("In every hyderabad restaurant has Biryani.")

bir = Biryani()
res = Restaurant()
hyd = Hyderabad()

hyd.biryani()

print()
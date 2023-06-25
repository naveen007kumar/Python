class Biryani:

    def biryani(self):
        print("Spicy food!!!!")

class Restaurant(Biryani):

    def biryani(self):
        print("This place has biryani.")

class Hyderabad(Restaurant):

    def temp(self):
        print("In every hyderabad restaurant has Biryani.")


bir = Biryani()
res = Restaurant()
hyd = Hyderabad()

hyd.biryani()
res.biryani()
bir.biryani()
## Multi-Level Inheritance and method chaining

class Biryani:

    def biryani(self):
        print("Spicy food!!!!")


class Restaurant(Biryani):

    def restaurant(self):
        print("This place has biryani.")
        return self
    def dhaba(self):
        print("Dhaba has no biryani.")
        return self
    def hotel(self):
        print("Hotel has biryani.")
        return self

class Hyderabad(Restaurant):

    def temp(self):
        print("In every hyderabad restaurant has Biryani.")


bir = Biryani()
res = Restaurant()
hyd = Hyderabad()

hyd.biryani()
res.biryani()
bir.biryani()

### method chaining
hyd.restaurant().dhaba().hotel()
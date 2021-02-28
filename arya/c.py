class Car:

    def __init__(self, w, m, f):
        self.wheel = w
        self.model = m
        self.fuel = f
    
    def print(self):
        print("This car is a", self.model)

    def fuel_cal(self, distance):
        print('Use ', (distance * 7)/100, 'Liter')
         

p = Car(4, 'pride', 7)
p.print()
p.fuel_cal(4521)
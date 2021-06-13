class Car:

    # (d)ouble (under)line
    def __init__(self, m, c):
        self.model = m
        self.company = c
    # method
    def sound(self):
        print(f'{self.model} says "GHUMGHUM"')


n = Car('Nissan', 'Saipa')
n.sound()
p = Car('Paykan', 'IranKhordo')
p.sound()
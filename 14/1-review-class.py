class Car:
    # model, company => attribute
    model = None
    company = None

print(Car)

p = Car()  # p=> instance, object    Car => class
print(p.company)
p.company = 'IranKhordro'
p.model = 'Peykan'
print(p.company)

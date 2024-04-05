from car import Car

car_1 = Car("BMW", "M3", 2022, "blue")
car_2 = Car("Audi", "RS6", 2023, "red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print("---------------------")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)



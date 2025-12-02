cars = ['bmw', 'audi', 'toyota', 'subacu']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subacu']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subacu']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subacu']
print(cars)
cars.reverse()
print(cars)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper)
    else:
        print(car.title)

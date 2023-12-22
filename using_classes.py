

# instance = CLASS(params ...)
# instance.method(params ...)
# CLASS.method(params ...)

cities = list()
cities.append('Denver')
cities.append('Albany')
cities.append('Miami')
cities.insert(1, 'Seattle')
print(f"cities: {cities}\n")

cities = cities + ['Spokane', 'Milwaukee']
print(f"cities: {cities}\n")

print(f"cities[3]: {cities[3]}\n")

#  CLASS[index-or-key]

class Dog:
    def bark(self):
        print("woof woof")


d1 = Dog()
d2 = Dog()
d3 = Dog()

d1.bark()
d2.bark()


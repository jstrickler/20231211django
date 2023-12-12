stuff = list()
colors = ['blue', 'pink', 'orange', 'yellow']
animals = []   # empty list

values = [5, "wombat", 87.8, None, ['spam', 'ham'], 'asparagus']

cities = []   
cities.insert(0, 'Alexandria')
print(f"cities: {cities}")
cities.append('St. Paul')
print(f"cities: {cities}")
cities.append('Durham')
cities.append('Harrisburg')
print(f"cities: {cities}")
cities.insert(2, "Tacoma Park")
cities.insert(0, "Columbia")
print(f"cities: {cities}")
more_cities = ['Fairfax', 'Clifton', 'Springfield']
cities.extend(more_cities)
print(f"cities: {cities}")

#   LIST.insert(pos, obj)    LIST.append(obj)    LIST.extend(iterable)

del cities[4]
print(f"cities: {cities}")

print(f"cities.index('Clifton'): {cities.index('Clifton')}")

cities.remove('Clifton')
print(f"cities: {cities}")

city = cities.pop()  # remove last element
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]    LIST.remove(value)    obj = LIST.pop()    obj = LIST.pop(pos)
print(f"cities[0]: {cities[0]}")
print(f"cities[4]: {cities[4]}")
print(f"cities[-1]: {cities[-1]}")
print(f"cities[len(cities)-1]: {cities[len(cities)-1]}")

#  slice -->       LIST[START:STOP]    LIST[:STOP]   LIST[START:]  LIST[START:STOP:STEP]

#  START is INclusive
#  STOP  is EXclusive

print(f"cities[0:3]: {cities[0:3]}")
print(f"cities[:3]: {cities[:3]}")

print(f"cities[2:4]: {cities[2:4]}")

person = "James Madison"
print("This made him", person[6:9])
print(f"person[:5]: {person[:5]}")

print(f"person[0:5:2]: {person[0:5:2]}")






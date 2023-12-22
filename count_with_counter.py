from collections import Counter


with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()

food_counter = Counter(foods)
print(food_counter)
print()
print(food_counter.most_common(3))

print(f"food_counter['sausage']: {food_counter['sausage']}")



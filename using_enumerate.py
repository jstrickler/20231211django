colors = ["red", "blue", "green", "yellow", "brown", "black"]

for color in colors:
    print(color)
print('-' * 60)

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)
print(list(enumerate(colors)))
print()
for i, color in enumerate(colors, 100):
    print(f"{i} {color}")
print()



colors = ["red", "blue", "green", "yellow", "brown", "black"]
nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

print(len(colors), len(nums))
print(min(colors), min(nums))
print(max(colors), max(nums))
print(sorted(colors), sorted(nums))
print(sum(nums))
print()

rcolors = reversed(colors)   #  ITERATOR (magic generator object)
print(rcolors)
for color in rcolors:  # one-time use
    print(color)
print()

reversed_colors = list(reversed(colors))
print(f"reversed_colors: {reversed_colors}\n")

combo = zip(colors, nums)
print(f"combo: {combo}")

for color, num in combo:
    print(color, num)
print()

print(list(zip(colors, nums)))






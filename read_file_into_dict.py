from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        #  DICT[key] = value
        knight_info[name] = title, color, quest, comment

pprint(knight_info)
print()

for knight, data in knight_info.items():
    print(knight, data)
print('-' * 60)

for knight, data in knight_info.items():
    print(data[0], knight)
print('-' * 60)


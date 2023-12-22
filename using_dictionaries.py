d1 = dict()
print(f"d1: {d1}")
capitals = {'NC': 'Raleigh', 'VA': 'Richmond', 'PA': 'Harrisburg'}
d3 = {}

capitals['MD'] = 'Annapolis'
capitals['DE'] = 'Dover'

print(f"capitals: {capitals}")
print(f"capitals.keys(): {capitals.keys()}")
print(f"capitals.values(): {capitals.values()}")

del capitals['DE']  # delete element with key 'DE'

capitals['WA'] = 'Seattle'
# time passes ...

capitals['WA'] = 'Olympia'

print(f"len(capitals): {len(capitals)}")

print(f"capitals['NC']: {capitals['NC']}")

print(f"'MD' in capitals: {'MD' in capitals}")
print(f"'CA' in capitals: {'CA' in capitals}")

# print(f"capitals['ND']: {capitals['ND']}")
print(f"capitals.get('MD'): {capitals.get('MD')}")
print(f"capitals.get('ND'): {capitals.get('ND')}")
print(f"capitals.get('ND', 42): {capitals.get('ND', 42)}")

print(f"capitals.setdefault('ND', 'Bismarck'): {capitals.setdefault('ND', 'Bismarck')}")
print(f"capitals: {capitals}")
print()

# for KEY, VALUE in DICT.items():
for state, capital in capitals.items():
    print(state, capital)
print()

for state, capital in sorted(capitals.items()):
    print(state, capital)
print()

for state, capital in sorted(capitals.items(), key=lambda e: (e[1], e[0])):
    print(state, capital)
print()










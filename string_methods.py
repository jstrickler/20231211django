person = "Taylor Swift"

print(f"'ay' in person: {'ay' in person}")

t_count = person.count('t')
print(f"t_count: {t_count}")

print(f"person.lower(): {person.lower()}")
print(f"person.upper(): {person.upper()}")

print(f"person.lower().count('t'): {person.lower().count('t')}")
print(f"person.replace('Swift', 'Momsen'): {person.replace('Swift', 'Momsen')}")

print(f"person.replace(' Swift', ''): {person.replace(' Swift', '')}")

old_file_name = "wombat.py"
new_file_name = old_file_name.removesuffix('.py') + '.txt'
print(f"new_file_name: {new_file_name}")

print(f"person.startswith('Taylor'): {person.startswith('Taylor')}")
print(f"person.startswith('Tom'): {person.startswith('Tom')}")

data = "     1234565       "


print(f"data: {data}")

print('|' + data + '|')
print('|' + data.strip() + '|')
print('|' + data.lstrip() + '|')
print('|' + data.rstrip() + '|')

print(f"person: {person}")
print(f"person.find('Swift'): {person.find('Swift')}")
print(f"person.find('Slow'): {person.find('Slow')}")

parts = person.split()
print(f"parts: {parts}")

data = "fee:fi:fo:fum"
parts = data.split(':')
print(f"parts: {parts}")

d = 'spam|ham|toast'
print(f"d.split('|'): {d.split('|')}")
print(d.split('|'))









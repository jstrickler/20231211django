fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"f0: {f0}\n")

# LIST = [VALUE for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('p')]
print(f"f3: {f3}\n")

foods = ['spam', 'spam', 'spam', 'toast', 'spam', 'spam', 'spam', 
         'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 
         'spam', 'ham', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs']

no_spam = [food for food in foods if food != 'spam']
print(f"no_spam: {no_spam}\n")

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

n1 = [n ** .5 for n in nums if n > 300]
print(f"n1: {n1}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [(p[1], p[-1]) for p in people]
print(f"dobs: {dobs}\n")

fruit_gen = (f.upper() for f in fruits)
print(f"fruit_gen: {fruit_gen}")

for fruit in fruit_gen:
    print(fruit)
print()





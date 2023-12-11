"""
String demo

This is a demonstration of how strings work in Python
"""
# the different string syntax types
s1 = "spam\n"
print(f"len(s1): {len(s1)}")
#  \n \r \t    \f \b  \???
s2 = 'spam\n'
print(f"len(s2): {len(s2)}")
s3 = """spam\n"""
s4 = '''spam\n'''  # triple-coated

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from dogs
where breed = "English Shepherd"
order by name, owner
limit 10
"""

s5 = r"spam\n"  # raw string  does not treat \ specially
print(f"len(s5): {len(s5)}")
print(f"s5: {s5}")
print(f"s1: {s1}")
print("done")

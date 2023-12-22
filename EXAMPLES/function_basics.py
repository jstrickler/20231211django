import os

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, Django world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()
print(get_hello())
print()

#       param
def sqrt(num):  # Function takes exactly one argument
    return num ** .5

#       arg
m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print(f"m is {m:.3f} n is {n:.3f}")

def rectangle_area(side1, side2=None):
    return side1 * (side2 if side2 else side1)

print(rectangle_area(5, 8))
print(rectangle_area(6))

def find_lines(search_term, *file_paths):
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(file_name, raw_line.rstrip())

find_lines('bird')
print()

find_lines('bird', '../DATA/parrot.txt')
print()

find_lines('bird', '../DATA/parrot.txt', '../DATA/alice.txt', '../data/words.txt')
print()

#  print(a, b, c, sep=":", end=" ")


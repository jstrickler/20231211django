import sys

print(f"sys.argv: {sys.argv}")
print(f"sys.argv[0]: {sys.argv[0]}")

celsius = float(sys.argv[1])

fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))


import sys

print(f"sys.argv: {sys.argv}\n")

print("Program name:", sys.argv[0])

animal = sys.argv[1]  # First command line parameter
print(f"animal: {animal}")


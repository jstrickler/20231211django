person = "Taylor Swift"
city = "New York"
value = 25.323839039393

print(person, city, value)
print("done")
#          positional | named 
print(person, city, value, sep=":")
print(person, city, value, sep="")
print(person, city, value, sep=", ")

print(person, end=" ")
print(city, end="--")
print(value, end=" ")
print("done")

print(person, city, value, sep=" ", end="\n")

s = f"{value:.3f}"
print(s)

print(city, person)
print(f"{city}: {person}")


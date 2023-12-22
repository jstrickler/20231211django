
numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
        # could put code here
    except ZeroDivisionError as err:
        print(f"uh-oh, when y = {y}, {err}")
    else:  # no exceptions raised
        total += quotient  # Only if no exceptions were raised
print(total)

TARGET_LETTER = 's'

count = 0

with open('DATA/words.txt') as words_in:
    for word in words_in:
        if word.startswith(TARGET_LETTER):
            count += 1

print(f"{count} words start with '{TARGET_LETTER}'")


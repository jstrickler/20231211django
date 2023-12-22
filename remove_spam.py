
input_file_name = 'DATA/breakfast.txt'
output_file_name = 'nonspam.txt'
spam_file_name = 'spam.txt'

foods = []

with open(input_file_name) as breakfast_in:
    with open(output_file_name, 'w') as nonspam_out: # open 'nonspam.txt'
        with open(spam_file_name, 'w') as spam_out:  # open 'spam.txt'
            for raw_line in breakfast_in:
                line = raw_line.rstrip()
                if line == 'spam':
                    spam_out.write(raw_line)  # write to 'spam.txt'
                else:
                    nonspam_out.write(raw_line)  # write to 'nonspam.txt'
print(foods)

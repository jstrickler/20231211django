from pprint import pprint

FILE_PATH = 'DATA/knights.txt'

def main():
    info = read_data()
    pretty_print(info)
    print('-' * 60)
    print_data(info)
    print('-' * 60)
    print_titles(info)


def read_data():
    knight_info = {}

    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            #  DICT[key] = value
            knight_info[name] = title, color, quest, comment
    return knight_info

def pretty_print(info):
    pprint(info)
    print()

def print_data(info):
    for knight, data in info.items():
        print(knight, data)

def print_titles(info):
    for knight, data in info.items():
        print(data[0], knight)

main()
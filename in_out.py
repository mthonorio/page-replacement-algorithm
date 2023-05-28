import struct
import operator


def open_file(fileName):
    try:
        with open(f'./{fileName}', 'r') as f:
            lines = f.readlines()
        lines = [int(line.strip()) for line in lines]   # Remove \n from each line
        number_of_pages = lines.pop(0)

        return number_of_pages, lines
    except FileNotFoundError:
        exit()

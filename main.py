from fifo import fifo
from otm import optimal
from LRU import LRU

file_path = "tests/example1.txt"

if __name__ == '__main__':
    fifo(file_path)
    optimal(file_path)
    LRU(file_path)

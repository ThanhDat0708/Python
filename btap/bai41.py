# Bai 41: Doc n dong cuoi cung cua tap tin
from collections import deque


def read_last_lines(filename, line_count):
    with open(filename, "r", encoding="utf-8") as file:
        for line in deque(file, maxlen=line_count):
            print(line, end="")


read_last_lines("test.txt", 2)

# Bai 50: Doc ngau nhien mot dong tu tap tin
import random


def random_line(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    return random.choice(lines) if lines else ""


print(random_line("test.txt"))

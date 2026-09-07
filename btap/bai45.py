# Bai 45: Dem so lan xuat hien cua cac tu trong tap tin
from collections import Counter


def word_count(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return Counter(file.read().split())


print("So lan xuat hien cua cac tu:", word_count("test.txt"))

# Bai 53: Dem so tu trong tap tin van ban
from pathlib import Path

def count_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
    data = data.replace(",", " ").replace(".", " ")
    return len(data.split())


words_file = Path(__file__).parent / "words.txt"
print(count_words(words_file))

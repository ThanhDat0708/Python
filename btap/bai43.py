# Bai 43: Tim tu co do dai lon nhat trong tap tin van ban

def longest_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()

    if not words:
        return []

    longest_length = len(max(words, key=len))
    return [word for word in words if len(word) == longest_length]


print(longest_words("test.txt"))

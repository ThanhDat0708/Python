# Bai 49: Ket hop tung dong tu hai tap tin
with open("abc.txt", "r", encoding="utf-8") as first_file, open(
    "test.txt", "r", encoding="utf-8"
) as second_file:
    for first_line, second_line in zip(first_file, second_file):
        print(first_line.rstrip("\n") + second_line.rstrip("\n"))

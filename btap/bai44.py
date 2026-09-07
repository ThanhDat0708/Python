# Bai 44: Dem so dong trong tap tin van ban

def line_count(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)


print("So dong cua tap tin la:", line_count("test.txt"))

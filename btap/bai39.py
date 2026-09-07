# Bai 39: Doc n dong dau tien cua tap tin

def read_first_lines(filename, line_count):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines()[:line_count]:
            print(line, end="")


read_first_lines("test.txt", 2)

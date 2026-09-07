# Bai 40: Them noi dung vao cuoi tap tin

def append_to_file(filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write("Python Exercises\n")
        file.write("Java Exercises\n")


append_to_file("abc.txt")

with open("abc.txt", "r", encoding="utf-8") as file:
    print(file.read())

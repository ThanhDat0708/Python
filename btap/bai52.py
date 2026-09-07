# Bai 52: Xoa ky tu xuong dong khoi tap tin

def remove_newlines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.rstrip("\r\n") for line in lines]


print(remove_newlines("test.txt"))

# Bai 47: Ghi cac gia tri cua danh sach vao tap tin
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

with open("abc.txt", "w", encoding="utf-8") as file:
    for color in colors:
        file.write(color + "\n")

with open("abc.txt", "r", encoding="utf-8") as file:
    print(file.read())

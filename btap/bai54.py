# Bai 54: Doc noi dung cac tap tin van ban vao danh sach
import glob

content_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        content_list.append(file.read())

print(content_list)

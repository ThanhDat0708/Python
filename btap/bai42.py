# Bai 42: Doc tung dong cua tap tin va luu vao danh sach

def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content_list = file.readlines()
    print(content_list)
    return content_list


read_lines("test.txt")

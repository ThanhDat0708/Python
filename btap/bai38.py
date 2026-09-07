 # Bai 38: Doc va hien thi toan bo noi dung tap tin
from pathlib import Path

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


read_file(Path(__file__).with_name("test.txt"))

# Bai 46: Tinh kich thuoc tap tin theo byte
import os


def file_size(filename):
    return os.path.getsize(filename)


print("Dung luong tap tin theo byte:", file_size("test.txt"))

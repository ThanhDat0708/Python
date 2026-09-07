# Bai 51: Kiem tra mot tap tin dang mo hay dong
file = open("abc.txt", "r", encoding="utf-8")
print("Tap tin dang mo:", not file.closed)
file.close()
print("Tap tin da dong:", file.closed)

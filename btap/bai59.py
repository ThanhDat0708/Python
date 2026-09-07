# Bai 59: Tim gia tri lon nhat va nho nhat theo phan tu thu hai

def max_min_values(class_students):
    maximum = max(class_students, key=lambda item: item[1])[1]
    minimum = min(class_students, key=lambda item: item[1])[1]
    return maximum, minimum


class_students = [
    ("V", 62),
    ("VI", 68),
    ("VII", 72),
    ("VIII", 70),
    ("IX", 74),
    ("X", 65),
]

print("Danh sach cac tuple ban dau:")
print(class_students)
print("Ket qua:", max_min_values(class_students))

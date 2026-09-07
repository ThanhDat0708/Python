# Bai 37: Xoa cac phan tu cua danh sach trong tu dien
items = {
    "C1": [10, 20, 30],
    "C2": [20, 30, 40],
    "C3": [12, 34],
}

print("Tu dien ban dau:")
print(items)

for values in items.values():
    values.clear()

print("Ket qua:")
print(items)

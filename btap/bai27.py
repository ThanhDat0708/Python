# Bai 27: Sap xep danh sach tuple theo phan tu thu hai giam dan
items = [("item1", 12.20), ("item2", 15.10), ("item3", 24.5)]
print(sorted(items, key=lambda item: item[1], reverse=True))

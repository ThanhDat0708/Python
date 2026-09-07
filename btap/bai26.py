# Bai 26: Xoa cac tuple rong khoi danh sach
items = [(), (), ("",), ("a", "b"), ("a", "b", "c"), ("d",)]
items = [item for item in items if item]
print(items)

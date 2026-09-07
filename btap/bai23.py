# Bai 23: Thay gia tri cuoi cung cua moi tuple bang 100
items = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result = [item[:-1] + (100,) for item in items]
print(result)

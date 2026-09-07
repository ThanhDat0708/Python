# Bai 6: Loai bo cac phan tu o vi tri 0, 4, 5
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
colors = [color for index, color in enumerate(colors) if index not in (0, 4, 5)]
print(colors)

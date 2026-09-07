# Bai 57: Tinh tong cac so duong va tong cac so am
numbers = [2, 4, -6, -9, 11, -12, 14, -5, 17]

negative_numbers = [number for number in numbers if number < 0]
positive_numbers = [number for number in numbers if number >= 0]

print("Danh sach ban dau:", numbers)
print("Tong cac so am:", sum(negative_numbers))
print("Tong cac so duong:", sum(positive_numbers))

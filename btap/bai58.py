# Bai 58: Tim cac so chia het cho 19 hoac 13
numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

result = [number for number in numbers if number % 19 == 0 or number % 13 == 0]

print("Danh sach ban dau:", numbers)
print("Cac so chia het cho 19 hoac 13:", result)

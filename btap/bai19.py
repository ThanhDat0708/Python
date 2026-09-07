# Bai 19: Them mot phan tu vao tuple
numbers = (4, 6, 2, 8, 3, 1)
numbers = numbers + (9,)
print(numbers)

numbers = numbers[:5] + (20, 25, 30) + numbers[5:]
print(numbers)

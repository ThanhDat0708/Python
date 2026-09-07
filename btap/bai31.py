# Bai 31: Xoa phan tu duoc chi dinh khoi mot tap hop
num_set = set([0, 1, 2, 3, 4, 5])

print("Tap hop ban dau:", num_set)

print("Xoa phan tu co gia tri 4:")
num_set.discard(4)
print(num_set)

print("Xoa phan tu co gia tri 5:")
num_set.discard(5)
print(num_set)

print("Xoa phan tu co gia tri 2:")
num_set.discard(2)
print(num_set)

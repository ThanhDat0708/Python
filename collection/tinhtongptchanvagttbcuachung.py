lst_a = []
n = int(input("Nhap kich thuoc danh sach: "))
# nhập danh sách
for i in range(n):
    tmp = int(input(f"Nhập phần tử thứ {i}: "))
    lst_a.append(tmp)

b = [x for x in lst_a if x % 2 == 0]
len_b = len(b)

if len_b > 0:
    s = sum(b)
    print(f"Tổng số chẵn: {s}, Trung bình: {s/len_b}")
else:
    print("Không có số chẵn nào")
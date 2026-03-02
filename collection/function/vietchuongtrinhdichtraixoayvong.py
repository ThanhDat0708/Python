def dich_trai(lst: list, k: int) -> list:
    k2 = k % len(lst)  # Đảm bảo k không vượt quá độ dài của danh sách
    if k2 == 0:
        return lst[k2::] + lst[:k2]
    else:
        return lst
list_a = [8, 20, 4, 2, 5]
list_b = dich_trai(list_a, 2)
print(list_b)
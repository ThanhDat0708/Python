# Bai 7: Kiem tra hai danh sach co phan tu chung hay khong

def has_common_data(first_list, second_list):
    return any(item in second_list for item in first_list)


print(has_common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(has_common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

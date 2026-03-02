def thongtin_sv():
    ten = input("Nhập tên sinh viên: ")
    lop = input("Nhập lớp: ")
    diem = float(input("Nhập điểm: "))
    return {"ten": ten, "lop": lop, "diem": diem}
def ds_sv():
    n = int(input("Nhập số lượng sinh viên: "))
    lst_sv = []
    for i in range(n):
        print(f"Nhập thông tin cho sinh viên thứ {i + 1}:")
        sv = thongtin_sv()
        lst_sv.append(sv)
    return lst_sv
def sinh_vien(sv):
    print(f"Tên:{sv['ten']},Lớp:{sv['lop']},Điểm:{sv['diem']}")
    
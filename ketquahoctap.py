a = float(input("Điểm môn thứ nhất: "))
b =  float(input("Điểm môn thứ hai: "))
c =  float(input("Điểm môn thứ ba: "))
if  a < 0 or b < 0 or c < 0:
    print("Vui lòng nhập điểm đúng đi ní.")
else:
    ket_qua = (a + b + c) / 3
    print(f"Kết Quả:{ket_qua}")

if ket_qua >= 0 and ket_qua <4:
    print(f"Kết Quả:{ket_qua} Yếu.")
elif ket_qua >= 4 and ket_qua < 6:
    print(f"Kết Quả:{ket_qua} Trung Bình.")
elif ket_qua >=6 and ket_qua < 8:
    print(f"Kết Quả:{ket_qua} Khá.")
else:
    print(f"Kết Quả:{ket_qua} Giỏi.")

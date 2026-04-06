from sympy import symbols, Implies
from sympy.logic.inference import satisfiable

# ==========================================
# PHẦN 1: ĐỊNH NGHĨA KÝ HIỆU & LUẬT (HÌNH THỨC)
# ==========================================

# 1. Định nghĩa các ký hiệu mệnh đề (P, Q, R)
# Đây là các ký hiệu toán học, chưa có giá trị True/False
P, Q, R = symbols('P Q R')

# 2. Biểu diễn các luật (Rules)
# Luật 1: "P -> Q" (Nếu P thì Q)
rule1 = Implies(P, Q)

# Luật 2: "Q -> R" (Nếu Q thì R)
# Thêm luật này để có thể suy ra R từ P
rule2 = Implies(Q, R)

print(f"Luật 1: {rule1}") # In ra: Luật 1: Implies(P, Q)
print(f"Luật 2: {rule2}") # In ra: Luật 2: Implies(Q, R)

# ==========================================
# PHẦN 2: XÂY DỰNG CƠ SỞ TRI THỨC (KB) & SỰ THẬT
# ==========================================

# 3. Định nghĩa sự thật (Fact): P là đúng
# Trong SymPy, sự thật được đưa vào KB dưới dạng ký hiệu P
fact_P = P

# 4. Tạo Cơ sở tri thức (KB) chứa tất cả các luật và sự thật
# KB = (P -> Q) AND (Q -> R) AND (P)
KB = rule1 & rule2 & fact_P
print(f"Cơ sở tri thức: {KB}")

# ==========================================
# PHẦN 3: SUY DIỄN LOGIC (INFERENCE)
# ==========================================

# 5. Kiểm tra tính thỏa mãn của KB & Tìm mâu thuẫn (Resolution)
# Ta dùng phương pháp PHẢN CHỨNG: Giả sử R là Sai (~R) và tìm mâu thuẫn.
result = satisfiable(KB & ~R)

# Nếu 'result' là False, nghĩa là (KB & ~R) dẫn đến mâu thuẫn.
# Do đó, giả sử R sai là vô lý -> R phải ĐÚNG.

print("-" * 20)
if result is False:
    print("Kết luận: R là ĐÚNG (True)")
else:
    print("Kết luận: Không đủ tri thức để suy ra R")
    # result có thể là một dict chứa các gán giá trị làm thỏa mãn KB.
    print(f"Các trường hợp thỏa mãn KB: {result}")

# Bai 56: Ghi cac chu cai tieng Anh vao tap tin theo nhom 3 ky tu
import string
from pathlib import Path

alphabet = string.ascii_uppercase
letters_per_line = 3
filename = Path(__file__).parent / "words1.txt"

lines = [
    alphabet[index:index + letters_per_line]
    for index in range(0, len(alphabet), letters_per_line)
]
filename.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(filename.read_text(encoding="utf-8"))

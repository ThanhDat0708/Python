# Bai 55: Tao 26 tap tin van ban A.txt den Z.txt
import string
from pathlib import Path

folder = Path(__file__).parent
for letter in string.ascii_uppercase:
    filename = folder / f"{letter}.txt"
    filename.write_text(letter + "\n", encoding="utf-8")

print("Da tao 26 tap tin tu A.txt den Z.txt")

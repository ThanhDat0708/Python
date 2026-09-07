# Bai 48: Sao chep noi dung mot tap tin sang tap tin khac
import shutil
from pathlib import Path

folder = Path(__file__).parent
source_file = folder / "test.py"
target_file = folder / "abc.py"

shutil.copyfile(source_file, target_file)
print("Da sao chep test.py thanh abc.py")

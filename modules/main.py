import io_handler
import processing
def main():
    dssv = io_handler.ds_sv()
    diem_max = processing.tim_sv_diem_max(dssv)
    diem_min =  processing.tim_sv_diem_min(dssv)
    print(f"sinh vien diem cao nhat:")
    io_handler.sinh_vien(diem_max)
    print(f"sinh vien diem nho nhat:")
    io_handler.sinh_vien(diem_min)
if __name__ == "__main__":
    main()
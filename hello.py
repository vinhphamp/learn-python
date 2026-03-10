class MonHoc:
    def __init__(self, maMH, tenMH, soTC):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTC = soTC

    def hienthiMH(self):
        print("Mã môn học: ", self.maMH)
        print("Tên môn học: ", self.tenMH)
        print("Số tín chỉ: ", self.soTC)

dsMH = []

def nhapDSMH():
    n = int(input("Nhập vào số lượng môn học: "))
    for i in range(n):
        maMH = input("Nhập vào mã môn học: ")
        tenMH = input("Nhập vào tên môn học: ")
        soTC = input("Số tín chỉ: ")
        mh = MonHoc(maMH, tenMH, soTC)
        dsMH.append(mh)

def hienthiDSMH():
    print("Danh sách môn học là: ")
    for i in range(len(dsMH)):
        print("Thông tin môn học: ", i + 1)
        dsMH[i].hienthiMH()

def main():
    nhapDSMH()
    hienthiDSMH()


main()    
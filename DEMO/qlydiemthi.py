'''
1. Vũ Trọng Phúc
2. Nguyễn Tiến Anh
3. Đỗ Thành Đạt
4. Lại Đức Anh
5. Mai Ngọc Dưỡng
'''
#Quản Lí Danh Sách
import libe.xu_ly_diem_thi
import os, csv
danh_sach=[]
khu_vuuc= [0.5,1,0]
i=0
__path="D:/16A2KHDL;THCS"
# Bắt đầu Chương Trình
print('Chương Trình Quản Lí Danh Sách')
while True:
    print('!!!Chọn lựa chọn của bạn!!!')
    print('1: Thêm sinh viên')
    print('2: In danh sách')
    print('3: Lưu file danh sách')
    print('4: Sắp xếp file danh sách')
    print('5: Tìm sinh viên có điểm tổng cao nhất')
    print('6: Xóa các sinh viên có tổng điểm dưới điểm tiêu chuẩn')
    chon=int(input('Nhập lựa chọn của bạn'))
    if chon ==1:
        libe.xu_ly_diem_thi.them_hoc_sinh(danh_sach)
    elif chon==2:
        libe.xu_ly_diem_thi.in_danh_sach(danh_sach)
    elif chon==3:
        libe.xu_ly_diem_thi.luu_file(__path,danh_sach)
        print('Đã lưu thành công!')
    elif chon==4:
        print('Danh sách ban đầu: ')
        libe.xu_ly_diem_thi.in_danh_sach(danh_sach)
        libe.xu_ly_diem_thi.sapxep(danh_sach)
    elif chon==5:
        libe.xu_ly_diem_thi.tim(danh_sach)
    elif chon==6:
        print('Danh sách sau khi xóa: ')
        libe.xu_ly_diem_thi.xoa(danh_sach)
    else:
        os.system('cls')
        print('Đã kết thúc chương trình!!!!!')
        break
    

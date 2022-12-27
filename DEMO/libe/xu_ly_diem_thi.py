import os, csv
def them_hoc_sinh(danh_sach):
    while True:
        mats=input('mã thí sinh: ')
        hoten=input('tên thí sinh: ')
        khuvuc=int(input('khu vực: '))
        diem1=float(input('điểm môn 1: '))
        diem2=float(input('điểm môn 2: '))
        diem3=float(input('điểm môn 3: '))
        diemkhuvuc= khu_vuuc[khuvuc-1]
        tongdiem= diem1 + diem2 + diem3 + diemkhuvuc
        danh_sach.append({'ma_sinh_vien':mats,'ten_thi_sinh':hoten,\
             'khu_vuc':khuvuc,'diem_mon_1': diem1,'diem_mon_2': diem2,\
        'diem_mon_3':diem3,\
             'tong_diem':tongdiem})
        tt=input('ban co muon tiep tuc them? (1:TT)')
        if tt!='1':
            break
    return 
def in_danh_sach(danh_sach):
    print('{:15}{:15}{:15}{:15}{:15}{:15}'.format('mã sinh viên','tên thí sinh','khu vực','điểm môn 1','điểm môn 2','điểm môn 3','tổng điểm'))
    for hd in danh_sach:
        print('{:15}{:15}{:1}{:17.5}{:16}{:15}'.format(hd['ma_sinh_vien'],hd['ten_thi_sinh'],hd['khu_vuc'],hd['diem_mon_1'],hd['diem_mon_2'],\
        hd['diem_mon_3'],hd['tong_diem']))
    return
def luu_file(_path,danh_sach):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f, delimiter= '\t').writerow(['mã sinh viên','tên thí sinh','khu vực','điểm môn 1','điểm môn 2','điểm môn 3','tổng điểm'])
        for hd in danh_sach:
            csv.writer(f, delimiter= '\t').writerow([hd['ma_sinh_vien'],hd['ten_thi_sinh'],hd['khu_vuc'],hd['diem_mon_1'],hd['diem_mon_2'],\
        hd['diem_mon_3'],hd['tong_diem']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
def sapxep(danh_sach):
    sorted_diem = sorted(danh_sach, key=lambda x: x['tong_diem'], reverse=True)
    print('Danh sách sau khi đã sắp xếp:')
    in_danh_sach(sorted_diem)
    return 
def tim(danh_sach):
    sorted_diem = sorted(danh_sach, key=lambda x: x['tong_diem'], reverse=True)
    print('{:15}{:15}{:15}{:15}{:15}{:15}'.format('mã sinh viên','tên thí sinh','khu vực','điểm môn 1','điểm môn 2','điểm môn 3','tổng điểm'))
    print('{:15}{:15}{:1}{:17.5}{:16}{:15}'.format(sorted_diem[0]['ma_sinh_vien'],sorted_diem[0]['ten_thi_sinh'],sorted_diem[0]['khu_vuc'],sorted_diem[0]['diem_mon_1'],sorted_diem[0]['diem_mon_2'],\
        sorted_diem[0]['diem_mon_3'],sorted_diem[0]['tong_diem']))
    return
def xoa(danh_sach):
    for i in range(len(danh_sach)):
        set= danh_sach[i-1]
        if set['tong_diem']<4:
            del(danh_sach[i])
    in_danh_sach(danh_sach)
    return
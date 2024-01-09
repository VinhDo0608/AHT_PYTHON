import json
from tabulate import tabulate

# Khởi tạo danh bạ trống
danh_ba = []


def print_menu():
    print("Chọn chức năng:")
    print("1. Thêm Liên hệ")
    print("2. Hiển thị Danh Bạ")
    print("3. Sửa Liên hệ")
    print("4. Xóa Liên hệ")
    print("5. Thoát chương trình")


# Đọc danh bạ từ tệp JSON khi ứng dụng khởi động
def doc_danh_ba():
    global danh_ba
    try:
        with open('danh_ba.json', 'r', encoding="utf-8") as file:
            danh_ba = json.load(file)
    except FileNotFoundError:
        danh_ba = []


# Lưu danh bạ vào tệp JSON
def ghi_danh_ba():
    with open('danh_ba.json', 'w', encoding="utf-8") as file:
        json.dump(danh_ba, file)


# Thêm một liên hệ mới vào danh bạ
def them_lien_he(ten, so_dien_thoai, dia_chi):
    global danh_ba
    lien_he_moi = {
        'Tên': ten,
        'Số điện thoại': so_dien_thoai,
        'Địa chỉ': dia_chi
    }
    danh_ba.append(lien_he_moi)
    ghi_danh_ba()


# Hiển thị toàn bộ danh bạ
def hien_thi_danh_ba():
    headers = ["STT", "Tên", "Số điện thoại", "Địa chỉ"]
    rows = []
    for index, lien_he in enumerate(danh_ba, start=1):
        rows.append([index, lien_he['Tên'], lien_he['Số điện thoại'], lien_he['Địa chỉ']])

    print(tabulate(rows, headers=headers, tablefmt="grid"))


# Sửa thông tin liên hệ dựa trên tên hoặc số điện thoại
def sua_lien_he(ten_cu, so_dien_thoai_cu, ten_moi, so_dien_thoai_moi, dia_chi_moi):
    global danh_ba
    for lien_he in danh_ba:
        if lien_he['Tên'] == ten_cu or lien_he['Số điện thoại'] == so_dien_thoai_cu:
            lien_he['Tên'] = ten_moi
            lien_he['Số điện thoại'] = so_dien_thoai_moi
            lien_he['Địa chỉ'] = dia_chi_moi
            ghi_danh_ba()
            break


# Xóa liên hệ dựa trên tên hoặc số điện thoại
def xoa_lien_he(ten, so_dien_thoai):
    global danh_ba
    for lien_he in danh_ba:
        if lien_he['Tên'] == ten or lien_he['Số điện thoại'] == so_dien_thoai:
            danh_ba.remove(lien_he)
            ghi_danh_ba()
            break


try:
    doc_danh_ba()
    while True:
        print_menu()
        choice = input("Chọn chức năng: ")

        if choice == '1':
            ten = input("Nhập tên: ")
            so_dien_thoai = input("Nhập số điện thoại: ")
            dia_chi = input("Nhập địa chỉ: ")
            them_lien_he(ten, so_dien_thoai, dia_chi)
            print("Thêm thành công!")
        elif choice == '2':
            hien_thi_danh_ba()
        elif choice == '3':
            ten_cu = input("Nhập tên cũ hoặc số điện thoại cũ: ")
            so_dien_thoai_cu = input("Nhập số điện thoại cũ: ")
            ten_moi = input("Nhập tên mới: ")
            so_dien_thoai_moi = input("Nhập số điện thoại mới: ")
            dia_chi_moi = input("Nhập địa chỉ mới: ")
            sua_lien_he(ten_cu, so_dien_thoai_cu, ten_moi, so_dien_thoai_moi, dia_chi_moi)
        elif choice == '4':
            ten = input("Nhập tên hoặc số điện thoại của liên hệ cần xóa: ")
            xoa_lien_he(ten, ten)
        elif choice == '5':
            print("Thoát chương trình")
            break
        else:
            print("Chọn chức năng không hợp lệ. Vui lòng chọn lại!")
except Exception as e:
    print(f"Lỗi! {e}")
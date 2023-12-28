class Nhanvien():
    def __init__(self,name,month,salary_per_day,day_of_working,coefficident):
        self.name = name
        self.month = month
        self.luong_co_ban = salary_per_day
        self.ngay_lam_viec = day_of_working
        self.he_so_luong = coefficident

    name = input("nhap ten cua ban: ")
    month = int(input("nhap so thang ban lam viec: "))
    salary_per_day = int(input("nhap luong co ban cua ban: "))
    day_of_working = int(input("nhap so ngay ban lam viec: "))
    coefficident = int(input("nhap he so luong cua ban: "))
    total_luong = salary_per_day / (day_of_working * coefficident )
    print("luong ma",name,"nhan duoc trong thang",month,"la", total_luong)
        
   
        
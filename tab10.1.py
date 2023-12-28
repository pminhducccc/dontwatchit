class Student():
    def __init__(self,name,diem1,diem2,diem3):
        self.name = name
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    name = input("nhap ten cua ban: ")
    diem1 = int(input("nhap diem cua ban: "))
    diem2 = int(input("nhap diem cua ban: "))
    diem3 = int(input("nhap diem cua ban: "))
    print(name,"diem trung binh cua ban la:",(diem1+diem2+diem3)/3)
   

    

    
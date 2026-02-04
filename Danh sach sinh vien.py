import json

class Student():
    def __init__(self, id, name, age, gpa):
        self.id = id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"{self.id:<5} {self.name:<20} {self.age:<5} {self.gpa:<5}"

class StudentManager():
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load_data()

    def load_data(self):
        self.students = []
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    s = Student(item['id'], item['name'], item['age'], item['gpa'])
                    self.students.append(s)
        except FileNotFoundError:
            print("Khong tim thay file!")

    def show_students(self):
        print("\n--- DANH SACH SINH VIEN ---")
        if not self.students:
            print("Danh sach trong.")
        else:
            print(f"{'ID':<5} {'Ten':<20} {'Tuoi':<5} {'GPA':<5}")
            print("-" * 40)
            for s in self.students:
                print(s)
        print("-" * 40)

    def add_student(self):
        print("\n--- THEM SINH VIEN ---")
        while True:
            try:
                s_id = int(input("Nhap ID: "))
                    
                for s in self.students:
                    if s.id == s_id:
                        print(f"Loi: ID {s_id} da ton tai! Vui long nhap ID khac.")
                        break
                else:
                    break
            except ValueError:
                print("Loi: ID phai la so nguyen.")

        while True:
            name = input("Nhap ten: ").title()
            if any(char.isdigit() for char in name):
                print("Loi: Ten khong duoc chua so! Vui long nhap lai.")
            elif name.strip() == "":
                print("Loi: Ten khong duoc de trong!")
            else:
                break

        while True:
            try:
                age = int(input("Nhap tuoi: "))
                if age <= 0:
                    print("Loi: Tuoi phai lon hon 0.")
                else:
                    break
            except ValueError:
                print("Loi: Tuoi phai la so nguyen.")

        while True:
            try:
                gpa = float(input("Nhap GPA (0 - 4.0): "))
                if (0 <= gpa <= 4):
                    break
                else:
                    print("Loi: GPA phai nam trong khoang tu 0 den 4.")
            except ValueError:
                print("Loi: GPA phai la so thuc.")

        new_student = Student(s_id, name, age, gpa)
        self.students.append(new_student)
        print(f"Da them thanh cong sinh vien: {name}")

    def delete_student(self):
        print("\n--- XOA SINH VIEN ---")
        try:
            s_id = int(input("Nhap ID can xoa: "))
            found = False
            for s in self.students:
                if s.id == s_id:
                    self.students.remove(s)
                    found = True
                    print(f"Da xoa sinh vien ID {s_id}")
                    break
            
            if not found:
                print("Khong tim thay ID nay.")
        except ValueError:
            print("Loi: ID phai la so.")

if __name__ == "__main__":
    manager = StudentManager('students.json')
    while True:
        print("\n=== MENU QUAN LY ===")
        print("1. Hien thi danh sach")
        print("2. Them sinh vien")
        print("3. Xoa sinh vien")
        print("4. Reset")
        print("5. Thoat")
        
        choice = input("Chon (1-5): ")
        if choice == '1':
            manager.show_students()
        elif choice == '2':
            manager.add_student()
        elif choice == '3':
            manager.delete_student()
        elif choice == '4':
            manager.load_data()
        elif choice == '5':
            print("Ket thuc!")
            break
        else:
            print("Chon sai, vui long chon lai.")
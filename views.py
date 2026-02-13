class StudentView:
    def show_menu(self):
        print("\n=== MENU QUẢN LÝ ===")
        print("1. Hiển thị danh sách")
        print("2. Thêm sinh viên")
        print("3. Xóa sinh viên")
        print("4. Reset")
        print("5. Thoát")
        return input("Chọn chức năng: ")

    def show_list(self, students):
        print("\n--- DANH SÁCH SINH VIÊN ---")
        if not students:
            print("Danh sách trống.")
        else:
            print(f"{'ID':<5} {'Tên':<20} {'Tuổi':<5} {'GPA':<5}")
            print("-" * 40)
            for s in students:
                print(f"{s.id:<5} {s.name:<20} {s.age:<5} {s.gpa:<5}")
        print("-" * 40)

    def get_student_input(self):
        print("--- Nhập thông tin sinh viên ---")
        while True:
            name = input("Nhập tên: ").title()
            if any(char.isdigit() for char in name):
                print("Lỗi: Tên không được chứa số.")
            elif name.strip() == "":
                print("Lỗi: Không được để trống.")
            else:
                break
        
        while True:
            try:
                age = int(input("Nhập tuổi: "))
                if age > 0: break
                print("Lỗi: Tuổi phải > 0.")
            except ValueError:
                print("Lỗi: Nhập số nguyên.")

        while True:
            try:
                gpa = float(input("Nhập GPA: "))
                if 0 <= gpa <= 4: break
                print("Lỗi: GPA từ 0-4.")
            except ValueError:
                print("Lỗi: Nhập số thực.")
        
        return name, age, gpa

    def get_id_input(self):
        while True:
            try:
                return int(input("Nhập ID: "))
            except ValueError:
                print("Lỗi: ID phải là số.")

    def show_message(self, message):
        print(f">> {message}")
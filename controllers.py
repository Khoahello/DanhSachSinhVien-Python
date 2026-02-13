from models import StudentModel
from views import StudentView

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '1':
                students = self.model.get_all_students()
                self.view.show_list(students)
            
            elif choice == '2':
                self.handle_add_student()
            
            elif choice == '3':
                self.handle_delete_student()
            
            elif choice == '4':
                self.model.load_data()
                self.view.show_message("Đã reset dữ liệu.")
            
            elif choice == '5':
                self.view.show_message("Kết thúc!")
                break
            else:
                self.view.show_message("Lựa chọn không hợp lệ.")

    def handle_add_student(self):
        s_id = self.view.get_id_input()
        
        if self.model.check_id_exists(s_id):
            self.view.show_message(f"Lỗi: ID {s_id} đã tồn tại!")
            return

        name, age, gpa = self.view.get_student_input()

        if self.model.add_student(s_id, name, age, gpa):
            self.view.show_message(f"Thêm thành công: {name}")

    def handle_delete_student(self):
        s_id = self.view.get_id_input()
        if self.model.delete_student(s_id):
            self.view.show_message(f"Đã xóa sinh viên ID {s_id}")
        else:
            self.view.show_message("Không tìm thấy ID này.")
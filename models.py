import json
import os

class Student:
    def __init__(self, id, name, age, gpa):
        self.id = id
        self.name = name
        self.age = age
        self.gpa = gpa

class StudentModel:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_data()

    def load_data(self):
        self.students = []
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    self.students.append(Student(item['id'], item['name'], item['age'], item['gpa']))
        except Exception:
            self.students = []

    def get_all_students(self):
        return self.students

    def check_id_exists(self, s_id):
        for s in self.students:
            if s.id == s_id:
                return True
        return False

    def add_student(self, s_id, name, age, gpa):
        if self.check_id_exists(s_id):
            return False
        new_s = Student(s_id, name, age, gpa)
        self.students.append(new_s)
        return True

    def delete_student(self, s_id):
        for s in self.students:
            if s.id == s_id:
                self.students.remove(s)
                return True
        return False
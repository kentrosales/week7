# Author: Kent Rovin Rosales
# Course: Certificate in Information Technology
# Date: April 2, 2026

class Student():

    id_counter = 1000

    def __init__(self, name, attendance, course):
        self.student_id = Student.id_counter
        Student.id_counter += 1
        self.name = name
        self.attendance = attendance
        self.course = course
        
    def __str__(self):
        return f"""Name: {self.name} | Attendance: {self.attendance}% | Course: {self.course}"""

class Attendance():
    
    def __init__(self):
        self.students = []
    
    def add_student(self, name, attendance, course):
        new_student = Student(name, attendance, course)
        self.students.append(new_student)
        print(f"Added: {name}")

    def find_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def update_student(self, student_id, new_attendance = None, new_course = None):
        for student in self.students:
            if student.student_id == student_id:
                if new_attendance is not None:
                    student.attendance = new_attendance
                if new_course:
                    student.course = new_course
                print(f"Record for {student_id} updated.")
                return
        print(f"Student with {student_id} not found.")

    def calculate_average_attendance(self):
        if not self.students:
            return 0.0
        total = sum(s.attendance for s in self.students)
        return total / len(self.students)
    
    def display_all_records(self):
        print("\n--- Current Student Records ---")
        if not self.students:
            print("No records found.")
        else:
            for student in self.students:
                print(student)
        print("-------------------------------\n")

if __name__ == "__main__": #making sure python runs this file when calling the "Attendance" class

    system = Attendance()
    # 1. Add student records
    system.add_student("Kent Rosales", 92.5, "Medical Technology")
    system.add_student("John Henry", 78.0, "Information Technology")
    system.add_student("Elmer Beray", 85.0, "Forklift Driving")

    # 2. Display records
    system.display_all_records()

    # 3. Update a record (e.g., Bob's attendance and course)
    # Elmer's ID would be 1002 based on the counter logic
    system.update_student(1002, new_attendance=82.0, new_course="Maritime Technology")

    # 4. Display again to see changes
    system.display_all_records()

    # 5. Calculate average attendance
    avg = system.calculate_average_attendance()
    print(f"Average Attendance for all students: {avg:.2f}%")
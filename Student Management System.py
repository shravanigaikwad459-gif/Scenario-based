class Student:

    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.grade())
        print()


class College:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        for student in self.students:
            student.display()


# Create college
college = College()

# Add students
college.add_student(Student(101, "Alice", 92))
college.add_student(Student(102, "Bob", 78))
college.add_student(Student(103, "Charlie", 65))
college.add_student(Student(104, "David", 45))

# Display all student details
college.display_all()
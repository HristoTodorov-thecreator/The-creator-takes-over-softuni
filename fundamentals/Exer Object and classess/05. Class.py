class Class:
    __students_count = 22

    def __init__(self,name : str):
        self.name = name

        self.students = []
        self.grades = []

    def add_student(self , name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)



    def get_average_grade(self):
        g = sum(self.grades) / len(self.grades)
        return float(f'{g:.2f}')


    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"



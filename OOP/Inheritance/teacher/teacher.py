from teacher.employee import Employee
from teacher.person import Person


class Teacher(Person,Employee):

    def teach(self):
        return 'teaching...'
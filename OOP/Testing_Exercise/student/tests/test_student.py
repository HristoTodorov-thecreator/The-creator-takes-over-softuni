import unittest

from project.student import Student  # Assuming your class is in student.py


class TestStudent(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures"""
        self.student = Student("John Doe")
        self.course_name = "Math"
        self.notes = ["Note 1", "Note 2"]

    def test_initialization_with_default_courses(self):
        """Test initialization with default courses parameter"""
        student = Student("Alice")
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.courses, {})

    def test_initialization_with_provided_courses(self):
        """Test initialization with provided courses"""
        courses = {"Physics": ["Note A"]}
        student = Student("Bob", courses)
        self.assertEqual(student.name, "Bob")
        self.assertEqual(student.courses, courses)

    def test_enroll_new_course_with_notes_default_choice(self):
        """Test enrolling in a new course with notes (default choice)"""
        result = self.student.enroll(self.course_name, self.notes)
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses[self.course_name], self.notes)

    def test_enroll_new_course_with_notes_explicit_yes(self):
        """Test enrolling in a new course with notes (explicit Y)"""
        result = self.student.enroll(self.course_name, self.notes, "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses[self.course_name], self.notes)

    def test_enroll_new_course_without_adding_notes(self):
        """Test enrolling in a new course without adding notes"""
        result = self.student.enroll(self.course_name, self.notes, "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses[self.course_name], [])

    def test_enroll_existing_course_updates_notes(self):
        """Test enrolling in an existing course updates notes"""

        self.student.enroll(self.course_name, self.notes)

        new_notes = ["Note 3"]
        result = self.student.enroll(self.course_name, new_notes)
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses[self.course_name], self.notes + new_notes)

    def test_add_notes_to_existing_course(self):
        """Test adding notes to an existing course"""
        self.student.enroll(self.course_name, [])
        result = self.student.add_notes(self.course_name, "New Note")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses[self.course_name], ["New Note"])

    def test_add_notes_to_nonexistent_course_raises_exception(self):
        """Test adding notes to a non-existent course raises exception"""
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Non-existent Course", "Some Note")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        """Test leaving an existing course"""
        self.student.enroll(self.course_name, self.notes)
        result = self.student.leave_course(self.course_name)
        self.assertEqual(result, "Course has been removed")
        self.assertNotIn(self.course_name, self.student.courses)

    def test_leave_nonexistent_course_raises_exception(self):
        """Test leaving a non-existent course raises exception"""
        with self.assertRaises(Exception) as context:
            self.student.leave_course("Non-existent Course")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")

    def test_multiple_courses_management(self):
        """Test managing multiple courses"""

        math_notes = ["Math Note 1"]
        self.student.enroll("Math", math_notes)


        physics_notes = ["Physics Note 1"]
        self.student.enroll("Physics", physics_notes, "Y")


        self.student.add_notes("Math", "Math Note 2")


        self.assertEqual(self.student.courses["Math"], ["Math Note 1", "Math Note 2"])
        self.assertEqual(self.student.courses["Physics"], ["Physics Note 1"])


        self.student.leave_course("Physics")
        self.assertIn("Math", self.student.courses)
        self.assertNotIn("Physics", self.student.courses)


if __name__ == '__main__':
    unittest.main()
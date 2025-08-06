from project.senior_student import SeniorStudent
import unittest

class TestSeniorStudent(unittest.TestCase):

    def setUp(self):
        self.student = SeniorStudent('1234','Ivan Petrov',3.5)

    def test_init_valid_data(self):
        self.assertEqual(self.student.student_id,'1234')
        self.assertEqual(self.student.name,'Ivan Petrov')
        self.assertEqual(self.student.student_gpa,3.5)
        self.assertEqual(self.student.colleges,set())

    def test_id_too_short_raises(self):
        with self.assertRaises(ValueError) as ex:
            SeniorStudent('127','Ivan',3.0)
        self.assertEqual(str(ex.exception),"Student ID must be at least 4 digits long!")

    def test_name_empty_raises(self):
        with self.assertRaises(ValueError) as ex:
            SeniorStudent('1377','',3)
        self.assertEqual(str(ex.exception),"Student name cannot be null or empty!")

    def test_gpa_too_low_raises(self):
        with self.assertRaises(ValueError) as ex:
            SeniorStudent('1477','Luka',0.5)
        self.assertEqual(str(ex.exception),"Student GPA must be more than 1.0!")

    def test_apply_to_college_successful(self):
        result = self.student.apply_to_college(3,'Harvard')
        self.assertIn('Harvard'.upper(),self.student.colleges)
        self.assertEqual(result,"Ivan Petrov successfully applied to Harvard.")

    def test_apply_to_college_fail_low_gpa(self):
        result = self.student.apply_to_college(4,'MIT')
        self.assertEqual(result,"Application failed!")
        self.assertNotIn('MIT',self.student.colleges)

    def test_successful_update_gpa(self):
        result = self.student.update_gpa(3.8)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.student.student_gpa, 3.8)

    def test_update_invalid_low_gpa(self):
        result = self.student.update_gpa(1)
        self.assertEqual(result,"The GPA has not been changed!")
        self.assertEqual(self.student.student_gpa,3.5)

    def test_eq_equal_gpa(self):
        other = SeniorStudent('9966','John',3.5)
        self.assertTrue(self.student == other)

    def test_eq_equal_fail_gpa(self):
        other = SeniorStudent('9866','Take',3)
        self.assertFalse(self.student == other)






if __name__ == '__main__':
    unittest.main()
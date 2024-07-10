import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        # declare 2 employees with first and last name and pay
        emp_1 = Employee('Anna', 'Smith', 9000)
        emp_2 = Employee('Frank', 'Barkley', 5000)

        # check their emails
        self.assertEqual(emp_1.email, 'Anna.Smith@email.com')
        self.assertEqual(emp_2.email, 'Frank.Barkley@email.com')

        # change their first names
        emp_1.first = 'Jane'
        emp_2.first = 'John'

        # check emails after change
        self.assertEqual(emp_1.email, 'Jane.Smith@email.com')
        self.assertEqual(emp_2.email, 'John.Barkley@email.com')

    def test_fullname(self):
        emp_1 = Employee('Anna', 'Smith', 9000)
        emp_2 = Employee('Frank', 'Barkley', 5000)

        self.assertEqual(emp_1.fullname, 'Anna Smith')
        self.assertEqual(emp_2.fullname, 'Frank Barkley')

        # change their first names
        emp_1.first = 'Jane'
        emp_2.first = 'John'

        # check emails after change
        self.assertEqual(emp_1.fullname, 'Jane Smith')
        self.assertEqual(emp_2.fullname, 'John Barkley')

    def test_apply_raise(self):
        emp_1 = Employee('Anna', 'Smith', 50000)
        emp_2 = Employee('Frank', 'Barkley', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

    def test_monthly_schedule(self):
        emp_1 = Employee('Anna', 'Smith', 50000)
        emp_2 = Employee('Frank', 'Barkley', 60000)

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Barkley/June')
            self.assertEqual(schedule, 'Bad Response.')

            


if __name__ == '__main__':
    unittest.main()
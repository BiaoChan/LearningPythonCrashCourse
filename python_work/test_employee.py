import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.default_salary = 10000
        self.employee = Employee('chen', 'bill', self.default_salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1234)
        self.assertEqual(self.employee.salary, 11234)

unittest.main()

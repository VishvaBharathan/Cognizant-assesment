import unittest

# Arithmetic Class
class Arithmetic:

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y


# Unit Tests
class TestArithmetic(unittest.TestCase):

    def setUp(self):
        self.obj = Arithmetic()

    def test_addition(self):
        self.assertEqual(self.obj.addition(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(self.obj.subtraction(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.obj.multiplication(10, 5), 50)

    def test_division(self):
        self.assertEqual(self.obj.division(10, 5), 2)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            self.obj.division(10, 0)


if __name__ == "__main__":
    unittest.main()

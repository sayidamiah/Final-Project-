import unittest
from function import multiply_numbers

class TestFunction(unittest.TestCase):

    def test_multiplication(self):
        result = multiply_numbers(3,5)
        self.assertEqual(result, 15)
    
    def test_multiplication_negative_numbers(self):
        result = multiply_numbers(-2,7)
        self.assertEqual(result, -14)

   # def test_multiplication_float_numbers(self):
       # result = multiply_numbers(1.5,2.5)
       # self.assertAlmostEqual(result,3.75, places=2)
    
    def test_multiplication_strings(self):
        with self.assertRaises(TypeError):
            multiply_numbers("10",2)
            multiply_numbers(10,"2")

if __name__ == '__main__':
    unittest.main()

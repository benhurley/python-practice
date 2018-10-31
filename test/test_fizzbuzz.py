import unittest
from func.fizzbuzz import fizzbuzz
from func.fizzbuzz import fizzbuzzjazz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(100), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz', '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73', '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz'])
        self.assertEqual(fizzbuzz(-1), [])
        self.assertEqual(fizzbuzz('t'), -1)
        self.assertEqual(fizzbuzz(2.546), -1)

    def test_fizzbuzzjazz(self):
        self.assertEqual(fizzbuzzjazz(100), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Jazz', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', 'Jazz', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'FizzJazz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', 'Jazz', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'BuzzJazz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'FizzJazz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', 'Jazz', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', 'Jazz', 'Fizz', '58', '59', 'FizzBuzz', '61', '62', 'FizzJazz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'BuzzJazz', '71', 'Fizz', '73', '74', 'FizzBuzz', '76', 'Jazz', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'FizzJazz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz', 'Jazz', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', 'Jazz', 'Fizz', 'Buzz'])
        self.assertEqual(fizzbuzzjazz(-1), [])
        self.assertEqual(fizzbuzzjazz('t'), -1)
        self.assertEqual(fizzbuzzjazz(2.546), -1)
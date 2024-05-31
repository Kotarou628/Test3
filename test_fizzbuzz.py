import unittest
import fizzbuzz
class TestFizzBuzz(unittest.TestCase):
def test_fizz(self):
self.assertEqual('Fizz', fizzbuzz.fizzbuzz(3))
def test_buzz(self):
self.assertEqual('Buzz', fizzbuzz.fizzbuzz(5))

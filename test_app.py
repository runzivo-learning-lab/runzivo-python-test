
import unittest
from app import greet, add_numbers

class TestApp(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(
            greet("ZSoftly Student"),
            "Hello, ZSoftly Student! Welcome to Runzivo."
        )

    def test_addition(self):
        self.assertEqual(add_numbers(10, 5), 15)

if __name__ == "__main__":
    unittest.main()

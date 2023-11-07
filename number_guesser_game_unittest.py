import unittest

class test_questions(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(10, 10)

    def test_q2(self):
        self.assertEqual(20,20)

    def test_q3(self):
        self.assertEqual(30,30)

if __name__ == "__main__":
    unittest.main()
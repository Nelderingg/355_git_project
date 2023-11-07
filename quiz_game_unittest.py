import unittest

class test_questions(unittest.TestCase):
    def test_q1(self):
        self.assertEqual("central processing unit".upper(), "CENTRAL PROCESSING UNIT")

    def test_q2(self):
        self.assertEqual("graphics processing unit".upper(), "GRAPHICS PROCESSING UNIT")

    def test_q3(self):
        self.assertEqual("random access memory".upper(), "RANDOM ACCESS MEMORY")

if __name__ == "__main__":
    unittest.main()
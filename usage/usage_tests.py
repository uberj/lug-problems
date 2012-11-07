import unittest
from calc_usage import calc_usage

START, END = 0, 9

class UsageTests(unittest.TestCase):

    def test1_one_list(self):
        b = [0, 2, 3, 4, 5]
        unused, used = calc_usage(START, END, [b])
        self.assertEqual(5, used)
        self.assertEqual(5, unused)

    def test2_one_list(self):
        b = [0, 2, 4, 6, 8]
        unused, used = calc_usage(START, END, [b])
        self.assertEqual(5, used)
        self.assertEqual(5, unused)

    def test3_one_list(self):
        b = [1]
        unused, used = calc_usage(START, END, [b])
        self.assertEqual(1, used)
        self.assertEqual(9, unused)

    def test4_one_list(self):
        b = [1, 9]
        unused, used = calc_usage(START, END, [b])
        self.assertEqual(2, used)
        self.assertEqual(8, unused)

    def test4_one_list(self):
        b = [1, 3, 9]
        unused, used = calc_usage(START, END, [b])
        self.assertEqual(3, used)
        self.assertEqual(7, unused)

    def test5_one_list(self):
        b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        unused, used = calc_usage(START, END, [b])
        self.assertEqual(10, used)
        self.assertEqual(0, unused)

    def test1_two_list(self):
        b = [0, 2, 3, 4, 5]
        c = [1, 3, 4, 5, 6]
        unused, used = calc_usage(START, END, [b, c])
        self.assertEqual(7, used)
        self.assertEqual(3, unused)

    def test2_two_list(self):
        c = [0, 3, 4, 7, 8]
        b = []
        unused, used = calc_usage(START, END, [b, c])
        self.assertEqual(5, used)
        self.assertEqual(5, unused)

    def test3_two_list(self):
        b = [1]
        c = [9]
        unused, used = calc_usage(START, END, [b, c])
        self.assertEqual(2, used)
        self.assertEqual(8, unused)

    def test4_two_list(self):
        b = [5, 9]
        c = [1, 9]
        unused, used = calc_usage(START, END, [b, c])
        self.assertEqual(3, used)
        self.assertEqual(7, unused)

    def test5_two_list(self):
        b = [1, 3, 9]
        c = [1, 3, 9]
        unused, used = calc_usage(START, END, [b, c])
        self.assertEqual(3, used)
        self.assertEqual(7, unused)

    def test1_three_list(self):
        b = [0, 2, 3, 4, 5]
        c = []
        d = [1, 3, 4, 5, 6]
        unused, used = calc_usage(START, END, [b, c, d])
        self.assertEqual(7, used)
        self.assertEqual(3, unused)

    def test2_three_list(self):
        b = [1, 3, 9]
        c = [0, 8, 9, 3]
        d = [0, 3, 4, 7, 8]
        unused, used = calc_usage(START, END, [b, c, d])
        self.assertEqual(7, used)
        self.assertEqual(3, unused)

    def test3_three_list(self):
        b = [1]
        c = [9]
        unused, used = calc_usage(START, END, [b, c])
        self.assertEqual(2, used)
        self.assertEqual(8, unused)

    def test0_three_list(self):
        b = [1, 3, 9]
        c = [0, 8, 9]
        d = [1, 3, 5]
        unused, used = calc_usage(START, END, [b, c, d])
        self.assertEqual(6, used)
        self.assertEqual(4, unused)

    def test0_6_list(self):
        lists = [[1, 3, 9],
                [9, 3, 1],
                [2, 2, 2],
                [5, 5, 5],
                [8, 6, 3],
                [1, 3, 4, 7, 0]]
        unused, used = calc_usage(START, END, lists)
        self.assertEqual(10, used)
        self.assertEqual(0, unused)

    def test0_very_large_range(self):
        lists = [[2**16]]
        unused, used = calc_usage(0, 2**64, lists)
        self.assertEqual(1, used)
        self.assertEqual((2**64), unused)

    def test1_very_large_range(self):
        lists = [[2**16, 2**26, 2**127]]
        unused, used = calc_usage(0, 2**128, lists)
        self.assertEqual(3, used)
        self.assertEqual((2**128) - 2, unused)

if __name__ == '__main__':
    unittest.main()

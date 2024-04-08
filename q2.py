"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).
"""
import unittest

# --------------------------------------------------------------
# Power of 3
# --------------------------------------------------------------
def isPowerOfThree(n):
# firstly elimating all the negative integers coz no power of 3 would give an integer less than 0
    if (n<0):
        return False
    else:
# a while loop to check if given n is a power of 3
        while n % 3 == 0:
            n = n // 3
            
        if n == 1:
            return True
        else:
            return False



# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(isPowerOfThree(3),True)
    def test1(self):
        self.assertEqual(isPowerOfThree(9),True)
    def test2(self):
        self.assertEqual(isPowerOfThree(12),False)
    def test3(self):
        self.assertEqual(isPowerOfThree(22),False)
    def test4(self):
        self.assertEqual(isPowerOfThree(27),True)


if __name__=='__main__':
    unittest.main(exit=True)
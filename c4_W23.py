import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

def enumerate1(N, a, b) :
    '''
    Assume that N and a and b are positive integers.
    Returns the sum of the integers from 1 to N, inclusive,
    but leaving out the integers divisible by a or b.

    For example, 
    enumerate1(10, 3, 2) returns 13, 
    since 1 + 5 + 7 = 13
    '''
    n=0
    for i in range(N):
        n+=i
        if (i%a)==0:
            n=n-i
        if (i%b)==0:
            n=n-i
    return n

            
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
     ans = enumerate1(10, 3, 2)
     self.assertEqual(ans, 13)
 def test2(self):
     ans = enumerate1(1000000, 3, 3)
     self.assertEqual(ans, 333333666667)
 def test3(self):
     ans = enumerate1(50, 4, 7)
     self.assertEqual(ans, 795)
 def test4(self):
     ans = enumerate1(2, 5, 7)
     self.assertEqual(ans, 3)
 def test5(self):
     ans = enumerate1(117, 7, 5)
     self.assertEqual(ans, 4781)

     
if __name__ == '__main__':
 unittest.main(exit=True)


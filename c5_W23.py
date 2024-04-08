import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""
def enumerate2(N) :
    '''
    Assume that N is a positive integer.
    Return the count of positive and even integers, that divide N with no remainder.

    For example, enumerate2(8) returns 3
    since 1, 2, 4, 8 divide into 8 with no remainder, but only 2, 4 and 8 are even.
    '''
    lst=[]
    for i in range(1,N+1):
        if N%i==0:
            if i%2==0:
                lst.append(i)
        else:
            continue
    
    return len(lst)
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
     ans = enumerate2(8)
     self.assertEqual(ans, 3)
 def test2(self):
     ans = enumerate2(124678)
     self.assertEqual(ans, 8)
 def test3(self):
     ans = enumerate2(50)
     self.assertEqual(ans, 3)
 def test4(self):
     ans = enumerate2(124)
     self.assertEqual(ans, 4)
 def test5(self):
     ans = enumerate2(117)
     self.assertEqual(ans, 0)
     
if __name__ == '__main__':
 unittest.main(exit=True)


import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

def add_up(tup, n) :
    '''
    Assume that tup is a tuple. Return the sum of the first n 
    elements of the tuple. Do not assume n <= len(tup).
    
    For example,
    add_up((), 9) returns 0
    add_up((3, 4, 6, 2), 3) returns 13
    add_up((2, 8), 2) returns 10
    '''
    summ=0
    length=len(tup)
    if length<n:
        for i in range(0,length):
            if i<n:
                summ+=tup[i]
            else:
                summ+=0
        return summ
    else:
        for i in range(0,n):
            if i<n:
                summ+=tup[i]
            else:
                summ+=0
        return summ
        
        
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(add_up((), 9), 0)
    def test2(self):
        self.assertEqual(add_up((3, 4, 6, 2), 3), 13)
    def test3(self):
        self.assertEqual(add_up((2, 8), 2), 10)
    def test4(self):
        self.assertEqual(add_up((100, 200, 300, 400, 500), 6), 1500)
    def test5(self):
        self.assertEqual(add_up((1, 1, 1, 1, 1, 1), 3), 3)

if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

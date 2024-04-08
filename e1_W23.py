import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""
def countdifferent(a, b, c, d) :
    '''
    Assume that the four parameters are numbers.
    Return the number of different values in the four numbers.
    For example, if a is 9, and b is 7, and c is 7 and d is 9,
    then the function would return 2, since there are two values: 7 and 9
    '''
    count=4
    if a==b or a==c or a==d:
      count-=1
    if b==c or b==d:
          count-=1
    if c==d:
          count-=1
    return count
        
        
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(countdifferent(1, 2, 3, 4), 4)
 def test2(self):
  self.assertEqual(countdifferent(1, 2, 3, 2), 3)
 def test3(self):
  self.assertEqual(countdifferent(12, 2, 2, 2), 2)
 def test4(self):
  self.assertEqual(countdifferent(0, 0, 0, 0), 1)

if __name__ == '__main__':
 unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

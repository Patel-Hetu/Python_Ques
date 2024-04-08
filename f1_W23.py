import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""
def count_different_digits(number) :
    '''
    Assume that number is an integer great than or equal to 0.
    Return the number of different digits in number.

    For example, if number is 523, then return 3, since 5, 2 and 3
    are the different digits.
    If number is 55, return 1, since 5 is the only kind of digit
    If number is 0, return 1
    '''
    string=str(number)
    lst1=[]
    for char in string:
        if char not in lst1:
            lst1.append(char)
        else:
            continue
    return len(lst1)

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(count_different_digits(57), 2)
 def test2(self):
  self.assertEqual(count_different_digits(0), 1)
 def test3(self):
  self.assertEqual(count_different_digits(4343), 2)
 def test4(self):
  self.assertEqual(count_different_digits(9876543210), 10)

  
if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

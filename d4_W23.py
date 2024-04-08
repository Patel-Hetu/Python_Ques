import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

'''
  Given an integer n, we would like to remove digits from either 
  the leftmost end or the rightmost end until there are no more 
  digits. If there are more even digits than odd digits, we will 
  remove from the rightmost end. If there are more odd digits than
  even, we'll remove from the leftmost end. If there are an equal 
  amount of odd and even numbers, we'll remove from both ends.
  Return a tuple where the first element contains the amount of
  leftmost removals and the second element contains the amount
  of rightmost removals.

  Example:
  n = 1000153
  Odd digits > Even digits, so remove from left end

  n = 000153
  Odd digits == Even digits, remove from both ends

  After removing until n has no more digits,
  we return (4,3) meaning 4 left removals and 3 right removals
'''
def digit_slice(n):
    x=str(n)
    a=b=right=left=0
    y=len(x)
    while y!=0:
        for i in x:
            num=int(i)
            if num%2==0:
                a=a+1
            else:
                b=b+1
        if b>a:
            x=x[1:]
            b=b-1
            left+=1
        elif a>b:
            x=x[:-1]
            a=a-1
            right+=1
        elif a==b:
            x=x[1:-1]
            left+=1
            right+=1
            a=a-1
            b=b-1
        y=len(x)
    return (left,right)

  
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
      self.assertEqual(digit_slice(1000153), (4,3))
    def test2(self):
      self.assertEqual(digit_slice(7146), (2,2))
    def test3(self):
      self.assertEqual(digit_slice(1), (1,0))
    def test4(self):
      self.assertEqual(digit_slice(6729135), (7,0))

      
if __name__ == '__main__':
 unittest.main(exit=True)

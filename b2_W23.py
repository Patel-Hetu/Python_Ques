import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

"""Bisection Search
Given a sorted non-empty tuple of integers and a target value to
insert, use bisection search to determine the index where this target
value would be if it were included, in order, in this tuple.  Then,
create and return a new sorted tuple, based on the original tuple,
such that now it includes, in order, the target value.

Your function MUST use BISECTION SEARCH (no points if you do not).  

Example:
    insertValue((-10,-7,0,1,8,9,22,88), 10) 
      returns (-10, -7, 0, 1, 8, 9, 10, 22, 88), since the 10 goes after the 9
    insertValue((-10,), 4) returns (-10, 4), since the 4 goes after the -10
    
Hint: the upper bound 'high' of your search, and the lower bound
'low' of your search, will eventually converge to low = high - 1.
"""

def insertValue(aTuple, target):
    l=0
    h=len(aTuple)-1
    y=0
    
    for i in aTuple:
        if i<target:
            y=i
    
    while l<=h:
        m=(l+h)//2
        if aTuple[m]==y:
            z=m
            break
        else:
            if aTuple[m]<y:
                l=m
            else:
                h=m
    
    s=list(aTuple)
    s.insert(z+1,target)
    return tuple(s)



class myTests(unittest.TestCase):
   def test1(self):
       self.assertEqual(insertValue((-10,-7,0,1,8,9,22,88),10),(-10, -7, 0, 1, 8, 9, 10, 22, 88))
   def test2(self):
       self.assertEqual(insertValue((-10,1,3,22,88),-11),(-11, -10, 1, 3, 22, 88))
   def test3(self):
       self.assertEqual(insertValue((-10,),4),(-10, 4))
   def test4(self):
      self.assertEqual(insertValue((-1,),-4),(-4, -1))
    
if __name__ == '__main__':
      unittest.main(exit=True)

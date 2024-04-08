import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""
"""
You are given two lists, whose elements are integers with values ranging from 1 to 9. 
Some elements might be missing in these lists. If so, then these elements have been 
replaced with 0 values. Each list can be any size larger than 1. 
The goal is to replace these missing elements with integer values ranging from 1 to 9, 
and such that the sum of both arrays is equal and as low as possible.
Then return this minimum commun sum.
If this is not possible for both lists to have the same sum, then return -1.

Example 1:
You are given the lists L1 and L2:
L1 = [1,0,2]
L2 = [1, 3, 0, 0]

L1 has 1 missing element, while L2 has 2 missing elements.
The smallest sum of the element for L1 is 4 (1+1+2), while L2 is 6 (1+3+1+1).
In turn, the function findMinimumEqualSum should return 6.


Example 2:
You are given the lists L1 and L2:
L1 = [9, 9, 0, 0]
L2 = [1,0,1]

L1 has 2 missing elements, while L2 has 1 missing element.
The smallest sum of the elements in L1 is 20 (9+9+1+1). 
It is not possible to assign values to the missing elements of L2, 
such that its sum becomes 20.
In turn, the function findMinimumEqualSum should return -1.   
"""

def findMinimumEqualSum(L1, L2):
    n1=L1.count(0)
    n2=L2.count(0)
    sum1=sum(L1)
    sum2=sum(L2)
    minsum1=sum1+n1
    maxsum1=sum1+(n1)*9
    minsum2=sum2+n2
    maxsum2=sum2+(n2)*9
    minsum=-1
    for i in range(minsum1,maxsum1+1):
       for j in range(minsum2,maxsum2+1):
            if i==j  and minsum<i:
              minsum=i
    return minsum
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(findMinimumEqualSum([1, 0, 2],[1, 3, 0, 0]), 6)
    def test2(self):
        self.assertEqual(findMinimumEqualSum([1, 0, 1], [9, 9, 0, 0]), -1)
    def test3(self):
        self.assertEqual(findMinimumEqualSum([9, 7], [9, 0, 6]), 16)
    def test4(self):
        self.assertEqual(findMinimumEqualSum([1, 0, 6, 0], [5, 0, 6]), 12)
    def test5(self):
        self.assertEqual(findMinimumEqualSum([9, 0, 6],[9, 7]), 16)



if __name__=='__main__':
    unittest.main(exit=True) 
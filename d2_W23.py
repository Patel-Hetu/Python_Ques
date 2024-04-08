import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

"""
You are given two lists, whose elements are integers with values ranging from 1 to 9. 
Some elements are missing in these lists. These elements have been replaced with 0 values. 
Each list can be any size larger than 1. 
The goal is to replace these missing elements with integer values ranging from 1 to 9, 
and such that the sum of both list is equal and as high as possible.
Then return this maximum commun sum.
If this is not possible for both lists to have the same sum, then return -1.

Example 1:
You are given the lists L1 and L2:
L1 = [1,0,2]
L2 = [1, 3, 0, 0]

L1 has 1 missing element, while L2 has 2 missing elements.
The smallest sum of the element for L1 is 12 (1+9+2), while L2 is 22 (1+3+9+9).
In turn, the function findMaximumEqualSum should return 12.


Example 2:
You are given the lists L1 and L2:
L1 = [1,0,1]
L2 = [9, 9, 0, 0]

L1 has 1 missing element, while L2 has 2 missing elements.
The largest sum of the elements in L1 is 11 (1+9+1). 
It is not possible to assign values to the missing elements of L2, 
such that its sum becomes 11.
In turn, the function findMaximumEqualSum should return -1.   
"""

def findMaximumEqualSum(L1, L2):
    length1=len(L1)
    length2=len(L2)
    if length1<length2:
        sum1=0
        sum2=0
        for i in range(0,length1):
            if L1[i]==0:
                L1[i]=9
            else:
                continue
        for i in range(0,length1):
            sum1+=L1[i]
        for j in range(0,length2):
            sum2+=L2[j]
        if sum2>sum1:
            return -1
        else:
            return sum1
    else:
        sum1=0
        sum2=0
        for i in range(0,length2):
            if L2[i]==0:
                L2[i]=9
            else:
                continue
        for i in range(0,length2):
            sum1+=L2[i]
        for j in range(0,length1):
            sum2+=L1[j]
        if sum2>sum1:
            return -1
        else:
            return sum1
        
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(findMaximumEqualSum([1, 0, 2],[1, 3, 0, 0]), 12)
    def test2(self):
        self.assertEqual(findMaximumEqualSum([1, 0, 1], [9, 9, 0, 0]), -1)
    def test3(self):
        self.assertEqual(findMaximumEqualSum([9, 0, 6], [9, 7]), 16)
    def test4(self):
        self.assertEqual(findMaximumEqualSum([1, 0, 6, 0], [5, 0, 6]), 20)
    def test5(self):
        self.assertEqual(findMaximumEqualSum([9, 7], [9, 0, 6]), 16)


if __name__=='__main__':
    unittest.main(exit=True)    

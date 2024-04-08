import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

'''
    Given a tuple nums, return True if there exists a pair of 
    numbers that sum to zero.

    ex:
    nums = (1,2,5,6,-2,5,7,8) -> True, since the pair 2 and -2 sum to zero
'''
def zero_sum(nums) :
    '''Assumes that nums is a tuple of integers.
    Returns True if two integers in the tuple add up to 0, otherwise False.
    '''
    
    n=nums
    #c=0
    for i in nums:
        for j in n:
            if i!=j:
                if i+j==0:
                    return True
   
    return False
    
            
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
     self.assertEqual(zero_sum((1,2,5,6,-2,5,7,8)), True)
    def test2(self):
      self.assertEqual(zero_sum((0,9,29,30,-1,3,-11,23,-44,80,30)), False)
    def test3(self):
      self.assertEqual(zero_sum((0,)), False)
    def test4(self):
      self.assertEqual(zero_sum((-1,1)), True)

if __name__ == '__main__':
 unittest.main(exit=True)

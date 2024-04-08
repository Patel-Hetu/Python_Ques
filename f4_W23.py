import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

"""
New office, no chairs. For each employee that arrives to workspace, 
represented by letter C, takes a chair if available, or we buy a new one if not available.
R means the employee leaves for lunch and frees up a chair
U means the employee returns from lunch and takes a chair if available. Otherwise we buy a new one.
Assume when we buy a new one the chair is available instantaneously.
L means that the employees leaves the office for the day and therefore frees up a chair
Given a string, return the minimum number of chairs we need to buy for the employees

For example, you are given the string 'CRUC'
The first letter is a 'C', which means that an employee comes. Since the office has no chair, 1 chair is purchased, and none is available.
The second letter is a 'R', which means that an employee leaves for lunch. The office has a purchased chair, and 1 is available.
The third letter is 'U', which means the employee returned from lunch. The office has purchased 1 chair and none is available.
The last letter is 'C', which means that an employee comes. Since the office has purchased 1 chair, but that none is available, the office purchases a 2nd chair, and none is available.
Since there are no more letters in the string, and that the office had purchased a total of 2 chairs, the function numbChair returns 2.
"""

def numbChair(A):
  n1=A.count("C")
  if "LC" in A:
      n1=n1-1
  return n1

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(numbChair('CRUC'), 2)
    def test2(self):
        self.assertEqual(numbChair('CCCRUCLCC'), 5)
    def test3(self):
        self.assertEqual(numbChair(''), 0)
    def test4(self):
        self.assertEqual(numbChair('CRUL'), 1)
    def test5(self):
        self.assertEqual(numbChair('CRUCLL'), 2)

if __name__=='__main__':
    unittest.main(exit=True)   

import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""
def slice_reverse(S, i, j) :
    '''
    Assume that S is a string and i and j are integers >= 0
    which are valid indices into S.
    Returns the slice of S from i to j, inclusive if i <= j, 
    but if j < i then returns REVERSE of the slice from i to j inclusive.
    Hint: the reverse of string s is s[::-1].

    For example, slice_reverse('wonderful', 3, 6) returns 'derf'
    slice_reverse('wonderful', 6, 3) returns 'fred'
    
    '''
    if i<=j:
        x=S[i:j+1]
    elif j<i:
        x=S[i:j-1:-1]
    return x

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
     self.assertEqual(slice_reverse('wonderful', 3, 6), 'derf')
 def test2(self):
     self.assertEqual(slice_reverse('wonderful', 6, 3), 'fred')
 def test3(self):
     self.assertEqual(slice_reverse('gaslighting', 0, 7), 'gaslight')
 def test4(self):
     self.assertEqual(slice_reverse('Toronto Met', 0, 0), 'T')
 def test5(self):
     self.assertEqual(slice_reverse('university', 5, 5), 'r')
     
    
if __name__ == '__main__':
 unittest.main(exit=True)



# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

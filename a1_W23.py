import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

def lower_upper(S) :
    '''
    Assume that S is a string.
    If the length of S is odd, then return a string just like S
    except that the middle letter is uppercase and the rest is lowercase.
    If the length of S is even, then return a string with the 
    first half lower case and the second half upper case.

    For example, lower_upper('wonderful') returns 'wondErful'.
    And, lower_upper('FROG') returns 'frOG'.
    And, lower_upper('SNAKE') returns 'snAke'.
    And, lower_upper('') returns ''.
    Hint: lower() and upper() are methods of str    
    '''
    s=S.lower()
    n=len(s)
    if n==0:
        return s
 
    if n%2==0:
        return s[:(n//2)].lower()+s[(n//2):].upper()
    else:
        return s[:(n//2)].lower()+s[(n//2)].upper()+s[(n//2)+1:].lower()
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
     self.assertEqual(lower_upper('wonderful'), 'wondErful')
 def test2(self):
     self.assertEqual(lower_upper('FROG'), 'frOG')
 def test3(self):
     self.assertEqual(lower_upper('t'), 'T')
 def test4(self):
     self.assertEqual(lower_upper(''), '')

if __name__ == '__main__':
 unittest.main(exit=True)




# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

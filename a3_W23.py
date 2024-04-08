import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""

def capitalize_middle(S) :
    '''
    Assume that S is a string.
    Returns a string just like S, but all lowercase except with 
    the middle one (when the length is odd) or two (when the length 
    is even) letter(s) capitalized.

    For example, capitalize_middle('wonderful') returns 'wondErful'.
    And, capitalize_middle('FROG') returns 'fROg'.
    Hint: upper() and lower() are methods of str
    '''
    length=len(S)
    string=''
    S=S.lower()
    if length%2==0:
        a=length/2
        b=a-1
        for i in range(0,len(S)):
            if i==a:
                string=string+S[i].upper()
            elif i==b:
                string=string+S[i].upper()
            else:
                string=string+S[i]
    else:
        a=length//2
        for i in range(0,len(S)):
            if i==a:
                string=string+S[i].upper()
            else:
                string=string+S[i]
    
    return string
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
     self.assertEqual(capitalize_middle('wonderful'), 'wondErful')
 def test2(self):
     self.assertEqual(capitalize_middle('FROG'), 'fROg')
 def test3(self):
     self.assertEqual(capitalize_middle('t'), 'T')
 def test4(self):
     self.assertEqual(capitalize_middle(''), '')
 def test5(self):
     self.assertEqual(capitalize_middle('UNiVeRSiTY'), 'univERsity')

if __name__ == '__main__':
 unittest.main(exit=True)

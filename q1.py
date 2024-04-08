#!/usr/bin/python3
import unittest

def encode1(string, key):
    """
    Write a function encode1(string, key) that does a keyword cipher 
    using the keyword key to create the alternate alphabet by placing 
    the key at the beginning just before the other letters.  
    For example, if the key is 'earth', then the alternate alphabet is 
    
    'earthbcdfgijklmnopqsuvwxyz'.  In that case,
    
    encode1('deed', 'earth') would produce 'thht'.   
    
    Characters from string which are not in the alphabet are simply 
    skipped and produce nothing in the output string.  
    For example, encode1('deeds speak', 'earth') produces 'thhtqqnhei'. 
    
    Assume that the letters from string and key are always lowercase.
    
    What is the result for encode1('morning glory', 'flower')
    ikpjcjaahkpy
    """
    I = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    altA = []
    
    #forming alternative alphabet list
    for i in range(len(key)):
        altA.append(key[i])
    for j in I:
        if altA.count(j) == 0:
            altA.append(j)
            
    #removing spaces from string
    string = string.replace(" ","")
    cipher = ""
    
    #replacing string letters with altA using the index from the regular alphabet list
    
    for k in string:
        cipher = cipher + altA[I.index(k)]
        
    return cipher

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
     self.assertEqual(encode1('morning glory', 'flower'), 'ikpjcjaahkpy')
 def test2(self):
     self.assertEqual(encode1('deeds speak', 'earth'), 'thhtqqnhei')
 def test3(self):
     self.assertEqual(encode1('deed', 'earth'), 'thht')
 def test4(self):
     self.assertEqual(encode1('toronto metropolitan university', 'computer'), 'qilihqiguqlijifaqchshavulnaqy')
 def test5(self):
     self.assertEqual(encode1('toronto metropolitan university', 'abcd'), 'torontometropolitanuniversity')

if __name__ == '__main__':
 unittest.main(exit=True)


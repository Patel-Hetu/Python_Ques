import unittest
"""
Very important:
Please upload on D2L, under Assignments -> Midterm code submission
the scripts you will have written during your midterm.

Submit your python scripts without modifying the filename. 
"""
"""
Bisection Search 

Write a function that finds the position of a given word in the sorted tuple,
'wordsTuple'.  Return the index, of where the word is. 
If the word is not in the tuple, return False.  

Your function MUST use BISECTION SEARCH (no points if you do not).  

In turn, you should NOT make use of any operators and functions such as
‘in’, ‘not in’ and index().
"""

wordsTuple =  ('nepalese', 'nepenthe', 'nephrite', 'nepotism', 'nerviest', 'nervosas', 'nestling',
 'netsukes', 'nettling', 'networks', 'neuritis', 'neuroses', 'neurosis', 'neurotic',
 'neutered', 'neutrals', 'neutrino', 'neutrons', 'newborns', 'newcomer', 'newlywed',
 'newsiest', 'newsboys', 'newscast', 'newsreel', 'nibbling', 'niceties', 'nickname',
 'nicotine', 'niftiest', 'nigerian', 'niggling', 'nightcap', 'nihilism', 'nihilist',
 'nimblest', 'ninepins', 'nineties', 'nineteen', 'nippiest', 'nirvanas', 'nitrated',
 'nitrates', 'nitrides', 'nitrites', 'nitrogen', 'nobelium', 'nobility', 'noblemen',
 'nobleman', 'noblesse', 'nobodies', 'nocturne', 'noisiest', 'nominate', 'nominees',
 'nomogram', 'nonagons', 'nonesuch', 'nonjuror', 'nonmetal', 'nonsense', 'nonunion',
 'nonwhite', 'noodling', 'noondays', 'noontide', 'noontime', 'normally', 'normalcy',
 'northern', 'nosegays', 'nosiness', 'nostrils', 'nostrums', 'notables', 'notaries',
 'notarize', 'notation', 'notching', 'notebook', 'nothings', 'noticing', 'notified',
 'notifies', 'notional', 'nouveaux', 'novelist', 'novellas', 'november', 'novocain',
 'nowadays', 'nuclease', 'nucleate', 'nucleoli', 'nucleons', 'nudities', 'nugatory',
 'nuisance', 'numbness', 'numbered', 'numerals', 'numerous', 'numerate', 'numinous',
 'numskull', 'nuptials', 'nursling', 'nurtured', 'nurtures', 'nuthatch', 'nutmeats',
 'nutrient', 'nutshell', 'nuttiest', 'nuzzling')

# Returns index of a word in a given sorted tuple, if present,
# otherwise return 'False'

# Your function MUST use BISECTION SEARCH (no marking points if you do not).  

def bisect3(wordsTuple, word):
    for i in range(0,len(wordsTuple)):
        if word==wordsTuple[i]:
            return i
    return False
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
  def test1(self):
      self.assertEqual(bisect3(wordsTuple, 'nepalese'),0)
  def test2(self):
      self.assertEqual(bisect3(wordsTuple, 'nuzzling'), 115)
  def test3(self):
      self.assertEqual(bisect3(wordsTuple, 'blueberry'), False)
  def test4(self):
      self.assertEqual(bisect3(wordsTuple, 'noontide'), 66)
          
if __name__ == '__main__':
  unittest.main(exit=True)
 
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

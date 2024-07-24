import unittest
from int_to_roman import SolutionIntToRoman
from roman_to_int import SolutionRomanToInt


class TestSolutionIntToRoman(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionIntToRoman()

    def test_int_to_roman(self):
        self.assertEqual(self.solution.intToRoman(1), "I")
        self.assertEqual(self.solution.intToRoman(4), "IV")
        self.assertEqual(self.solution.intToRoman(9), "IX")
        self.assertEqual(self.solution.intToRoman(58), "LVIII")  
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")  
        self.assertEqual(self.solution.intToRoman(2023), "MMXXIII")  
        self.assertEqual(self.solution.intToRoman(3999), "MMMCMXCIX") 

if __name__ == '__main__':
    unittest.main()

class TestSolutionRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionRomanToInt()

    def test_roman_to_int(self):
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58) 
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994) 
        self.assertEqual(self.solution.romanToInt("MMXXIII"), 2023)  
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)  

if __name__ == '__main__':
    unittest.main()
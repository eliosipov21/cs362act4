import unittest
import calc 

class testCaseAdd(unittest.TestCase):
    ####Palindrome Tests####
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
    def test_palindrome(self):
        self.assertEqual(calc.isPalindrome("aba"), True)
    def test_palindrome2(self):
        self.assertEqual(calc.isPalindrome("a"), True)
    def test_palindrome3(self):
        self.assertEqual(calc.isPalindrome(""), False)
    def test_palindrome4(self):
        self.assertEqual(calc.isPalindrome(1), False)
    def test_palindrome5(self):
        self.assertEqual(calc.isPalindrome("abababa"), True)
    def test_palindrome6(self):
        self.assertEqual(calc.isPalindrome("zabababaz"), True)
    def test_palindrome7(self):
        self.assertEqual(calc.isPalindrome("010"), True)
    

    ####Numwords tests 
    def test_numwords(self):
        res1 = calc.numWords("hello")
        self.assertEqual(res1, 1)
    def test_numwords2(self):
        res2 = calc.numWords("hello world")
        self.assertEqual(res2, 2)
    def test_numwords3(self):
        res3 = calc.numWords("")
        self.assertEqual(res3, 3)





if __name__ == '__main__':
    unittest.main()
def isPalindrome(str): 
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


def numWords(str):
    res = sum(i for i in str.split())
    return res 

def add(a,b):
    return a + b
 
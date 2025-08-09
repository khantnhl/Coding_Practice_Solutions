
def isPalindrome(self, x: int) -> bool:
    if(x < 0):
        return False

    num = 0
    temp = x
    while(temp):
        remainder = temp % 10
        temp = temp // 10
    
        num = num * 10 + remainder
    
    return(num==x)

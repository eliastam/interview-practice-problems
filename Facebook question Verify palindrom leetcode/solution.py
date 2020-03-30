def isPalindrome(s):
    n = len(s)
    if n <2:
        return True
    i = 0 
    j = n-1
    while j >= i :
        if not s[i].isalnum():
            i+=1
            continue
        if not s[j].isalnum():
            j-=1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i +=1
        j -=1
    return True
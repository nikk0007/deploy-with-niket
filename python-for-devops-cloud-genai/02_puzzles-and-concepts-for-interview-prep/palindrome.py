def isPalindrome(str):
    reversed = str[::-1]
    if str == reversed:
        print("Yes")
    else:
        print("No")

isPalindrome("qwertytrewq")            
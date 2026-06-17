def anagram(str1, str2):
    if len(str1) != len(str2):
        return "NOT an Anagram"
    else:
        for n in str1:
            try:
                str1.replace(n, "")
                str2.index(n)

            except Exception as e:
                print("Exception: " + str(e))
                return "NOT an Anagram"
            
        return("YES, Its is an Anagram")  


def anagram_short(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
  


print(anagram("abccd", "dcabc"))
print(anagram_short("abccd", "dcabc"))
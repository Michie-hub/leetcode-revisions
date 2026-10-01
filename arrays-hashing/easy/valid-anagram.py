#VALID ANAGRAM
 # CHECK IF T IS AN ANAGRAM OF S. BOTH T AND S ARE ARRAYS
 # DO THESE TWO CONTAINS THE EXACT FREQUENCIES OF ELEMENTS.
 # FIRST CHECK IF THE LENGTh IS THE SAME, THEN CHECK THE FREQUENCIES OF T AND IF EQUAL TOT THE FREQUECIES OF S THEN TRUE.
from collections import Counter
def valid_anagram(s, t):
    return Counter(s) == Counter(t)
s = ["silent"]
t = ["listen"]
print(valid_anagram(s, t))
   
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True       
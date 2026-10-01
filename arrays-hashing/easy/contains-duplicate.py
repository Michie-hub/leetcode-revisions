# CONTAINS DUPLICATE -EASY

#RETURN TRUE IN ANY VALUE IN AN ARRAY NUMS APPEARS ATLEAST TWICE

def contains_duplicate(nums):
    seen = set() #empty set to store seen values, sets only store unique values
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
nums = [1,2,3,4,1]
print(contains_duplicate(nums))
    
def group_anagram(strs):
    groups = {}
    for string in strs:
        key = ''.join(sorted(string))
        groups[key].append(string)
    return list(groups.values()) 

##contains duplicate
#return true if any value appears twice
def contains_duplicate(nums):
    set = ()
    for n in nums:
        if n in seen:
            return True
        
        set.add(n)
    return False

##Tow sum- return indices of two numbers that add up to target
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement =  target - num
        if complement in seen:
            return [seen[complement], i]
        seen[nums] = i
        
#valid anagram-check if t is an anagram of s
def valid_anagram(s, t):
    from collections import Counter
    return s.Counter == t.Counter
    
            
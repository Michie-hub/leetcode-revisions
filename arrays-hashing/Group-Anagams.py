#GIVEN AN ARRAY OF STRINGS STRS, GROUP THE ANAGRAMS TOGETHER. YOU CAN RETURN THE ANSWER IN ANY ORDER
#EXAMPLE: INPUT: STRS = ["eat","tea", "tan","ate","nat","bat"]\nutput: [["bat"],["nat","tan"],["ate", "eat","tea"]]

#constraints: ["1 <= strs.length <= 10^4", "0 <= strs[i].length <= 100", "strs[i] consists of lowercase English letters."]

def group_anagram(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))#sorting every string into a list(sorted)
        if key not in groups:
            groups[key] = []
            
        groups[key].append(s)
    return list(groups.values())    
strs = ["eat","tea", "tan","ate","nat","bat"]
print(group_anagram(strs))        
            
        
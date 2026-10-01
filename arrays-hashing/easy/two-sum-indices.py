#TWO SUM INDICES

#RETURN INDICES OF TWO NUMBERS IN AN ARRAY NUMS THAT ADD UP TO TARGET. ?? does it matter if the numbers are identical.
#given a target, we iterate through nums and add every value we encounter to the empty hash map we created. For every value we subtract from target and if we find a compliment, we return the index.

def two_sum(nums, target):
    
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return[seen[complement], i]
        seen[n] = i
nums = [2, 7, 11, 15]
target = 9        
print(two_sum(nums, target))    


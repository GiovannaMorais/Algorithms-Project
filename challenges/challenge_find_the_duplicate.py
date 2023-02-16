def find_duplicate(nums):
    if not nums: return False
    nums.sort()
    for index, num in enumerate(nums[1:], start = 1): 
        if not isinstance(num, int) or num < 0:
            return False
        if nums[index - 1] == nums[index]:
            return num
    return False
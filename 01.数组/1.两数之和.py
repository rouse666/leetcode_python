def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
                return [i, j]

    return []


target1 = 5
nums1 = [2, 3, 4, 1]
twoSum(nums1,target1)


def maxSubArray(nums):
    curr = nums[0]
    maxi = nums[0]

    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        maxi = max(maxi, curr)

    return maxi

arr = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(arr))
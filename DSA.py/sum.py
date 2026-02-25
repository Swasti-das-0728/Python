from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target value: "))

    sol = Solution()
    print("Indices:", sol.twoSum(nums, target))
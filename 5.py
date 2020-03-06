class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        return nums[k - 1]


if __name__ == '__main__':
    l = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    print(solution.findKthLargest(nums=l, k=k))

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        i = 0
        pairs = 0
        res = 0
        for j in range(len(nums)):
            pairs += count[nums[j]]
            count[nums[j]] += 1
            while pairs >= k:
                res += len(nums) - j
                count[nums[i]] -= 1
                pairs -= count[nums[i]]
                i += 1

        return res
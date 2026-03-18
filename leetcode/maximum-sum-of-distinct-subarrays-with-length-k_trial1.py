class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        i = 0
        current_sum = 0
        max_sum = 0
        for j in range(len(nums)):
            current_sum += nums[j]
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            if j - i + 1 > k:
                current_sum -= nums[i]
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                i += 1
            if j - i + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_i = arr.index(size)
            if max_i != size - 1:
                if max_i != 0:
                    ans.append(max_i + 1)
                    arr[:max_i + 1] = arr[:max_i + 1][::-1]
                ans.append(size)
                arr[:size] = arr[:size][::-1]

        return ans
            
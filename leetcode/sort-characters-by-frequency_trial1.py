class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        result = ""
        for i, j in count.most_common():
            while(j > 0):
                result += i
                j -= 1
        return result
        
        
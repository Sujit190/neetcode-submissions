class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash  = {}
        for i in nums:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1
        
        freq_list = []
        for n, val in hash.items():
            freq_list.append((val, n))
        
        freq_list.sort(reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(freq_list[i][1])
        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleFrq = dict()

        for num in nums:
            eleFrq[num] = eleFrq.get(num, 0) + 1
        
        eleList = list()

        for num, cnt in eleFrq.items():
            eleList.append([cnt, num])
        
        eleList.sort(reverse=True)

        res = list()
        for i in range(len(eleList)):
            if len(res) < k:
                res.append(eleList[i][1])
        return res
class Solution(object):
    def topKFrequent(self, nums, k):
        if not nums:
            return None
        elif not k:
            return []

        res = []
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        for j in range(k):
            max_key = max(dic, key=dic.get)
            dic[max_key] = 0
            res.append(max_key)

        return res

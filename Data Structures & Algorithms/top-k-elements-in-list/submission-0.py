class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1. Count frequencies
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 2. Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # 3. Put numbers into their frequency bucket
        for num, freq in count.items():
            buckets[freq].append(num)

        # 4. Collect the top k
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        return result        
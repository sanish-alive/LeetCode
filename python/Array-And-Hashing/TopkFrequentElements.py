from collections import defaultdict

def topKFrequent(nums, k):
    hash_table = defaultdict(int)

    for i in nums:
        hash_table[i] += 1

    sorted_number = sorted(hash_table.keys(), key = lambda x: hash_table[x], reverse=True)

    return sorted_number[:k]

print(topKFrequent([1,1,1,2,2,3], 2))
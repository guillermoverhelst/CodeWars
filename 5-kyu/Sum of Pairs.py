#First solution
def sum_pairs(ints, s):
    seen = {}
    for i, num in enumerate(ints):
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen[num] = i
    return None

#better solution
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

print(sum_pairs([11, 3, 7, 5], 10))
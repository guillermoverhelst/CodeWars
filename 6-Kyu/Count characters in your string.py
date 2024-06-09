#First solution
def count(s):
    char_count = {}
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count
print(count("aba"))

#Better solution
def count2(s):
    return { i : s.count(i) for i in s}
print(count2("aba"))
#First Solution
def zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        print(n)
        i *= 5
    return count

print(zeros(6))
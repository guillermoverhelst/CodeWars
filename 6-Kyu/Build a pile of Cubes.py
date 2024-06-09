#First solution
def find_nb(m):
    n = 0
    i = 0
    while(n < m):
        n += i**3
        if n == m:
            return i
        i += 1
    return -1

print(find_nb(1071225))
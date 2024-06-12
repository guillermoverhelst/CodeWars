#Fist Solution
def smallest(n):
    s = str(n)
    length = len(s)
    min_number = n
    min_i = 0
    min_j = 0
    
    for i in range(length):
        for j in range(length):
            if i != j:
                temp_list = list(s)
                digit = temp_list.pop(i)
                temp_list.insert(j, digit)
                new_number = int(''.join(temp_list))
                if new_number < min_number or (new_number == min_number and i < min_i) or (new_number == min_number and i == min_i and j < min_j):
                    min_number = new_number
                    min_i = i
                    min_j = j

    return [min_number, min_i, min_j]

#Better solution
def smallest2(n):
	s = str(n)
	min1, from1, to1 = n, 0, 0
	for i in range(len(s)):
		removed = s[:i] + s[i+1:]
		for j in range(len(removed)+1):
			num = int(removed[:j] + s[i] + removed[j:])
			if (num < min1):
				min1, from1, to1 = num, i, j
	return [min1, from1, to1]
print(smallest(261235))

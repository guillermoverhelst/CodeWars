#First solution
def solution(number):
    numbers = []
    if number <= 0:
        return 0
    else:
        for i in range(number-1,1,-1):
            if i%3 == 0 or i%5 == 0:
                numbers.append(i)
        
        return sum(numbers)
    
print(solution(10))

#Other solution
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
  
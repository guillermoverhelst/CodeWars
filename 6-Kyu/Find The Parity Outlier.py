#first solution
def find_outlier(integers):
    evenscounter = sum(integers.count(i) for i in integers if i % 2 == 0)
    oddscounter = sum(integers.count(i) for i in integers if i % 2 != 0)
    if evenscounter < oddscounter :
        return ([i for i in integers if i % 2 == 0]).pop()
    else:
        return ([i for i in integers if i % 2 != 0]).pop()

print(find_outlier([2, 4, 6, 8, 10, 3]))

#Better solution
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
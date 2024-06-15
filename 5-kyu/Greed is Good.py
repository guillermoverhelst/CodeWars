#First soltuion
def score(dice):
    counting_dices = {}
    score = 0
    counter = 0
    for i in dice:
        if i in counting_dices:
            counter = counting_dices[i][0] + 1
            score = counting_dices[i][1]
            if i == 1:
                score += 100
                if counter == 3:
                    score = 1000
            if i == 5:
                score += 50
                if counter == 3:
                    score = 500
            
            if counter == 3:
                if i == 2:
                    score = 200
                elif i == 3:
                    score = 300
                elif i == 4:
                    score = 400
                elif i == 6:
                    score = 600
            
            counting_dices[i] = [counter,score]
        else:
            score = 0
            if i == 1:
                score = 100
            if i == 5:
                score = 50
            counter = 1
            counting_dices[i] = [counter, score]

    
    return sum(counting_dices[i][1] for i in counting_dices)

print(score([1, 1, 1, 3, 1]))

#better solution
def score2(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 
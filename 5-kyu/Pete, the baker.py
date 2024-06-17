def cakes(recipe, available):
    cake_counter = 0
    cake = 0 
    for i in available:
        for j in recipe:
            if i == j:
                while(available[i] - recipe[j]) >= 0:
                    available[i] = available[i] - recipe[j]
                    cake_counter += 1
                 

    if cake_counter == len(recipe):
        cake += 1
    return available

def cakes(recipe, available):
    min_cakes = float('inf')
    
    for ingredient, amount_needed in recipe.items():
        if ingredient not in available:
            return 0
        available_amount = available[ingredient]
        cakes_possible = available_amount // amount_needed
        if cakes_possible < min_cakes:
            min_cakes = cakes_possible
            
    return min_cakes

def cakes(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
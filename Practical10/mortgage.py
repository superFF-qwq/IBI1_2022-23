## for task1: Mortgage affordability calculator

def checkpurchase(cost, salary):
    return cost <= salary*5
## define a function to check the relationship between salary and cost

value = 180000
salary = 35000

if checkpurchase(value, salary):
    orint('yes')
else:
    print('No')
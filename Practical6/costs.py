import numpy as np
import matplotlib.pyplot as plt
#use abbreviations

_costs = [1,8,15,7,5,14,43,40]
_OlympicGames = ["Los Angeles 1984", "Seoul 1988", "Barcelona 1992", "Atlanta 1996", "Sydney 2000", "Athens 2003", "Beijing 2008", "London 2012"]
#initialise data

data = zip(_costs, _OlympicGames)
data = sorted(data)
#sort data by the first key "costs"

costs = [item[0] for item in data]
OlympicGames = [item[1] for item in data]
#take out costs and corresponding games

#print(costs)
#print(OlympicGames)

n = len(data)
ind = np.arange(n)

plt.bar(ind, costs, width = 0.35)
plt.ylabel("Costs(in $ billions)")
plt.title("Costs of Olympic Games")
plt.xticks(ind, OlympicGames)
plt.yticks(np.arange(0,41,5))

#draw the bar plot and set proper parameters

plt.show()
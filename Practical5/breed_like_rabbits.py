generation = 1
rabbits = 2
while(True):
	if(rabbits > 100):
		break
	generation += 1
	rabbits = rabbits * 2
print("At generation "+str(generation)+" over 100 rabbits have been born")
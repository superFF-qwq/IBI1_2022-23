generation = 1 # initialise generation = 1
rabbits = 2 # initialise rabbits number = 2
while(True):
	if(rabbits > 100): # if rabbits exceed 100, then break
		break
	generation += 1
	rabbits = rabbits * 2 # every two rabbits will have 2 babies
print("At generation "+str(generation)+" over 100 rabbits have been born") # print answer
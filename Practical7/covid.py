import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#print(os.getcwd())
#print(os.listdir())

covid_data = pd.read_csv("full_data.csv") ######portfolio task1 : read csv

#print(covid_data.head(5))

#print(covid_data.info())

#print(covid_data.describe())

#print(covid_data.iloc[0,1])
#print(covid_data.head(2))

#print(covid_data.iloc[2,0:5])
#print(covid_data.head(6))

#print(covid_data.iloc[0:2,:])
#print(covid_data.head(3))

#print(covid_data.iloc[0:10:2,0:5])
#print(covid_data.head(11))

print(covid_data.iloc[0:1000:100,2]) ######portfolio task2 : show lines

#print(covid_data.iloc[0:3,[0,1,3]])
#my_columns = [True, True, False, True, False, False]
#print(covid_data.iloc[0:3,my_columns])

#print(covid_data.loc[2:4,"date"])

#print(covid_data.loc[0:81,"total_cases"])
#print(covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"])

my_rows = covid_data["location"]=="Afghanistan"
print(covid_data.loc[my_rows,"total_cases"])	######profolio task3 : use boolean

#print(covid_data.loc[covid_data["date"]=="2020-03-31",["location","new_cases","new_deaths"]])


new_data = covid_data.loc[covid_data["date"]=="2020-03-31",["location","new_cases","new_deaths"]]
#print(new_data.head())
print(new_data.describe())	###portfolio task4 : calculate mean value
###### The result shows:
###### mean of new cases : 640.461538
###### mean of new deaths : 37.928205

plt.boxplot([new_data["new_cases"],new_data["new_deaths"]],
	vert = True,
	whis = 1.5,
	patch_artist = True,
	meanline = False,
	showbox = True,
	showcaps = True,
	showfliers = False,
	notch = False,
	labels = ["new_cases","new_deaths"])
plt.show()	######portfolio task5 : draw a boxplot

world_dates = covid_data["date"]
world_new_cases = covid_data["new_cases"]
plt.plot(world_dates,world_new_cases,'bo')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title("new cases in the world")
plt.xlabel("date")
plt.ylabel("cases")
plt.show()	######profolio task6 : draw a boxplot

cases = covid_data.loc[covid_data["date"]=="2020-03-31","total_cases"]
#print(cases)
#print(type(cases))
#plt.boxplot(cases)
plt.boxplot(cases,
	vert = True,
	whis = 1.5,
	patch_artist = True,
	meanline = False,
	showbox = True,
	showcaps = True,
	showfliers = False,
	notch = False)
plt.title("total cases in different countries")
plt.xlabel("date:2020-03-31")
plt.show()	######profolio task7 : answer the question
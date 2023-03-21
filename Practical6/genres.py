import matplotlib.pyplot as plt

labels = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show

genres = {'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War': 7}

input='Comedy' # input is a variable that stores the input string.
ans = genres[input]
print(ans)
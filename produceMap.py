import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

myArray = np.empty([87 , 87], dtype= int)
x = 0
y = 0
with open('D:\\ContactProtein\\Log1\\Log1Result.dataset','r', encoding='UTF8') as result:
    for lines in result:
        line = lines.split(" ")
        if len(line) <= 1:
            continue
        y = 0
        for value in range(0, len(line)-1):
            #print(line[value])
            myArray[x][y] = int(line[value])
            y += 1
        x += 1
ax = sns.heatmap(myArray, cmap= "YlGnBu")
plt.show()


from sklearn import metrics
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

y_pred = []
with open('D:\\ContactProtein\\Log3\\Log3Result.dataset','r', encoding='UTF8') as result :
    for lines in result:
        line = lines.split(" ")
        if (len(lines) <=1):
            continue
        for x in range(0, len(line)-1):
            y_pred.append(line[x])
#print(y_pred)

y_true = []
with open ('D:\\ContactProtein\\originalProtein\\prova.dataset','r', encoding= 'UTF8') as f:
    for lines2 in f:
        line2 = lines2.split(" ")
        if (len(lines2) <=1):
            continue
        for count in range(0, len(line2)-1):
            y_true.append(line2[count])

# print(metrics.confusion_matrix(y_true, y_pred))
ax = sns.heatmap(metrics.confusion_matrix(y_true, y_pred), cmap= "Greens")
plt.show()
#print(metrics.classification_report(y_true, y_pred, digits=10))

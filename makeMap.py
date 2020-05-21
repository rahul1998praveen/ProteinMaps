import pandas as pd
import math
from scipy.spatial import distance

with open('D:\\ContactProtein\\Log3\\Log3Result.dataset','w', encoding='UTF8') as result :
    with open('D:\\ContactProtein\\Log3\\prova.dataset.prediction', 'r', encoding='UTF8') as file:
        for lines in file:
            line = lines.split(" ")
            #print(type(line))
            values = []
            index = 0
            counter =0
            count = 0
            if len(line) <= 1:
                result.write(line[0])
                continue
            for x in range(0, len(line)):
                values.append(line[x])
                count += 1
                counter += 1
                if count >= 10:
                    print(values.index(str(max(float(sub) for sub in values))))
                    #print(values)
                    result.write(str(values.index(str(max(float(sub) for sub in values)))))
                    result.write(" ")
                    values = []
                    count = 0
                    continue
            result.write("\n")
print(counter)



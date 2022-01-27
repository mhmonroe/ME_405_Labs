# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:37:03 2022

@author: monro
"""

''' @file HW0x00.py
    @breif   Takes csv
    @details This code takes a cs
    @author  Marcus Monroe
    @date    January 8, 2022
'''



import matplotlib.pyplot as plt



# I would like to thank GeeksforGeeks and stackoverflow for some inspiration
# https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
# https://stackoverflow.com/questions/32327936/how-to-load-data-from-a-csv-file-without-importing-the-csv-module-library

x = []
y = []
  
with open('eric.csv', 'r') as f:
    plot = []
    stripped_plot = []
    stripped_plot_row = []
    for line in f:
            words = line.split(',')
            plot.append((words[0], words[1]))
    for row in plot:
        print(row)
        for h in row:
            print(h)
            h.strip()
            print(h)
            stripped_plot_row.append(h)
        stripped_plot.append(stripped_plot_row)
        
    for row in stripped_plot:
 
        for k in row[0]:
            aa = k.isdigit()
        for j in row[1]:
            bb = j.isdigit()
            print(row[1])
            print(j)

        if aa or bb:
            if aa:
                x.append(row[0])
                
            else:
                x.append(str(0))
            
            if bb:
                y.append(row[1])
                
            else:
                y.append(str(0))
        else:
            pass
print(x)
print(y)
plt.bar(x, y, color = 'g', width = 0.72, label = "Airspeed")
plt.xlabel('Swallow weight, [kg]')
plt.ylabel('Airspeed, [mph]')
plt.title('Airspeed of an unladen swallow')
plt.legend()
plt.show()

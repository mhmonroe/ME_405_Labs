''' @file HW0x00.py
    @breif   Takes csv file data and creates a bar chart
    @details This code takes a csv file, only looks at the first two columns,
             takes the valid data, and plots it on a Monty Python themed
             bar graph
    @author  Marcus Monroe
    @date    January 14, 2022
'''


import matplotlib.pyplot as plt



# I would like to thank GeeksforGeeks and stackoverflow for some inspiration
# https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
# https://stackoverflow.com/questions/32327936/how-to-load-data-from-a-csv-fi
# le-without-importing-the-csv-module-library



# Establishing the first two columns to be printed
x = []
y = []
 
# Reading csv file data and assigning it to x and y variables 
with open('marcus.csv', 'r') as f:
    
    # Assigning csv data to the plot variable
    plot = []
    for line in f:
            words = line.split(',')
            plot.append((words[0], words[1]))
      
    for row in plot:
        # Determining if the data is correct numeric type
        try:
            row[0] == float(row[0])
            aa = True
        except:
            aa = False
        try:
            row[1] == float(row[1])
            bb = True
        except:
            bb = False
         
        # Appending data based on if data is correct
        if aa and bb:
            x.append(row[0])
            y.append(row[1])
                
        elif aa and bb==False:
            x.append(row[0])
            y.append(str(0))
            
        elif aa==False and bb:
            y.append(row[1])
            x.append(str(0))
                
        else:
            # This adds nothing to the data list if both columns have
            # incomplete data.
            pass
        
# Plotting appropiate data
   
plt.bar(x, y, color = 'g', width = 0.72, label = "Airspeed")
plt.xlabel('Swallow weight, [kg]')
plt.ylabel('Airspeed, [mph]')
# Please note this is an African swallow
plt.title('Airspeed of an unladen swallow') 
plt.legend()
plt.show()


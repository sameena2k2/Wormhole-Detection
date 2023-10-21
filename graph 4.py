# importing the required module
import matplotlib.pyplot as plt

# lambda=5
x1 = [5.2,6,7,8,9,10,11,12,13]
y1 = [1.5,0.1,0.3,0.1,0.4,0.1,0.2,0.1,0.25]
plt.plot(x1, y1, label = "line 1")
plt.plot(x1, y1, color='green',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# lambda=6
x2 = [5.2,6,7,8,9,10,11,12,13]
y2 = [0.9,0.1,0.2,0.1,0.15,0.1,0.15,0.1,0.15]
plt.plot(x2, y2, label = "line 2")
plt.plot(x2, y2, color='red',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# lambda=7
x3 = [5.2,6,7,8,9,10,11,12,13]
y3 = [0.75,0.1,0.15,0.1,0.10,0.1,0.1,0.1,0.1]
plt.plot(x3, y3, label = "line 2")
plt.plot(x3, y3, color='pink',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)

# naming the x axis
plt.xlabel('avg_degree')
# naming the y axis
plt.ylabel('avg_number of false positives')

# giving a title to my graph
plt.title('grid_QUDG')

# function to show the plot
plt.show()

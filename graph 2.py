# importing the required module
import matplotlib.pyplot as plt

# lambda=5
x1 = [7.2,8,9,10,11,12,13]
y1 = [11,4.5,1.8,1.4,1.8,1.4,1.2]
plt.plot(x1, y1, label = "line 1")
plt.plot(x1, y1, color='green',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# lambda=6
x2 = [7,8,9,10,11,12,13]
y2 = [7.2,3.9,1.6,1.3,1.3,1.0,0.5]
plt.plot(x2, y2, label = "line 2")
plt.plot(x2, y2, color='red',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# lambda=7
x3 = [7,8,9,10,11,12,13]
y3 = [5.2,3.2,1.4,1.3,1.0,1.0,0.5]
plt.plot(x3, y3, label = "line 2")
plt.plot(x3, y3, color='pink',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)

# naming the x axis
plt.xlabel('avg_degree')
# naming the y axis
plt.ylabel('avg_number of false positives')

# giving a title to my graph
plt.title('Random_QUDG')

# function to show the plot
plt.show()

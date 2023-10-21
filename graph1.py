# importing the required module
import matplotlib.pyplot as plt

# lambda=5
x1 = [7,8,9,10,11,12,13]
y1 = [22,15,13,9,5,3,3]
plt.plot(x1, y1, label = "line 1")
plt.plot(x1, y1, color='green',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# lambda=6
x2 = [7,8,9,10,11,12,13]
y2 = [16,10,9,6,3,2,1]
plt.plot(x2, y2, label = "line 2")
plt.plot(x2, y2, color='red',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# lambda=7
x3 = [7,8,9,10,11,12,13]
y3 = [14,8,6,4,2,1,1]
plt.plot(x3, y3, label = "line 2")
plt.plot(x3, y3, color='pink',  linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)

# naming the x axis
plt.xlabel('avg_degree')
# naming the y axis
plt.ylabel('avg_number of false positives')

# giving a title to my graph
plt.title('Random_UDG')

# function to show the plot
plt.show()

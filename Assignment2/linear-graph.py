"""

1- Draw the lines  y=2x+1,  y=2x+2,  y=2x+3 in the same figure. Use different drawing colors and line types for your graphs to make them stand out
in black and white. Set the image title and labels for the horizontal and vertical axes.

"""
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,100,20)
y1= 2*x + 1
plt.plot(x,y1, color="red", linestyle="--",linewidth=5,label="y = 2x + 1")

y2= 2*x + 2
plt.plot(x,y2, color="green", linestyle="-.",linewidth=3, label="y = 2x + 2")

y3= 2*x + 3
print(y3)
plt.plot(x,y3, color="blue", linestyle=":",linewidth=4,label="y = 2x + 3")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y=2x+1, y=2x+2, y=2x+3')
plt.legend()
plt.show()





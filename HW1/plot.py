import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-10,10,0.1)
y = x**2
plt.plot(x,y)
plt.fill_between(x,y,100)
plt.xlabel('x')
plt.savefig("plot1.png")

plt.figure()
x = np.arange(-2*(np.pi),2*(np.pi),0.1)
y = np.sin(x)
plt.plot(x,y)
plt.fill_between(x,y,2)
plt.xlabel('x')
plt.savefig("plot2.png")

x = np.arange(-10,10,0.1)
y = np.arange(-10,10,0.1)
X,Y = np.meshgrid(x,y)
Z = (X*Y)**2
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("plot3.png")

plt.figure()
plt.contour(X,Y,Z,10, colors='black')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("plot4.png")
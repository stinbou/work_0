# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
a = [4,5,6]
print(type(a))
print(a.shape)
print(a[0])
b = [[4,5,6],[1,2,3]]
print(b.shape)
print(b[0,0],b[0,1],b[1,1])
a = pd.zeros([3,3],dtype = int)
b = pd.ones([4,5],dtype = int)
c = pd.diag(1,1,1,1)
d = pd.radom.radom(3,2)
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a)
print(a[2,3],a[0,0])


print(b)
print(b[0,0])
c =
print(c[o,-1])
a = [[1,2],[3,4],[5,6]]
print(a[[0, 1, 2], [0, 1, 0]])
a = np.arange(1,13).reshape(4,3)
print(a[0,0],a[1,2],a[2,0],a[3,1])

x = np.array([1,2])
print(type(x))
x = np.array([1.0,2.0])
print(type(x))
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x + y)
print(np.add(x,y))
print(x - y)
print(np.subtract(x,y))
print(x * y)
print(np.multiply(x,y))
print(np.dot(x,y))
print(np.divide(x,y))
print(np.sqrt(x))
print(x.dot(y))
print(np.dot(x,y))

x = np.arange(0,100,0.1)
y = x * x
plt.title("graph0")
plt.plot(x,y)
plt.show
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.polt(x,y)
plt.show
y = np.cos(x)
plt.polt(x,y)
plt.show



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import matplotlib.pyplot as plt
import numpy as np
x_val=np.array([1,2,3,4,5,6])
y_val=np.array([6,7,7,8,8,4])
# plt.plot(x_val,y_val,marker='D',linestyle='dashed',color='r',linewidth='10')
plt.plot(x_val,y_val,marker='D',linestyle='dotted',color='r')
plt.xlabel("x value")
plt.ylabel("y label")
plt.title("Title for plot")
plt.grid(axis='y',linewidth='5',color='b')
plt.show() 

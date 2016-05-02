import os
import json
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [1, 3, 7, 13, 21]
n = len(x)

def Numerator(isAverage = True):
    if isAverage:
        xVal = np.mean(x)
        yVal = np.mean(y)
        p = []
        for i in range(len(y)):
            p.append(x[i] * y[i])
        xyVal = np.mean(p)
        return xyVal - xVal * yVal
    else:
        xVal = np.sum(x)
        yVal = np.sum(y)
        p = []
        for i in range(len(y)):
            p.append(x[i] * y[i])
        xyVal = np.sum(p)
        return xyVal - n**-1 * (xVal * yVal) 

def Divisor(isAverage = True):
    if isAverage:
        xVal = np.mean(x)
        p = []
        for i in range(len(y)):
            p.append(x[i]**2)
        x2Val = np.mean(p)
        return x2Val - xVal**2
    else:
        xVal = np.sum(x)
        p = []
        for i in range(len(y)):
            p.append(x[i]**2)
        x2Val = np.sum(p)
        return x2Val - n**-1 * xVal**2    

def Intercept(slope, isAverage = True):
    if isAverage:
        xVal = np.mean(x)
        yVal = np.mean(y)
    else:
        xVal = np.sum(x)
        yVal = np.sum(y)
        
    return yVal - slope * xVal

def Update_line(num, data, line):
    line.set_data(data)
    return line

def OpenFile(filename):
    with open(os.getcwd()+filename) as f:
        #Read json
def DrawGraph():
    #Using slope interept form
    slope = Numerator() / Divisor()
    intercept = Intercept(slope)
    
    xline = []
    yline = []
    for vx in range(len(x)):
        vy = slope * vx + intercept
        if vx == 0 or vx == len(x) - 1:
            xline.append(vx)
            yline.append(vy)
        #print (vx, vy)
    
    #Plot the input verticies
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'bo')
    #Plot the closed solution
    plt.plot(xline, yline)
    #Boilerplate
    plt.xlabel('input_x')
    plt.ylabel('input_y')
    plt.title('Closed set solution to singular regression')
    #plt.savefig('example.png')
    plt.show()

DrawGraph()
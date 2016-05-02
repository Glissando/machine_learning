import os
import json
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [1, 3, 7, 13, 21]
n = len(x)

#helper functions
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

def slope_intercept_form(mx, b):
    return mx + b
    
def OpenFile(filename):
    pass
    #with open(os.getcwd()+filename) as f:
        #Read json
def DrawGraph():
    #Using slope interept form
    slope = Numerator() / Divisor()
    intercept = Intercept(slope)
    
    #Create the line segment
    xline = []
    yline = []
    
    xline.append(0)
    yline.append(slope_intercept_form(0, intercept))
    
    xline.append(len(x) - 1)
    yline.append(slope_intercept_form(slope * (len(x) - 1), intercept))
    
    #Debugging
    #for vx in range(len(x)):
        #vy = slope * vx + intercept
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
    #plt.savefig('closed_set.png')
    plt.show()

DrawGraph()
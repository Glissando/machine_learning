
import numpy as np
import matplotlib.pyplot as plt

x = [4.87*(10**-6), 5.4*(10**-6), 6.06*(10**-6), 6.89*(10**-6), 8*(10**-6), 9.52*(10**-6)]
y = [100.3, 111.6, 124.3, 139.8, 158.2, 174.9]
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
    
    xline.append(x[len(x)-1])
    yline.append(slope_intercept_form(slope * x[len(x)-1], intercept))
    print(slope*x[len(x)-1])
    #Debugging
    #for vx in range(len(x)):
        #vy = slope * vx + intercept
        #print (vx, vy)
    
    #Plot the input verticies
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'bo')
        print(x[i])
    #Plot the closed solution
    plt.plot(xline, yline)
    #Boilerplate
    plt.xlabel('Inverse Volume')
    plt.ylabel('Pressure')
    plt.title('Graph of Pressure and Inverse Volume')
    plt.savefig('pv_diagram.png')
    #plt.xlim([0,0.00001])
    plt.show()

DrawGraph()
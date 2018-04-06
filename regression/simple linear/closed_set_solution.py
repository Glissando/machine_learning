
import numpy as np
import matplotlib.pyplot as plt

x = [3.03*(10**-2), 1*(10**-3), 2.2*(10**-2), 1*(10**-2), 4.5*(10**-2), 8.3*(10**-2)]
y = [1.6*(10**-3), 6.1*(10**-3), 26.1*(10**-3), 56.7*(10**-3), 0.23, 0.30]
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
    print(slope)
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
    plt.xlabel('Inverse resistance')
    plt.ylabel('Current')
    plt.title('Graph of Current and Inverse Resistance')
    plt.savefig('pv_diagram.png')
    xLowerBound = x[x.index(min(x))]
    xUpperBound = x[x.index(max(x))]
    yLowerBound = y[y.index(min(y))]
    yUpperBound = y[y.index(max(y))]
    plt.xlim([xLowerBound - 0.1*xLowerBound, xUpperBound + 0.1*xUpperBound])
    plt.ylim([yLowerBound - 0.1*yLowerBound, yUpperBound + 0.1*yUpperBound])
    plt.show()

DrawGraph()
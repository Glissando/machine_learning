import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

x = [0, 1, 2, 3, 4]
y = [1, 3, 7, 13, 21]
n = len(x)
initial_intercept = 0
initial_slope = 0
#The derivative of the cost for the intercept is the sum of the errors
#The derivative of the cost for the slope is the sum of the product of the errors and the input

def NegateList(list):
    a = []    
    for i in range(len(list)):
        a.append(-list[i])
    return a

def UpdatePredictions(predictions, slope, intercept):
    for i in range(n):
        predictions[i] = slope * i + intercept

def GradientDescent():
    intercept = initial_intercept
    slope = initial_slope
    step_size = 0.05
    tolerance = 0.01
    
    predictions = list(range(n))
    UpdatePredictions(predictions, slope, intercept)
    errors = NegateList(y)
    magnitude = float("inf")
    
    plt.xlabel('dependent variable')
    plt.ylabel('independent variable')
    
    plt.title('gradient descent solution to singular regression')
    
    while(magnitude > tolerance):
        #Update intercept
        error_sum = np.sum(errors)
        adjustment = step_size * error_sum
        intercept = intercept - adjustment
        
        #Update slope
        sum = []
        for i in range(len(errors)):
            sum.append(errors[i] * x[i])
        sum = np.sum(sum)
        adjustment = step_size * sum
        slope = slope - adjustment
        magnitude = math.sqrt(error_sum**2 + sum**2)
        
        #Calculate predictions and errors
        for i in range(n):
            predictions[i] = slope * i + intercept
            errors[i] = predictions[i] - y[i]
            #print(errors[i])
        
        #print(magnitude)
    
    for i in range(len(predictions)):
        print(predictions[i])

GradientDescent()
#fig = plt.figure()

#descentAni = anim.FuncAnimation(fig,)

#descentAni.save('gradient_descent_example.mp4')
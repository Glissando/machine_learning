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

def Sum(list):
    m = 0
    for i in range(list):
        m += list[i]
    return m

def Mean(list):
    return Sum(list) / n

def NegateList(list):
    a = []    
    for i in range(len(list)):
        a.append(-list[i])
    return a

def GradientDescent():
    intercept = initial_intercept
    slope = initial_slope
    step_size = 0.05
    tolerance = 0.01
    
    predictions = []
    errors = NegateList(y)
    magnitude = float("inf")
    
    while(magnitude > tolerance):
        #Update intercept
        error_sum = Sum(error)
        adjustment = step_size * error_sum
        intercept = intercept - adjustment
        
        #Update slope
        sum = []
        for i in range(len(errors)):
            a.append(errors[i] * x[i])
        sum = Sum(sum)
        adjustment = step_size * sum
        magnitude = math.sqrt(error_sum**2 + sum**2)
        
        #Calculate predictions and errors
        for i in range(len(x)):
            predictions[i] = slope * i + intercept
            errors[i] = predictions[i] - y[i]
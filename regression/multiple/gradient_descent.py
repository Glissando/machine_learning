import math
import numpy as np
import matplotlib.pyplot as plt

features =        [[0,42,3,22],
                  [13,33,2,11],
                  [5,21,67,4],
                  [2,52,77,7]]

weights = [42, 3, 17, 21]

initial_weights = np.array([-47000, 1])

def get_numpy_data(features, ouput):
    pass

def regression_coefficient():
    pass

def predict_outcome(feature_matrix, weights):
    predictions = []
    #Do dot product to calculate the predicted output
    predictions = np.dot(feature_matrix, weights)
    return predictions

def prediction_error(predictions, output):
    return np.subtract(predictions, output)

def feature_derivative(error, feature):
    return np.dot(feature, error) * 2

#Accepts a numpy feature_matrix 2D array, a 1D output array,
#an array of initial weights, a step size and a convergence tolerance.
def gradient_descent(features, output, initial_weights, step_size, tolerance):
    converged = False
    weights = np.array(initial_weights)
    errors = []
    while not converged:
        predictions = predict_outcome(features, weights)
        errors = prediction_error(predictions, output)
        
        gradient_sum_squares = 0
        
        for i in range(len(weights)):
            #feature column derivative
            
            
        gradient_magnitude = math.sqrt(gradient_sum_squares)
        if gradient_magnitude < tolerance:
            converged = True
    
    return weights
    

print(predict_outcome(features, weights))
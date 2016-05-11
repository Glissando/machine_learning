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

def gradient_descent(output, initial_weights, step_size, tolerance):
    converged = False
    weights = np.array(initial_weights)
    

print(predict_outcome(features, weights))
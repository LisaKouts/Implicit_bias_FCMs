import numpy as np
import numpy.linalg as la
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

"""Sigmoid transfer function"""
def sigmoid(A, l=1, h=0):
    return 1.0 / (1.0 + np.exp(-l*(A-h)))

"""Hyperbolic transfer function"""
def hyperbolic(A):
    return np.tanh(A)

"""Rescaled transfer function"""
def rescaled(A):
    if la.norm(A)==0.0:
        return np.zeros(A.shape)
    else:
        return A / la.norm(A)

"""Recurrent reasoning process"""
def reasoning(W, A, T=50, phi=0.8, function=rescaled):
    '''
    Returns the activation values per iteration of a Fuzzy Cognitive Map. The final activation values are a proxy for implicit bias.

    Parameters
    ----------
    W: 2-D numpy array
        correlation matrix of shape (number of features, number of features)
    A: 2-D numpy array
        initial activation values for each concept/variable
    names: list
        list of feature/concept names. order should be the same as in the correlation matrix
    case: string
        name of protected attribute, the implicit influence of which is to be analyzed 
    T: integer
        default is 50, number of iterations
    phi: float 
        default is 0.8, parameter in the [0,1] interval controlling the non-linearity of the reasoning process
    '''
    
    states = np.zeros([len(A), T, len(W)])
    states[:,0,:] = A
    
    for t in range(1,T):
        A = states[:,t,:] = (phi * function(np.matmul(A, W)) + (1-phi) * states[:,0,:])

    return states

import sys
if __name__ == "__main__":
    double_args = reasoning(sys.argv)
    print("In mymodule:",double_args)
    
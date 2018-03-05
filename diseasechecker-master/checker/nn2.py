# Test the neural  network

import numpy as np
w1 = np.loadtxt('weights_W1')
w2 = np.loadtxt('weights_W2')
w3 = np.loadtxt('weights_W3')
W1 = np.matrix(w1)
W2 = np.matrix(w2)
W3 = np.matrix(w3)
X = np.matrix([[1,0]])


def sigmoid(z):
    return 1/(1+np.exp(-z))


def forward(X,w1, w2,w3):
    global W1, W2,W3, z2,a2,a2b,z3,a3,a3b,z4
    W1 = w1                                             # initialization of weights(may be redundant)
    W2 = w2
    W3 = w3
    Xt = np.vstack((1,np.transpose(X)))                 # X is a [n*1] row matrix, converting it to column matrix and adding bias-> we get Xt
    z2 = np.matmul(W1, Xt)                              # multiplying Xt with W1 to get input to hidden layer i.e. z2
    a2 = sigmoid(z2)                                    # activation on hidden layer to get output of hidden layer i.e. a2
    a2b = np.vstack((1,a2))                             # adding bias to the activation of hidden unit, we get a2b (activation of layer 2 with bias)
    z3 = np.matmul(W2,a2b)                              # multiplying a2b with W2 to get input to the output layer ie z3
    a3 = sigmoid(z3)
    a3b = np.vstack((1,a3))
    z4= np.matmul(W3, a3b)
    yHat = sigmoid(z4)                                  # applying activation to z3 to get the observed output yHat
    return(yHat)                                        # return observerd output in the order of n * 1


a = forward(X,W1,W2,W3)

print(a)

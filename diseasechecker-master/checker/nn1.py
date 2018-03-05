'''
X -> input to neural net
Y -> actual output of neural net
yHat ->  observed output of neural net
z2 -> weighted input to hidden layer
a2 -> activation on the hidden layer input z2
a2b -> activation with addition of bias
z3 -> weighted input to the output layer

'''





import numpy as np

x = np.loadtxt('refinedInput.csv')
y = np.loadtxt('refinedOutput.csv')

X =np.matrix(x)
Y =np.matrix(y)


# input and output for xor gate
#X = np.matrix([[0,0],[0,1],[1,0],[1,1]])
#Y = np.matrix([[1,0],[0,1],[0,1],[1,0]])



alpha = 4.5
training_cost = 0
inputLayerSize = 94
hiddenLayerSize1 = 85
hiddenLayerSize2 = 45
outputLayerSize = 37

#random initialization of weights
W1 = 2*np.matrix(np.random.rand(hiddenLayerSize1, inputLayerSize+1)) - 1   #W1 for input to hidden layer
W2 = 2*np.matrix(np.random.rand(hiddenLayerSize2, hiddenLayerSize1+1))- 1   #W2 for hidden to output layer
W3 = 2*np.matrix(np.random.rand(outputLayerSize, hiddenLayerSize2+1))- 1

def sigmoid(z):
    return (1/(1+np.exp(-z)))


def sigmoidPrime(z):
    s = sigmoid(z)
    return (np.multiply(s,(1-s)))
    #return np.exp(-z)/((1+np.exp(-z))**2)


# Function for forward propagation
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

def costFunction(X, Y):
    J = 0.5 * sum(np.square(X-Y))
    return J

def backPropagation(X, Y):
    global z3, W1, W2,W3, training_cost, a2b, a3b
    y = forward(X, W1, W2,W3)
    t = Y.T
    training_cost += costFunction(y,t)
    err_op = np.multiply(-(y - t) , sigmoidPrime(z4))
    dW3 = (err_op * a3b.T)
    err_l3 = np.multiply((W3.T * err_op)[1:], sigmoidPrime(z3))
    dW2 = (err_l3 * a2b.T)
    err_l2 = np.multiply((W2.T * err_l3)[1:], sigmoidPrime(z2))
    x_b = np.vstack((1, X.T ))
    dW1 = err_l2 *x_b.T
    return dW1, dW2, dW3


def weightUpdate(delW1,delW2, delW3):
    global alpha,W1,W2,W3 
    W1 = W1 + alpha * delW1                 # update the weights by values obtained from backpropagation
    W2 = W2 + alpha * delW2
    W3 = W3 + alpha * delW3

# start the training of neural net

for epoch in range(20000):
    ip = 0
    for x0 in X:  
        y0 = Y[ip]
        ip = ip + 1
        a,b,c = backPropagation(x0,y0)
        weightUpdate(a,b,c)
        print (training_cost)
        training_cost = 0

np.savetxt('weights_W1', W1)
np.savetxt('weights_W2', W2)
np.savetxt('weights_W3', W3)
print('Sucess')

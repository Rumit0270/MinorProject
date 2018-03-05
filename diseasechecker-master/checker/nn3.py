import numpy as np
import pandas as pd

def sigmoid(z):
    return 1/(1+np.exp(-z))

def forward(X,w1,w2,w3):
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


def compute(ip):
    databaseDisease = pd.read_csv('/home/phoenix/minor/checker/SmallDiseaseSet38.csv')
    databaseSymptom = pd.read_csv('/home/phoenix/minor/checker/symptomlabel.csv')

    a = np.array(databaseDisease)
    b = np.array(databaseSymptom)

    diseaseLabel = a.T[0:1]
    symptomLabel = np.delete(b[0:1], 0, axis=1)


    w1 = np.loadtxt('/home/phoenix/minor/checker/weights_W1')
    w2 = np.loadtxt('/home/phoenix/minor/checker/weights_W2')
    w3 = np.loadtxt('/home/phoenix/minor/checker/weights_W3')
    W1 = np.matrix(w1)
    W2 = np.matrix(w2)
    W3 = np.matrix(w3)

    #print(symptomLabel)
    #print(diseaseLabel)


    symptomInput = []
    inputNet = []
    symptomInput = ip.splitlines()
    

    for i in range(len(symptomInput)):
        symptomInput[i] = symptomInput[i].upper()


    for item in symptomLabel[0]:
        if item.upper() in symptomInput:
            inputNet.append(1)
        else:
            inputNet.append(0)
    #print(inputNet)

    X = np.matrix(inputNet)




    outputNet = forward(X,W1,W2,W3).T
    outputNet[np.logical_or(outputNet<0.01,outputNet>1)]=0.0
    #outputNet = np.round(outputNet)

    

    s=[]

    s = np.squeeze(np.asarray(outputNet))



    possibleDiseases = []
    counter = 0
    for j in s:
        if j != 0.0:
            possibleDiseases.append(diseaseLabel[0][counter])
        counter = counter + 1

    return(possibleDiseases)
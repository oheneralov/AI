# three layer neural network 
# uses the MNIST dataset converted into CSV
# (c) Oleksandr Heneralov, 2017
# license GPLv2

import numpy
import matplotlib.pyplot
import scipy.special # sigmoid
import neural_network

neuralNetwork = neural_network.neuralNetwork

inputNodesNum = 200*200 # 28*28
hiddenNodesNum = 1000
outputNodesNum = 2 # daisy, roses
learningRate = 0.1
# epochs is the number of times the training data set is used for training
epochs = 6

n = neuralNetwork(inputNodesNum, hiddenNodesNum, outputNodesNum, learningRate)

# load training data
#trainingDataList = n.loadDataSetMNISTCSV("mnist_dataset/mnist_train.csv")
trainingDataList = n.loadCustomImages("custom_data/training")

# --------------------------train the neural network--------------------------

print('\n--------------------------training the neural network--------------------------')

for epoch in range(epochs):
    # go through all records in the training data set
    print('epoch %s' % epoch)
    print("training images: %s" % len(trainingDataList))
    for record in trainingDataList:
        # split a record by ','
        allValues = record.split(',')
        # scale and shift the inputs
        inputs = (numpy.asfarray(allValues[1:]) / 255.0 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
        targets = numpy.zeros(outputNodesNum) + 0.01
        # allValues[0] is the target label for this record
        targets[int(allValues[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass


# load test data
#testDataList = n.loadDataSetMNISTCSV("custom_data/testing")
testDataList = n.loadCustomImages("custom_data/testing")

# --------------------------test the neural network--------------------------

print('\n--------------------------testing the neural network--------------------------')
# correctAnswersList for how well the network performs, initially empty
correctAnswersList = []

# go through all the records in the test data set
print("training images: %s" % len(testDataList))

for record in testDataList:
    # split the record by ','
    allValues = record.split(',')
    # correct answer is first value
    correctLabel = int(allValues[0])
    # scale and shift the inputs
    inputs = (numpy.asfarray(allValues[1:]) / 255.0 * 0.99) + 0.01

    # test the network
    label = n.predict(inputs)

    # append correct or incorrect to list
    if (label == correctLabel):
        # network's answer matches correct answer, add 1 to correctAnswersList
        # print("network's answer is correct %s" % label)
        correctAnswersList.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to correctAnswersList
        correctAnswersList.append(0)
        # print("Error! network's answer is %s but should be %s" % (label, correctLabel))
        pass
    
    pass

correctAnsWerAsPercentage = (sum(correctAnswersList))/(len(correctAnswersList))*100
print("accuracy = {0} %".format(correctAnsWerAsPercentage))


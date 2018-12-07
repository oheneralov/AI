import numpy
# plotting arrays library
import matplotlib.pyplot
# sigmoid function expit()
import scipy.special
import os
import glob
import imageio
from random import shuffle

class neuralNetwork:
    def __init__(self, inputNodesNum, hiddenNodesNum, outputNodesNum, learningRate):
        self.inputNodesNum = inputNodesNum
        self.hiddenNodesNum = hiddenNodesNum
        self.outputNodesNum = outputNodesNum

        # learning rate
        self.learningRate = learningRate
        
        # link weight matrices, hidden Weights and output Weights
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        self.hiddenWeights = numpy.random.normal(0.0, pow(self.inputNodesNum, -0.5), (self.hiddenNodesNum, self.inputNodesNum))
        self.outputWeights = numpy.random.normal(0.0, pow(self.hiddenNodesNum, -0.5), (self.outputNodesNum, self.hiddenNodesNum))

        # activation function : sigmoid
        #  1/(1+exp(-x))
        self.activation_function = lambda ndArray: scipy.special.expit(ndArray)
        # activation function: relu
        # max(0, x)  
        # np.maximum(0, x)
        pass

    def calculateSignals(self, weights, signalValues):
        return self.activation_function(numpy.dot(weights, signalValues))

    
    # train a neural network
    def train(self, inputsList, targetsList):
        # convert inputs list into 2d array
        inputs = numpy.array(inputsList, ndmin = 2).T
        targets = numpy.array(targetsList, ndmin = 2).T
        
        # calculate signals values got from hidden layer
        hiddenOutputs = self.calculateSignals(self.hiddenWeights, inputs)
        
        # calculate signals values got from output layer
        finalOutputs = self.calculateSignals(self.outputWeights, hiddenOutputs)
        
        # calculate loss
        outputErrors = targets - finalOutputs

        # backpropagation and gradient descend for updating weights due to errors
        hiddenErrors = numpy.dot(self.outputWeights.T, outputErrors) 
        
        self.outputWeights += self.learningRate * numpy.dot((outputErrors * finalOutputs * (1.0 - finalOutputs)), numpy.transpose(hiddenOutputs))
        
        self.hiddenWeights += self.learningRate * numpy.dot((hiddenErrors * hiddenOutputs * (1.0 - hiddenOutputs)), numpy.transpose(inputs))
        pass

    # pass to the neural network data and get the prediction (the label)
    def predict(self, inputsList):
        # convert inputs list to 2d array
        inputs = numpy.array(inputsList, ndmin = 2).T
        
        # calculate the signals got from hidden layer
        hiddenOutputs = self.calculateSignals(self.hiddenWeights, inputs)
        
        # calculate the signals got from a final output layer
        finalOutputs = self.calculateSignals(self.outputWeights, hiddenOutputs)
        return numpy.argmax(finalOutputs)

    def loadDataSetMNISTCSV(self, filename):
        dataFile = open(filename, 'r')
        dataList = dataFile.readlines()
        dataFile.close()
        return dataList

    def loadCustomImages(self, dir):
        dataset = self.images2Cifar(dir)
        return dataset

    def get_immediate_subdirectories(self, dir):
        return [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

    def get_immediate_files(self, dir):
        return [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]


    def loadImage2List(self, dir, label):
        imageFiles = self.get_immediate_files(dir)
        print("Number of files to process: " + str(len(imageFiles)))
        imagesIn1Category = []

        for image_file_name in imageFiles:
            # load image data from png files into an array
            file = './' + dir + '/' + image_file_name
            #print("Processing file: " + file)
            img_array = imageio.imread(file, as_gray=True)

            # reshape from 28x28 to 1d list of 784 values
            img_data  = img_array.reshape(40000)

            # append label and image data to a data set
            record = numpy.append(label, img_data)
            list = record.tolist()
            result = [str(int(x)) for x in list]
            csv = ",".join(result)
            imagesIn1Category.append(csv)
            shuffle(imagesIn1Category)
        return imagesIn1Category


    def images2Cifar(self, dir):
        dataset = []
        categories = self.get_immediate_subdirectories(dir)
        print("available categories: ", categories)
        for category in categories:
            print("Processing dir: " + category)
            label = categories.index(category)
            imagesList = self.loadImage2List(dir + '/' + category, label)
            dataset = dataset + imagesList

        print("Finished converting images into array")

        if len(dataset) == 0:
            print('No images found!')
            exit()

        return dataset



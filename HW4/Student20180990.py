import numpy as np
import sys
import os
import operator

def createDataSet(folder):
	file_list = os.listdir(folder)
	labels=[]
	returnMat=[] 

	for file in file_list:
		labels.append(file.split('_')[0])

		filepath = folder + '/' + file
		with open(filepath, 'r', encoding='UTF8') as f:
			line = f.readlines()
		line = [item[:-1] for item in line]
		line = ''.join(line)
		line = [float(item) for item in line]
		returnMat.append(line)
	returnMat = np.array(returnMat)
	#print(returnMat)
	#print(labels)
	return returnMat, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def calculateErrorRate(trainDataSet, trainLabels, testDataSet, testLabels, k):
	count = 0
	total = len(testDataSet) 
	for i in range(total):
		result = classify0(testDataSet[i], trainDataSet, trainLabels, k)
		if result != testLabels[i]:
			count += 1
	print(int(count/total*100))	
	
trainingDigits = sys.argv[1]
testDigits = sys.argv[2]
	
trainDataSet, trainLabels = createDataSet(trainingDigits)
testDataSet, testLabels = createDataSet(testDigits)

for k in range(1, 21):
	calculateErrorRate(trainDataSet, trainLabels, testDataSet, testLabels, k)

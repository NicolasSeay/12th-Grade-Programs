import csv
import random
import math
import operator

#Elim Sq. Ft., Use 93 - 138
def loadDataset(filename, trainingSet=[] , testSet=[]):
        i = 0
        j = 0
        with open(filename, 'rb') as csvfile:
                lines = csv.reader(csvfile)
                dataset = list(lines)
                for x in range(228):
                    for y in range(5):
                        dataset[x][y] = float(dataset[x][y])
                    dataset[x][0] = float((dataset[x][0] - 27502) / (27616 - 27502))
                    dataset[x][1] = float((dataset[x][1] - 1) / (6 - 1))
                    dataset[x][2] = float((dataset[x][2] - 1.5) / (6 - 1.5))
                    dataset[x][4] = float((dataset[x][4] - 88000) / (1009512 - 88000)) * 2
                    if ((x >= 0) and (x < 48)):
                    #if (x < 185):
                        trainingSet.append(dataset[x])
                        if(str(trainingSet[i][5]) == "Raleigh"):
                            trainingSet[i][5] = 1
                        elif(str(trainingSet[i][5]) == "Cary"):
                            trainingSet[i][5] = 2
                        elif(str(trainingSet[i][5]) == "Morrisville"):
                            trainingSet[i][5] = 3
                        elif(str(trainingSet[i][5]) == "Garner"):
                           trainingSet[i][5] = 3
                        elif(str(trainingSet[i][5]) == "Fuquay-Varina"):
                           trainingSet[i][5] = 3
                        elif(str(trainingSet[i][5]) == "Apex"):
                            trainingSet[i][5] = 4
                        del trainingSet[i][6:]
                        del trainingSet[i][3]
                        i += 1
                    elif x > 184:
                        testSet.append(dataset[x])
                        if(str(testSet[j][5]) == "Raleigh"):
                            testSet[j][5] = 1
                        elif(str(testSet[j][5]) == "Cary"):
                            testSet[j][5] = 2
                        elif(str(testSet[j][5]) == "Morrisville"):
                            testSet[j][5] = 3
                        elif(str(testSet[j][5]) == "Garner"):
                            testSet[j][5] = 3
                        elif(str(testSet[j][5]) == "Fuquay-Varina"):
                            testSet[j][5] = 3
                        elif(str(testSet[j][5]) == "Apex"):
                            testSet[j][5] = 4
                        del testSet[j][6:]
                        del testSet[j][3]
                        j += 1
                        
                        
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2) #2 because squared for distance formila
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	loadDataset('Real Estate Data for CS4 - House data.csv', trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	k = 3
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	
main()

import csv
import random
import math
import operator

def loadDataset(filename, trainingSet=[] , testSet=[]):
        with open(filename, 'rb') as csvfile:
                lines = csv.reader(csvfile)
                dataset = list(lines)
                for x in range(1000):
                    for y in range(11):
                        dataset[x][y] = float(dataset[x][y])
                    dataset[x][0] = float((dataset[x][0] - 0) / (4 - 0))        #Work Status--
                    dataset[x][1] = float((dataset[x][1] - 0) / (2 - 0))        #Divorce--
                    dataset[x][2] = float((dataset[x][2] - 3) / (20 - 3))       #Education
                    dataset[x][3] = float((dataset[x][3] - 0) / (3 - 0))        #Babies
                    dataset[x][4] = float((dataset[x][4] - 0) / (6 - 0))        #Preteen
                    dataset[x][5] = float((dataset[x][5] - 0) / (5 - 0))        #Teens
                    dataset[x][6] = float((dataset[x][6] - 500) / (50000 - 500))     #Income--
                    dataset[x][7] = float((dataset[x][7] - 0) / (5 - 0))        #Attend--
                    dataset[x][8] = float((dataset[x][8] - 0) / (20 - 0))       #TV Hours
                    dataset[x][9] = float((dataset[x][9] - 0) / (1 - 0))        #Female--
                    dataset[x][10] = float((dataset[x][10] - 0) / (1 - 0))       #Happy--
                    if (x <= 799):
                        trainingSet.append(dataset[x])
                    elif (x > 799):
                        testSet.append(dataset[x])
                        
                        
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2) #2 because squared for distance formila
	#print math.sqrt(distance)
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
	loadDataset('KNN HHI TEST DATASET.csv', trainingSet, testSet)
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

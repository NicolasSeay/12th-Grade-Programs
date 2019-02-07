from math import log
import operator
import treeplotter
import random

#what to put into the python shell:
    #import trees
    #ds,l=createDataSet()
    #calcShannonEnt(ds,l)
    #gini_index(ds,l)

def createDataSet():
    dataSet = [[1,1,0,1,1,1,'Greek'],   #1
               [1,0,1,1,1,1,'Greek'],   #2
               #[0,1,0,1,0,0,'Greek'],   #3
               [1,1,1,1,1,0,'Italian'], #4
               [1,1,1,1,1,0,'Italian'], #5
               #[0,1,0,1,1,0,'Italian'], #6
               [1,0,0,0,0,1,'Moroccan'],#7
               [1,0,0,0,0,1,'Moroccan'],#8
               [0,1,0,0,0,0,'Moroccan']]#9
               #[1,0,0,1,1,0,'American']]#10
    labels = ["dinner","sacred", "pasta", "specific drinks", "dairy", "chicken"]
    return dataSet, labels

def gini_index(classes, groups):
        # count all samples at split point
        n_instances = float(sum([len(group) for group in groups]))
        # sum weighted Gini index for each group
        gini = 0.0
        count=1
        for group in groups:
            size = float(len(group))
            # avoid divide by zero
            if size == 0:
                continue
            score = 0.0
            # score the group based on the score for each class
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            # weight the group score by its relative size

            gini = (1.0 - score) * (size / n_instances)
            print count
            print gini
            count=count+1
        return gini

    
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet,labels):
    output = []
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = gini_index(dataSet,labels)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * gini_index(subDataSet, labels)
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        #output.append(i)
        #output.append(newEntropy)
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    #output.append(int(bestFeature))
    output = int(bestFeature)-1
    return output                      #returns an integer

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet,labels)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree                            
    
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
    
ds,l = createDataSet()
tree=createTree(ds,l)
treeplotter.createPlot(tree)




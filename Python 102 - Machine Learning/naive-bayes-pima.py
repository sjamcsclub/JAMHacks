import csv, random
from sklearn.naive_bayes import GaussianNB

def loadData(filename):
    lines = csv.reader(open(filename, newline=""))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return (trainSet, copy)

def extractLabels(dataset):
    features = []
    labels = []
    for instance in dataset:
        features.append(instance[:-1])
        labels.append(int(instance[-1]))
    return (features, labels)

dataset = loadData("pima.csv")

trainData, testData = splitDataset(dataset, 0.25)

trainFeatures, trainLabels = extractLabels(trainData)
testFeatures, testLabels = extractLabels(testData)

print(len(trainLabels), len(testLabels))

classifier = GaussianNB()
classifier = classifier.fit(trainFeatures, trainLabels)

print(classifier.predict(testFeatures))

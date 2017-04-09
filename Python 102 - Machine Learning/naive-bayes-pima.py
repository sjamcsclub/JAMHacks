import csv
from sklearn.naive_bayes import GaussianNB

def loadData(filename):
    lines = csv.reader(open(filename, newline=""))
    dataset = list(lines)
    labels = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i][:-1]]
        labels[i] = dataset[i][-1]
    return dataset, labels

features, labels = loadData("pima.csv")

classifier = GaussianNB()
classifier = classifier.fit(trainFeatures, trainLabels)

print(classifier.predict(testFeatures, testLabels))

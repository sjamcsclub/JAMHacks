# Example of Naive Bayes implemented from Scratch in Python
# Source: http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
import csv
import random
import math


def mean(numbers):
	return sum(numbers) / len(numbers)

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x - avg)**2 for x in numbers]) / (len(numbers) - 1)
	return math.sqrt(variance)

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
	return [trainSet, copy]

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

def train(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.items():
		summaries[classValue] = summarize(instances)
	return summaries

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(x - mean)**2 / (2 * stdev**2))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions

def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1
	return correct/len(testSet)

def main():
	filename = "pima-indians-diabetes.data.csv"
	
	print("Loading dataset")
	dataset = loadData(filename)
	trainingSet, testSet = splitDataset(dataset, 0.5)
	
	print("Training model")
	summaries = train(trainingSet)
	
	print("Making predictions")
	predictions = getPredictions(summaries, testSet)

	accuracy = getAccuracy(testSet, predictions)
	print("Accuracy: " + str(round(accuracy*100, 4)) + "%")

main()
import random
import math

def readFromFile(inputFile):
    allSpecies = []
    f = open(inputFile, "r").read().split("\n")
    for line in f:
        allSpecies.append(line)
    return allSpecies

def chooseSpecies(originalList, pairsToCross):
    speciesToMutate = [None] * int(pairsToCross)
    alreadyChoosenOrganisms = [None] * int(pairsToCross)
    for i in range(3):
        randomOrganisms = random.choice([i for i in range(len(originalList)) if i not in alreadyChoosenOrganisms])
        alreadyChoosenOrganisms[i] = randomOrganisms
        speciesToMutate[i] = originalList[randomOrganisms]
    return speciesToMutate

def removeSpecies(orginalList, choosenSpecies):
    for species in choosenSpecies:
        while species in orginalList:
            orginalList.remove(species)
    return orginalList

def sliceChromosomes(organismsToCrossOver, pairsToCrossOver):
    separateChromosomes = [None] * pairsToCrossOver * 2
    counter = 0
    for i in range(int(len(organismsToCrossOver) / 2)):
        whereToSlice = organismsToCrossOver[i]
        whereToSlice = str(whereToSlice)
        if int(len(whereToSlice)) <= 0:
            return separateChromosomes
        firstHalfOfLine = whereToSlice[:int(len(whereToSlice) // 2)]
        separateChromosomes[counter] = firstHalfOfLine
        counter += 1
        secondHalfOfLine = whereToSlice[int(len(whereToSlice)) // 2:]
        separateChromosomes[counter] = secondHalfOfLine
        counter += 1
    return separateChromosomes

def mixLines(slicedChromosomes, pairsToCrossOver):
    alreadyMixedLines = [None] * len(slicedChromosomes)
    mixedPairs = [None] * pairsToCrossOver
    counter = 0
    for i in range(int(len(slicedChromosomes)/2)):
        firstLineToMix = random.choice([i for i in range(len(slicedChromosomes)) if i not in alreadyMixedLines])
        alreadyMixedLines[counter] = firstLineToMix
        counter += 1
        secondLineToMix = random.choice([i for i in range(len(slicedChromosomes)) if i not in alreadyMixedLines])
        alreadyMixedLines[counter] = secondLineToMix
        counter += 1
        mixedPairs[i] = str(slicedChromosomes[firstLineToMix]) + " " + str(slicedChromosomes[secondLineToMix])
    for i in range(len(mixedPairs)):
        mixedPairs = [s[1:] if s.startswith(" ") else s for s in mixedPairs]
        mixedPairs[i] = mixedPairs[i].replace("  ", " ")
        mixedPairs[i] = mixedPairs[i].replace(str(None), "")
        mixedPairs[i] = mixedPairs[i].replace("No", "")
        mixedPairs[i] = mixedPairs[i].replace("ne", "")
    return mixedPairs

def connectTwoLists(mixedLines, slicedOrginalList):
    for i in range (len(mixedLines)):
        slicedOrginalList.append(mixedLines[i])
    return slicedOrginalList

def fitnessFunction(connectedList, tresholdFunction, proLifeFunction):
    afterFitness = []
    for line in connectedList:
        numbers = [int(num) for num in line.split() if num.strip().isdigit()]
        lineSum = sum(numbers)
        cosOfLineSum = math.cos(lineSum)
        cosOfLineSum = abs(cosOfLineSum)
        if cosOfLineSum <= proLifeFunction and cosOfLineSum >= tresholdFunction:
            afterFitness.append(line)
        elif cosOfLineSum > proLifeFunction:
            afterFitness.append(line)
            afterFitness.append(line)
        else:
            continue
    return afterFitness

def saveToFile(afterFitness, outputFile):
    counter = 0
    with open(str(outputFile), "w") as file:
        for line in afterFitness:
            file.write(line)
            if counter < (len(afterFitness) - 1):
                file.write("\n")
                counter += 1

def checkIfFileExists(userInput):
    notSure = True
    while notSure:
        try:
            f = open(userInput, "r")
            f.close()
            notSure = True
            return userInput
        except FileNotFoundError:
            print("Incorrect path to file, plaese enter correct path: ")
            userInput = input()

def checkIfInt(userInput):
    while not isinstance(userInput, int):
        try:
            userInput = int(userInput)
        except ValueError:
            print("Input should be an integer value: ")
            userInput = input()
    return userInput

def checkIfFloat(userInput):
    while not isinstance(userInput, float):
        try:
            userInput = float(userInput)
        except ValueError:
            print("Input should be a float value: ")
            userInput = input()
    return userInput

def checkIfInRange(userInput):
    while float(userInput) >= 1:
        print("Value should be in range <0;1>: ")
        userInput = input()
        userInput = checkIfFloat(userInput)
    return userInput

def main():
    #-----------get-user-input-----------#
    print("Input file: ")
    inputFile = input()
    inputFile = checkIfFileExists(inputFile)
    print("Generations: ")
    generations = input()
    generations = checkIfInt(generations)
    print("Pairs to cross over: ")
    pairsToCross = input()
    pairsToCross = checkIfInt(pairsToCross)
    print("Treshold function value: ")
    tresholdFunction = input()
    tresholdFunction = checkIfFloat(tresholdFunction)
    tresholdFunction = checkIfInRange(tresholdFunction)
    print("Prolife function value: ")
    proLifeFunction = input()
    proLifeFunction = checkIfFloat(proLifeFunction)
    proLifeFunction = checkIfFloat(proLifeFunction)
    proLifeFunction = checkIfInRange(proLifeFunction)
    print("Output file: ")
    outputFile = input()
    outputFile = checkIfFileExists(outputFile)
    #----------------main----------------#
    for i in range(generations):
        orginal = readFromFile(inputFile)
        chosenOnes = chooseSpecies(orginal, pairsToCross)
        slicedOrginalList = removeSpecies(orginal, chosenOnes)
        slicedChromosomes = sliceChromosomes(chosenOnes, pairsToCross)
        mixedLines = mixLines(slicedChromosomes, pairsToCross)
        connectedList = connectTwoLists(mixedLines, slicedOrginalList)
        afterFitness = fitnessFunction(connectedList, tresholdFunction, proLifeFunction)
    saveToFile(afterFitness, outputFile)
    print("All done")

main()

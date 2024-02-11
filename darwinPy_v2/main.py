import random

def readFromFile(pathFile):
    #----------------------read-from-file-----------------------#
    with open(pathFile, "r") as file:
        chromosomesList = [line.strip() for line in file if line.strip()]
    print("Orginal: ")
    print(chromosomesList)
    return chromosomesList
    #-----------------------------------------------------------#

def chooseSpecies(chromosomeList, pairsToCrossOver):
    #--------------check-if-possible-to-cross-over--------------#
    lenght = len(chromosomeList)
    while lenght < pairsToCrossOver:
        if lenght % 2 != 0:
            lenght += 1
        lenght = lenght / 2
    #----------------main-function-of-definition----------------#
    chosenSpecies = [None] * pairsToCrossOver
    alreadyChosen = [None] * pairsToCrossOver
    for i in range(pairsToCrossOver):
        randomLine = random.choice([i for i in range(lenght) if i not in alreadyChosen])
        alreadyChosen[i] = randomLine
        chosenSpecies[i] = chromosomeList[randomLine]
    print("Chosen species: ")
    print(chosenSpecies)
    return chosenSpecies
    #-----------------------------------------------------------#

def shrinkOrginalList(chromosomeList, chosenSpecies):
     #------------------remove-chesen-species--------------------#
    for item in chosenSpecies:
        if item in chromosomeList:
            chromosomeList.remove(item)
        else:
            continue
    print("Sliced list: ")
    print(chromosomeList)
    return chromosomeList
    #-----------------------------------------------------------#

def sliceChosenSpecies(chosenSpecies, pairsToCrossOver):
    #--------------check-if-possible-to-cross-over--------------#
    lenght = len(chosenSpecies)
    if pairsToCrossOver > lenght / 2:
        pairsToCrossOver = (lenght / 2) - 2
    #----------------main-function-of-definition----------------#
    pairsToCrossOver = pairsToCrossOver * 2
    listOfSlicedChromosomes = [None] * (len(chosenSpecies) * 2)
    counter = 0
    for line in chosenSpecies:
    #----------------check-if-possible-to-slice-----------------#
        if len(line) > 1:
            mid = round(len(line) / 2)
            firstHalf = line[:mid]
            secondHalf = line[mid:]
        else:
            firstHalf = secondHalf = line
    #---------------------append-to-list------------------------#
        listOfSlicedChromosomes[counter] = firstHalf
        counter += 1
        listOfSlicedChromosomes[counter] = secondHalf
        counter += 1
    listOfSlicedChromosomes = [line.replace("  ", " ") for line in listOfSlicedChromosomes]
    listOfSlicedChromosomes = [line.strip() if line.startswith(' ') else line for line in listOfSlicedChromosomes]
    print("Sliced species: ")
    print(listOfSlicedChromosomes)
    return listOfSlicedChromosomes
    #-----------------------------------------------------------#

def mixChosenSpecies(listOfSlicedChromosomes):
    alreadyMixed = [None] * len(listOfSlicedChromosomes)
    mixed = [None] * len(listOfSlicedChromosomes)

    for i in range(len(listOfSlicedChromosomes)):
        randomLine = random.choice([i for i in range(len(listOfSlicedChromosomes)) if i not in alreadyMixed])
        alreadyMixed[i] = randomLine
        if i % 2:
            cnt = i - 1
            mixed[cnt] = (mixed[cnt] + " " + listOfSlicedChromosomes[randomLine]) if mixed[cnt] is not None else listOfSlicedChromosomes[randomLine]
        else:
            mixed[i] = listOfSlicedChromosomes[randomLine]

    mixed = [element.strip() for element in mixed if element is not None and element.strip() != ""]
    print("Mixed:")
    print(mixed)
    return mixed

def putAllTogether(shrinkedOrginalList, mixedSpecies):
    for i in range(len(mixedSpecies)):
        shrinkedOrginalList.append(mixedSpecies[i])
    print("All: ")
    print(shrinkedOrginalList)
    return shrinkedOrginalList

def saveToFile(pathFile, puttedAllTogether):
    with open("darwinPy_v2\output.txt", "w") as f:
        for item in puttedAllTogether:
            f.write(item)
            f.write("\n")

def main():
    pairsToCrossOver = 2
    pathFile = "darwinPy_v2/input.txt"
    orginalList = readFromFile(pathFile)
    toSlice = chooseSpecies(orginalList, pairsToCrossOver)
    shrinkedOrginalList =shrinkOrginalList(orginalList, toSlice)
    toMix = sliceChosenSpecies(toSlice, pairsToCrossOver)
    mixedSpecies = mixChosenSpecies(toMix)
    puttedAllTogether = putAllTogether(shrinkedOrginalList, mixedSpecies)
    saveToFile(pathFile, puttedAllTogether)

main()

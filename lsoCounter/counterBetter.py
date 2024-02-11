import dataBase as d
from datetime import datetime

def start():
    thisMonth = datetime.now().month
    f = open("punkty.txt", "a")
    f.write("\n\n" + "Month: " + str(thisMonth)+ "\n\n")
    f.close()

#ask how many times person attended for a mass
def howMany():
    times  = None
    print("How many masses: ")
    while times is None:
        times = input()
        try:
            times = int(times)
        except ValueError:
            print("{input} is not a number. Please enter correct value".format(input = times))
            times = None
    return times

#creates new list for comperison
def newListCreator(times):
    newList = [None] * times
    if 2 > times: 
        for i in range(times):
            userInput = input()
            newList[i] = userInput
    else:
        for i in range(2):
            userInput = input()
            newList[i] = userInput
    return newList

#extend list for comperison without issues
def extendList(orignalList, times):
    deafultList = orignalList.copy()
    if 2 < times:
        for i in range(times - 2):
            deafultList.append('')
    print(deafultList)
    return deafultList

#point counter
def check(deafultList, list, times):
    countPoints = 0
    if times == 0:
        countPoints -= 2
    elif 2 > times and times != 0: 
        if list[0] != deafultList[0] or list[0] != deafultList[1]:
            countPoints +=1
    else:
        for i in range(2):
            if list[i] == deafultList[i]:
                countPoints += 2
            else:
                countPoints += 1
        for i in range(times - 2):
            countPoints += 1
    return countPoints

#saves results to file
def printToFile(points, name):
    f = open("punkty.txt", "a")
    f.write(str(name) + ": " + str(points) + "\n")

def checkIfAbsentOnSunday():
    print("Sundey attendance: ")
    wasOrNot = input()
    if wasOrNot == "y":
        point = 1
    else:
        point = 0
    return point

#main function
def main():
    leng = len(d.nameUsername)
    listOfPoints = [None] * 4
    listOfPoints2 = [None] * 4
    for i in range(leng):
        name = d.nameUsername[i]
        print(str(name) + ": ")
        for j in range(4):
            print(str(d.weekNumber[j]))
            orignalList = d.masses[i]
            times = howMany()
            deafultList = extendList(orignalList, times)
            resultList = newListCreator(times)
            points = check(deafultList ,resultList, times)
            listOfPoints[j]  = points
            point = checkIfAbsentOnSunday()
            listOfPoints2[j] = point
        monthPoints = sum(listOfPoints) + sum(listOfPoints2)
        print(monthPoints)
        printToFile(monthPoints, name)

start()
main()

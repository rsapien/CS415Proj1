# Project 1 - Asymptotic Analysis of Algorithms
# Creators: Robert Sapien & Vince Bjazevic
# Date: 28 February 2020

import matplotlib.pyplot as plt
from random import *
import time

counter = 0

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibAdds(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    return fibAdds(n - 1) + fibAdds(n - 2) + 1

def PlotFib():
    fibx = []
    fiby = []
    for i in range(1, 35):
        fibx.append(i)
        fiby.append(fibAdds(i))
    print("FibValues: ", fibx)
    print("fiby: ", fiby)
    plt.scatter(fibx, fiby)
    plt.xlabel('Index of Fibonacci Number')
    plt.ylabel('Number of Additions')
    plt.title('Fibonacci Analysis')
    plt.show()




def Euclids(a, b):
    global counter
    if (b == 0):
        return a
    counter += 1
    return Euclids(b, a % b)

def PlotEuc():
    global counter
    EucX = []
    EucY = []
    for i in range(1, 35):
        a = Fibonacci(i)
        Euclids(Fibonacci(i+1), a)
        EucY.append(counter)
        EucX.append(a)
        counter = 0
    plt.scatter(EucX, EucY)
    plt.xlabel('n')
    plt.ylabel('Number of Modulo')
    plt.title('Euclids GCD Analysis')
    plt.show()


def decreaseByOne(a, n):
    if n <= 0:
        return 1
    return a * decreaseByOne(a, n - 1)


def dboMuls(a, n):
    if n <= 0:
        return 0
    return a * dboMuls(a, n - 1) + 1


def plotDBO(n):
    numMuls = []
    dbo = []

    for i in range(n):
        #dbo.append(decreaseByOne(2, i))
        dbo.append(decreaseByOne(2, i))
        numMuls.append(dboMuls(2, i))

    plt.xlabel("Decrease-By-One")
    plt.ylabel("Decrease-By-One Multiplications")
    plt.scatter(dbo, numMuls)
    plt.show()


def ComputeDBC(a, n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return (ComputeDBC(a, n / 2)) + 1
    return (ComputeDBC(a, (n - 1) / 2)) + 2


def decreaseByConstant(a, n):
    if n <= 0:
        return 1
    elif n % 2 == 0:
        return decreaseByConstant(a, n / 2) ** 2
    else:
        return a * (decreaseByConstant(a, (n - 1) / 2) ** 2)


def plotDBC(n):
    numMuls = []
    dbc = []

    for i in range(n):
        #dbc.append(decreaseByConstant(2, i))
        dbc.append(i)
        numMuls.append(ComputeDBC(2, i))

    plt.xlabel("Decrease-By-Constant")
    plt.ylabel("Decrease-By-Constant Multiplications")
    plt.scatter(dbc, numMuls)
    plt.show()


def divideConquer(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return divideConquer(a, n / 2) * divideConquer(a, n / 2)
    else:
        return a * divideConquer(a, (n - 1) / 2) * divideConquer(a, (n - 1) / 2)


def computeDivC(a, n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return computeDivC(a, n / 2) + 1
    else:
        return computeDivC(a, (n - 1) / 2) + 2


def plotDivC(n):
    numMuls = []
    divC = []

    for i in range(n):
        #divC.append(divideConquer(2, i))
        divC.append(i)
        numMuls.append(computeDivC(2, i))

    plt.xlabel("Divide-and-Conquer")
    plt.ylabel("Divide-and-Conquer Multiplications")
    plt.scatter(divC, numMuls)
    plt.show()


def SelectionSort(A):
    global counter
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            counter += 1
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

def InsertionSort(A):
    global counter
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        counter += 2
        while j >= 0 and key < A[j]:
            counter += 2
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def DefaultPlotSorts():
    testCase('B')
    testCase('A')
    testCase('W')

def testCase(test):
    list = []
    if test == 'B':
        for i in range(2, 102):
            tempList = []
            for j in range(1, i):
                tempList.append(j)
            list.append(tempList)
    elif test == 'A':
        for i in range(2, 102):
            tempList = []
            for j in range(1, i):
                tempList.append(randint(1, 1000))
            list.append(tempList)
    else:
        for i in range(102, 2, -1):
            tempList = []
            for j in range(i, i, -1):
                tempList.append(j)
            list.append(tempList)
    plotSorts(list, test)

def plotSorts(list, test):
    global counter
    xInsertSort = []
    yInsertSort = []
    xSelectSort = []
    ySelectSort = []
    for i in range(len(list)):
        InsertionSort((list[i]))
        yInsertSort.append(counter)
        xInsertSort.append(len(list[i]))
    counter = 0
    for i in range(len(list)):
        SelectionSort(list[i])
        ySelectSort.append(counter)
        xSelectSort.append(len(list[i]))
    counter = 0
    if test == 'A':
        test = 'Average (random values)'
    elif test == 'B':
        test = 'Best (Sorted values)'
    else:
        test = 'Worst (Reversed Order)'
    plt.xlabel('Size of List')
    plt.ylabel('Number of Swaps')
    plt.title(str(test) + ' Case for Insertion and Selection sort')
    plt.legend((plt.scatter(xInsertSort, yInsertSort, c='red'),
                plt.scatter(xSelectSort, ySelectSort, c = 'purple')),
               ('Insertion Sort', 'Selection Sort'))
    plt.show()

def instructions(s):
    if s == "Default":
        print("Please choose a mode. Enter 'user',"
              " for user mode or 'plot', for plot mode (case sensitive):")
    elif s == "user":
        print("Type f for Fibonnaci function.")
        print("Type g for GCD function.")
        print("Type e for Exponentiation functions."
              "   (Decrease-by-One, Decrease-by-Constant-Factor, and Divide-and-Conquer")
        print("Type s for sorting functions."
              "  (Insertion & Selection Sort)\n")
        print("Type 'back' to return to the user/plot selection.")
        print("Type x to exit the program.\n")
    elif s == "plot":
        print("Type fplot for Fibonnaci plot.")
        print("Type gplot for GCD plot.")
        print("Type eplot for Exponentiation plots."
              "   (Decrease-by-One, Decrease-by-Constant-Factor, and Divide-and-Conquer")
        print("Type splot for sorting plot."
              "  (Insertion & Selection Sort)\n")
        print("Type 'back' to return to the user/plot selection.")
        print("Type x to exit the program.\n")
    else:
        print("Invalid prompt.")

def getOutput(i):
    if i == 'f':
        k = int(input("Input kth value of Fibonacci algorithm: "))
        print("kth value of Fibonacci: ", Fibonacci(k))
        print("Number of Adds: ", fibAdds(k), "\n")
        return "user"

    elif i == 'g':
        k = int(input("Input kth value of Fibonacci \n"
                      "algorithm to get GCD: "))
        print("GCD of k and k-1: ", Euclids(k, k - 1), "\n")
        return "user"

    elif i == 'e':
        a = int(input("Input constant: "))
        n = int(input("Input exponent: "))
        print("Decrease-by-One: ", decreaseByOne(a, n))
        print("Decrease-by-Constant: ", decreaseByConstant(a, n))
        print("Divide-and-Conquer: ", divideConquer(a, n))
        return "user"

    elif i == 's':
        n = int(input("Input array size: "))
        arr = [int(j) for j in input("Input n numbers in any order: ").split()]
        arr1 = arr
        InsertionSort(arr)
        SelectionSort(arr1)
        print("Selection Sort: ", arr1)
        print("Insertion Sort: ", arr)
        return "user"

    elif i == "back":
        return "Default"

def main():

    userInput = "Default"
    instructions(userInput)
    userInput = input("Input: ")

    while userInput.lower() != "x":
        if type(userInput) != str:
            print("Please type one of the letters to access the options: ")
        else:
            s = getOutput(userInput)
        time.sleep(3)
        instructions(s)
        userInput = input("Input: ")


main()

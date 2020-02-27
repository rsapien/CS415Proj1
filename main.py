
# Project 1 - Asymptotic Analysis of Algorithms
# Creators: Robert Sapien & Vince Bjazevic
# Date: 28 February 2020

import matplotlib.pyplot as plt
import time

def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibAdds(n):
    if n <= 1:
        return 0
    return fibAdds(n-1) + fibAdds(n-2) + 1


def PlotFib(n):
    FibValues = []
    fiby = []
    for i in range(n):
        FibValues.append(Fibonacci(i))
        fiby.append(fibAdds(i))

    print("FibValues: ", FibValues)
    print("fiby: ", fiby)
    plt.xlabel("Fibonacci numbers calculated")
    plt.ylabel("Number of additions done\n")
    plt.plot(FibValues, fiby)
    plt.show()


def Euclids(a, b):
    if (b == 0):
        return a
    else:
        return Euclids(b, a % b)

def Mods(a, b):
    if (b == 0):
        return 0
    else:
        return Euclids(b, a % b) + 1

def PlotEuc(n):
    EucX = []
    EucY = []
    i = 1
    for i in range(n):
        a = Fibonacci(i)
        b = Fibonacci(i-1)
        count = Mods(a, b)
        EucY.append(count)
        EucX.append(a)

    plt.xlabel("Euclid's numbers calculated")
    plt.ylabel("Number of divisons")
    plt.plot(EucX, EucY)


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
        dbo.append(decreaseByOne(2, i))
        numMuls.append(dboMuls(2, i))

    plt.xlabel("Decrease-By-One")
    plt.ylabel("Decrease-By-One Multiplications")
    plt.plot(dbo, numMuls)
    plt.show()


def ComputeDBC(a, n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return (decreaseByOne(a, n / 2)) + 1
    return (decreaseByOne(a, (n - 1) / 2)) + 2

def DecreaseByConstant(a, n):
    if n <= 0:
        return 1
    elif n % 2 == 0:
        return decreaseByOne(a, n / 2) ** 2
    return a * decreaseByOne(a, (n - 1) / 2) ** 2

def PlotEx2():
    global count
    for i in range(len(fibx)):
        count = 0
        Fibonacci(fibx[i])
        fiby[i] = count

    # plt.xlabel("Fibonacci numbers calculated")
    # plt.ylabel("Number of additions done")
    # plt.plot(fibx, fiby)
    # plt.show()


def divideConquer(a, n):
    if n <= 0:
        return 1
    elif n % 2 == 0:
        return divideConquer(a, n / 2) * divideConquer(a, n / 2)
    return a * divideConquer(a, n / 2) * divideConquer(a, n / 2)

def dcMuls(a, n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return divideConquer(a, n / 2) * divideConquer(a, n / 2) + 1
    return a * divideConquer(a, n / 2) * divideConquer(a, n / 2) + 2



def PlotEx3(n):

    for i in range(n):



    # plt.xlabel("Fibonacci numbers calculated")
    # plt.ylabel("Number of additions done")
    # plt.plot(fibx, fiby)
    # plt.show()


def SelectionSort(A):
    global count
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


def PlotSelection():
    global count
    for i in range(len(fibx)):
        count = 0
        Fibonacci(fibx[i])
        fiby[i] = count

    # plt.xlabel("Fibonacci numbers calculated")
    # plt.ylabel("Number of additions done")
    # plt.plot(fibx, fiby)
    # plt.show()


def PlotInsertSort():
    global count
    for i in range(len(fibx)):
        count = 0
        Fibonacci(fibx[i])
        fiby[i] = count

    # plt.xlabel("Fibonacci numbers calculated")
    # plt.ylabel("Number of additions done")
    # plt.plot(fibx, fiby)
    # plt.show()


def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def instructions():
    print("Type f for Fibonnaci function.")
    print("Type g for GCD function.")
    print("Type e for Exponentiation functions."
          "   (Decrease-by-One, Decrease-by-Constant-Factor, and Divide-and-Conquer")
    print("Type s for sorting functions."
          "  (Insertion & Selection Sort)\n")
    print("Type x to exit the program.\n")

def getOutput(i):
    if i == 'f':
        k = int(input("Input kth value of Fibonacci algorithm: "))
        print("kth value of Fibonacci: ", Fibonacci(k))
        print("Number of Adds: ", count, "\n")

    elif i == 'g':
        k = int(input("Input kth value of Fibonacci \n"
                      "algorithm to get GCD: "))
        print("GCD of k and k-1: ", Euclids(k, k-1), "\n")

    elif i == 'e':
        a = int(input("Input constant: "))
        n = int(input("Input exponent: "))
        print("Decrease-by-One: ", decreaseByOne(a, n))
        print("Decrease-by-Constant: ", DecreaseByConstant(a, n))
        print("Divide-and-Conquer: ", divideConquer(a, n))

    elif i == 's':
        n = int(input("Input array size: "))
        arr = [int(j) for j in input("Input n numbers in any order: ").split()]
        arr1 = arr
        InsertionSort(arr)
        SelectionSort(arr1)
        print("Selection Sort: ", arr1)
        print("Insertion Sort: ", arr)



def main():
    print("Fibonacci: ")
    print(Fibonacci(5))
    print(fibAdds(5))
    #PlotFib(20)

    print("DBO: ")
    print(decreaseByOne(2, 5))
    print(dboMuls(2, 5))
    #plotDBO(10)

    print("D&C: ")
    print(divideConquer(2, 5))
    print(dcMuls(2, 5))

    #instructions()

    #uInput = input("Input: ")

    #while uInput.lower() != "x":
        #if type(uInput) != str:
            #print("Please type one of the letters to access the functions: ")

        #else:
            #getOutput(uInput)

        #time.sleep(3)
        #instructions()
        #uInput = input("Input: ")

main()

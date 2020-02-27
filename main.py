
# Project 1 - Asymptotic Analysis of Algorithms
# Creators: Robert Sapien & Vince Bjazevic
# Date: 28 February 2020

import matplotlib.pyplot as plt
import time

FibValues = []
Euclid = []
Exponent = []

def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibAdds(n):
    if n <= 1:
        return 1
    return fibAdds(n-1) + fibAdds(n-2)


def PlotFib(n):
    for i in range(n):
        FibonacciValues
        fiby[i] = count

    plt.xlabel("Fibonacci numbers calculated")
    plt.ylabel("Number of additions done\n")
    plt.plot(fibx, fiby)
    plt.show()


def Euclids(a, b):
    if (b == 0):
        return a
    else:
        return Euclids(b, a % b)


def DecreaseByOne(a, n):
    global count
    if n <= 0:
        return 1
    else:
        count += 1
        return a * DecreaseByOne(a, n - 1)


def PlotEx1():
    global count
    for i in range(len(ExpX)):
        count = 0
        DecreaseByOne(i, ExpX[i])
        ExpY[i] = count

    plt.xlabel("Decrease-By-One calculated")
    plt.ylabel("Number of multiplications done")
    plt.plot(ExpX, ExpY)
    plt.show()


def DecreaseByConstant(a, n):
    global count
    if n <= 0:
        return 1
    elif n % 2 == 0:
        count += 1
        return DecreaseByOne(a, n / 2) ** 2
    else:
        count += 2
        return a * DecreaseByOne(a, (n - 1) / 2) ** 2


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


def DivideConquer(a, n):
    global count
    if n <= 0:
        return 1
    elif n % 2 == 0:
        count += 1
        return DecreaseByOne(a, n / 2) * DecreaseByOne(a, n / 2)
    else:
        count += 1
        return a * DecreaseByOne(a, (n - 1) / 2) * DecreaseByOne(a, (n - 1) / 2)


def PlotEx3():
    global count
    for i in range(len(fibx)):
        count = 0
        Fibonacci(fibx[i])
        fiby[i] = count

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
        print("Decrease-by-One: ", DecreaseByOne(a, n))
        print("Decrease-by-Constant: ", DecreaseByConstant(a, n))
        print("Divide-and-Conquer: ", DivideConquer(a, n))

    elif i == 's':
        n = int(input("Input array size: "))
        arr = [int(j) for j in input("Input n numbers in any order: ").split()]
        arr1 = arr
        InsertionSort(arr)
        SelectionSort(arr1)
        print("Selection Sort: ", arr1)
        print("Insertion Sort: ", arr)



def main():
    print(Fibonacci(3))
    print(fibAdds(3))

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

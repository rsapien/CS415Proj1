
# Project 1 - Asymptotic Analysis of Algorithms
# Creators: Robert Sapien & Vince Bjazevic
# Date: 28 February 2020

import matplotlib.pyplot as plt
import numpy as numpy


fibx = [8, 10, 12, 14, 16, 18, 20]
fiby = [1, 2, 3, 4, 5, 6, 7]

FibonacciValues = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
                   17711, 28657, 46368, 75025, 121393]
EucX = [4, 6, 8, 10, 12, 16, 18, 20]
EucY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ExpX = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
ExpY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)


def fibAdds(n):
    if n <= 1:
        return n
    else:
        return fibAdds(n-1) + fibAdds(n-2) + 1


def PlotFib():
    for i in range(len(fibx)):
        Fib(fibx[i])
        fiby[i] = fibAdds(fibx[i])

    plt.xlabel("Fibonacci numbers calculated")
    plt.ylabel("Number of additions done")
    plt.plot(fibx, fiby)
    plt.show()


def Euclids(a, b):
    global count
    if (b == 0):
        return a
    else:
        count += 1
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
    print("Type f for Fibonnaci function.\n")
    print("Type g for GCD function.\n")
    print("Type e for Exponentiation functions.\n"
          "   (Decrease-by-One, Decrease-by-Constant-Factor, and Divide-and-Conquer")
    print("Type s for sorting functions.\n"
          "  (Insertion & Selection Sort)\n")
    print("Type x to exit the program.\n")

def getOutput(i):
    if i == 'f':
        k = int(input("Input kth value of Fibonacci algorithm: "))
        print("kth value of Fibonacci: ", Fib(k), "\n")

    elif i == 'g':
        k = int(input("Input kth value of Fibonacci \n"
                      "algorithm to get GCD: "))
        print("GCD of k and k-1: ", Euclids(k, k-1), "\n")

    elif i == 'e':
        a = int(input("Input constant: "))
        n = int(input("Input exponent: "))
        print("Decrease-by-One: ", DecreaseByOne(a, n), "\n")
        print("Decrease-by-Constant: ", DecreaseByConstant(a, n), "\n")
        print("Divide-and-Conquer: ", DivideConquer(a, n), "\n")

    elif i == 's':
        n = int(input("Input array size: "))
        arr = [int(j) for j in input("Input n numbers in any order: ").split()]
        arr1 = arr
        InsertionSort(arr)
        SelectionSort(arr1)
        print("Selection Sort: ", arr1)
        print("Insertion Sort: ", arr)



def main():

    instructions()

    uInput = input("Input: ")

    while numpy.lower(uInput) != "exit":
        if type(uInput) != str:
            print("Please type one of the letters to access the functions: ")
            pass

        else:
            getOutput(uInput)

        instructions()
        uInput = input("Input: ")

main()

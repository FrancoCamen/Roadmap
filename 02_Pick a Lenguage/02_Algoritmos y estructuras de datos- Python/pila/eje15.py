# Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.
from pila import Pila
stack = Pila()

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr):
    stack = [(0, len(arr)-1)]
    
    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = partition(arr, low, high)

            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))
    return arr

arr = [4, 2, 9, 1, 6, 3, 8, 5, 7]
print(arr)
arr_ordenado = quicksort(arr)
print(arr_ordenado)
# define function that takes in array of strings and returns list of list of strings
# same anagram function as mergeSort
def anagram(strings):
    newMap = {}  
    
    for val in strings:
        sorted = sortString(val)      
        if sorted in newMap:
            newMap[sorted].append(val)
        else:
            newMap[sorted] = [val]
    return list(newMap.values())

def sortString(str):
    char = list(str)
    heapSort(char)
    return ''.join(char)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr,n,i):
    maxNum = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[maxNum]:
        maxNum = left
    if right < n and arr[right] > arr[maxNum]:
        maxNum = right
    if maxNum != i:
        arr[i], arr[maxNum] = arr[maxNum], arr[i]
        heapify(arr, n, maxNum)

strings = ["bucket","rat","mango","tango","ogtan","tar"]
result = anagram(strings)
print(result)

# test cases ALL WORK
# test1 = ["bucket", "rat", "mango", "tango", "ogtan", "tar"]
# test2 = ["apple", "banana", "carrot", "date"]
# test3 = ["listen", "silent", "enlist", "inlets"]
# test4 = ["hello", "world", "drolw", "cat", "tac"]
# test5 = ["word"]
# test6 = []
# test7 = ["aaa", "aa", "a", "aaa", "aa"]
# result1 = anagram(test1)
# result2 = anagram(test2)
# result3 = anagram(test3)
# result4 = anagram(test4)
# result5 = anagram(test5)
# result6 = anagram(test6)
# result7 = anagram(test7)

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)
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

print("HEAP SORT SOLUTION")
print("Assignment Example")
strings = ["bucket","rat","mango","tango","ogtan","tar"]
result = anagram(strings)
print(f"Group {strings} into anagrams: {result} \n")

# test cases ALL WORK
print("Custom testcases \n")
test2 = ["apple", "banana", "carrot", "date"]
test3 = ["listen", "silent", "enlist", "inlets"]
test4 = ["hello", "world", "drolw", "cat", "tac"]
test5 = ["word"]
test6 = []
test7 = ["aaa", "aa", "a", "aaa", "aa"]
print(f"Group {test2} into anagrams: {anagram(test2)}")
print(f"Group {test3} into anagrams: {anagram(test3)}")
print(f"Group {test4} into anagrams: {anagram(test4)}")
print(f"Group {test5} into anagrams: {anagram(test5)}")
print(f"Group {test6} into anagrams: {anagram(test6)}")
print(f"Group {test7} into anagrams: {anagram(test7)}")
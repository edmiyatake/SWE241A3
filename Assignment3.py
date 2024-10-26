# define function that takes in array of strings and returns list of list of strings

def anagram(strings):
    newMap = {}  
    
    for val in strings:
        sorted = sortString(val)      
        if sorted in newMap:
            newMap[sorted].append(val)
        else:
            newMap[sorted] = [val]
    return list(newMap.values())

def merge(left,right):
    solution = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            solution.append(left[i])
            i += 1
        else:
            solution.append(right[j])
            j += 1

    solution.extend(left[i:])
    solution.extend(right[j:])
    return solution

def mergeSort(arr):
    newMap = {}

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left,right)

def sortString(s):
    newList = list(s)
    chars = mergeSort(newList)
    return "".join(chars)

# test cases that were given by canvas prompt
print("MERGE SORT SOLUTION")
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

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

# each sort program takes in a list and spits out a hashMap
# calculate sum of ASCII values for each string and place into hashmap with index sortedSTR
# Randomly chose merge sort and heap sort

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
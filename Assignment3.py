# define function that takes in array of strings and returns list of list of strings
# takes in a bunch of strings and probably the list form of hashmap key-value pairs
def anagram(arr1):
    solution = sort(arr1)
    return list(solution)

# each sort program takes in a list and spits out a hashMap
# calculate sum of ASCII values for each string and place into hashmap with index sortedSTR

def sort(arr):
    for str in arr:
        print(ord(str[0]))
    return 1

test1 = ["boom", "hate", "tartan", "root", "moob", "satan", "banana", "cat", "tac", "app"]
sort(test1)
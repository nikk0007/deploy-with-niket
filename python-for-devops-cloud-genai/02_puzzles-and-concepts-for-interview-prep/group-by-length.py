# Given a list of words, group the words by their lengths and return the result
# as a dictionary where the keys are the word lengths and the values are lists of words of that length.

words_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear', 'peach', 'plum']

def getGroup(myList):
    myDictionary = {}
    for item in words_list:
        arr = myDictionary.get(len(item), [])
        arr.append(item)
        myDictionary[len(item)] = arr

    return myDictionary    


# another way:
def getGroup_2(myList):
    myDictionary = {}
    for item in  myList:
        sizeKey = len(item)
        if sizeKey not in myDictionary:
            tempList = [item]
            myDictionary[sizeKey] = tempList
        else:
            list = myDictionary[sizeKey]
            list.append(item)
            myDictionary[sizeKey] = list    

    return myDictionary


print(getGroup(words_list))
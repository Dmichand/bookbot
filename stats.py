def getBookList(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        bookList = fileContents.split()
    return bookList

def getNumberOfWords(text):
    listOfWords = text.split()
    couter = 0
    for word in listOfWords:
        couter += 1
    return couter


def getBookInStr(filePath):
     with open(filePath) as f:
        text = f.read()
        return text
     


def timesCharAppeared(text):
    letters = {}
    for word in text:
         char = word.lower()
         if char in letters:
              letters[char] += 1
         else:
              letters[char] = 1
    return letters


def sort_on(d):
    return d["num"]


def moveToList(timesCharAppeared):
    sortedList = []
    for char in timesCharAppeared:
        sortedList.append({"char": char, "num": timesCharAppeared[char]})
    sortedList.sort(reverse=True, key=sort_on)
    return sortedList

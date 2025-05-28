def main():
   import sys
   from stats import (getNumberOfWords, getBookInStr, moveToList, timesCharAppeared)
   if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   
   
   pathToBook = sys.argv[1]



   bookInStr = getBookInStr(pathToBook)
   numberOfWords = getNumberOfWords(bookInStr)
   charDict = timesCharAppeared(bookInStr)
   sortedList = moveToList(charDict)
   printOutput(pathToBook,numberOfWords,sortedList)

def printOutput(pathToBook,numberOfWords,sortedList):
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {pathToBook}...")
   print("----------- Word Count ----------")
   print(f"Found {numberOfWords} total words")
   print("--------- Character Count -------")
   for item in sortedList:
      if not item["char"].isalpha():
         continue
      print(f"{item['char']}: {item['num']}")
   print("============= END ===============")
main()
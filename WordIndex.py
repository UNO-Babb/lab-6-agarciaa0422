#WordIndex.py
#Name:Arturo
#Date:3/2/2025
#Assignment:WordINdex

def main():
  textFile = open("gettysberg.txt", 'r')
  
  words = {} #create an empty dictionary
  lineNum = 0

  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w = w.replace("," , "")
      w = w.replace("." , "")
     
      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w] = [lineNum]

    for word in words:
      print(word, words[word])


if __name__ == '__main__':
  main()

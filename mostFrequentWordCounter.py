filePath = "randomText.txt"
wordCounts = dict()
with open(filePath, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            wordCounts[word] = wordCounts.get(word, 0) + 1
frequentWord, nOfTimes = None, None
for word, counts in wordCounts.items():
    if nOfTimes is None or nOfTimes < counts:
        nOfTimes = counts
        frequentWord = word
print(frequentWord, '\t', nOfTimes)

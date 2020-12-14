
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


def getWordScore(word, n):
    sum = 0
    for letter in word:
        sum += SCRABBLE_LETTER_VALUES[letter]
    sum = sum * len(word)
    if len(word) == n:
        sum += 50
    return sum


def displayHand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


def dealHand(n):

    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):
    newHand = dict(hand)
    for letter in word:
        newHand[letter] -= 1
    return newHand


def isValidWord(word, hand, wordList):
    handy = dict(hand)
    if word not in wordList:
        return False
    for key in word:
        try:
            assert handy[key] >= 1
            handy[key] -= 1
        except:
            return False
    return True   



def calculateHandlen(hand):
    length = 0
    for num in hand.values():
        length += num
    return length



def playHand(hand, wordList, n):
    finalScore = 0
    flag = True
    while flag == True:
        print("Current Hand:", end = " "),displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        
        if word == '.':
            print("Goodbye! Total score:",finalScore,"points.")
            break
        
        elif isValidWord(word, hand, wordList) :
            finalScore += getWordScore(word, n)
            print('"'+word+'"' ,'earned', getWordScore(word, n) ,'points. Total:', finalScore ,'points\n')
            hand = updateHand(hand, word)
            
            if calculateHandlen(hand) == 0:
                print("Run out of letters. Total score:", finalScore ,"points.")
                break
        else:
            print("Invalid word, please try again.")
            


def playGame(wordList):
    n = HAND_SIZE
    while True:
        userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if userInput == "e":
            break
        elif userInput == "n":
            hand = dealHand(n)
            playHand(hand, wordList, n)
        elif userInput == "r":
            try:
                playHand(hand, wordList, n)
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        else:
            print("Invalid command.")
        
            
            
            
            
            
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


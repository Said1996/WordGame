from WordGame import *
import time



def compChooseWord(hand, wordList, n):

    bestScore = 0

    bestWord = None
    for word in wordList:
        
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if (score > bestScore):
                bestScore = score
                bestWord = word
    return bestWord


def compPlayHand(hand, wordList, n):
    
    totalScore = 0
    while (calculateHandlen(hand) > 0) :
       
        print("Current Hand: ", end=' ')
        displayHand(hand)

        word = compChooseWord(hand, wordList, n)

        if word == None:

            break
            

        else :

            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            else :
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                hand = updateHand(hand, word)
                print()
    print('Total score: ' + str(totalScore) + ' points.')

    

def playGame(wordList):
    n = HAND_SIZE
    userInput = ''
    userOrComp = ''
    
    while True :
        try:
            userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            assert userInput == 'e' or userInput == 'r' or userInput == 'n'  
            if userInput == 'e':
                    break
            elif userInput == 'r' and lastCommand == '':
                raise Exception
        except AssertionError:
            print("Invalid command.")
        except Exception:
            print("You have not played a hand yet. Please play a new hand first!")
        else:
            while True:
                try:
                    userOrComp = input("Enter u to have yourself play, c to have the computer play: ")   
                    assert userOrComp == 'c' or userOrComp == 'u'
                except AssertionError:
                    print("Invalid command.")
                else:
                    if userInput == "n":
                        lastCommand = userInput
                        hand = dealHand(n)
                        if userOrComp == 'u':
                            playHand(hand, wordList, n)
                        else:
                            compPlayHand(hand, wordList, n)
                    elif userInput == "r":
                            if userOrComp == 'u':
                                playHand(hand, wordList, n)
                            else:
                                compPlayHand(hand, wordList, n)
                    break

                    

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)




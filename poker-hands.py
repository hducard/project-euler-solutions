'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

1. High Card: Highest value card.
2. One Pair: Two cards of the same value.
3. Two Pairs: Two different pairs.
4. Three of a Kind: Three cards of the same value.
5. Straight: All cards are consecutive values.
6. Flush: All cards of the same suit.
7. Full House: Three of a kind and a pair.
8. Four of a Kind: Four cards of the same value.
9. Straight Flush: All cards are consecutive values of same suit.
10. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD [Pair of Fives]   2C 3S 8S 8D TD [Pair of Eights]  Player2
2	 	5D 8C 9S JS AC [Highst card Ace] 2C 5C 7D 8S QH [Highst card Queen]  Player 1
3	 	2D 9C AS AH AC [Three Aces]      3D 6D 7D TD QD [Flush with Diamonds]  Player 2
4	 	4D 6S 9H QH QC [Pair of Queens Highest card Nine] 3D 6D 7H QD QS [Pair of Queens Highest card Seven] Player 1
5	 	2H 2D 4C 4D 4S [Full House With Three Fours] 3C 3D 3S 9S 9D [Full House with Three Threes]  Player 1

'''
'''
Points to note:
1. function must be able to identify hand - High card, One pair, Two pair, 3 of kind, Straight, Flush, Full house, Four of
     a kind, Straight flush, Royal flush
2.

'''
def rankHand(hand1, hand2):
    return true
    #do something
def rankCard(card):
    if card[0] == '2':
        return 1
    if card[0] == '3':
        return 2
    if card[0] == '4':
        return 3
    if card[0] == '5':
        return 4
    if card[0] == '6':
        return 5
    if card[0] == '7':
        return 6
    if card[0] == '8':
        return 7
    if card[0] == '9':
        return 8
    if card[0] == 'T':
        return 9
    if card[0] == 'J':
        return 10
    if card[0] == 'Q':
        return 11
    if card[0] == 'K':
        return 12
    if card[0] == 'A':
        return 13


def sortCards(cards):
    numCards = len(cards)
    index = 0
    tempCardRank=[]
    for i in range(0,numCards):
        Value = rankCard(cards[i])
        for j in range(i,numCards):

        return cards
        #find min value card
        #  needs a compare function
        # swap with index
        # increment index
    return cards


hands=[]

with open('input-p54.txt') as f:
    hands = f.readlines()
numOfHands = len(hands)
newHands=[]
for i in range(0,numOfHands):
    hands[i] = hands[i].split(" ")
    tempList = []
    tempList.append(hands[i][:5])
    tempList.append(hands[i][5:])
    newHands.append(tempList)
Hands = newHands
print(Hands[0])

#print(rankCard(Hands[0][0][1]))
#sort the cards in each hand
'''
for i in range(0,numOfHands):
    Hands[i][0] = sortCards(Hands[i][0])
    Hands[i][1] = sortCards(Hands[i][1])
'''
winOne = 0
'''
for k in hands:
    result = rankHand(k)
    if (result == 1):
        winOne = winOne+1
    else:
        winTwo = winTwo+1

print(winOne)
'''

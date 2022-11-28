__author__ = 'sebastian_lang'
'''
Royal flush 50 to 1
Straight flush 40 to 1
Four of a kind 30 to 1
Full House 8 to 1
Flush 7 to 1
Straight 4 to 1
Three of a kind 3 to 1
'''

from hand import HandType

class TripsBet:
    Table = {
        HandType.UNDEFINED: 0.0,
        HandType.HIGH_CARD: 0.0,
        HandType.PAIR: 0.0,
        HandType.TWO_PAIR: 0.0,
        HandType.THREE_OF_A_KIND: 3.0,
        HandType.STRAIGHT: 4.0,
        HandType.FLUSH: 7.0,
        HandType.FULL_HOUSE: 8.0,
        HandType.FOUR_OF_A_KIND: 30.0,
        HandType.STRAIGHT_FLUSH: 40.0,
        HandType.ROYAL_FLUSH: 50.0
    }
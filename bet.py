__author__ = 'monica_wang'

class Bet:
    def __init__(self, unit):
        self.ante = unit

        # blind matches ante
        self.blind = self.ante

        # trips bet
        if self.ante > 0:
            self.trips = self.ante
        else:
            self.trips = 0

        # play bet initial zero
        self.play = 0
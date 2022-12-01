# Simulation to answer the questions of the Casino St. Moritz.
# Date: 30.11.2022
# Author: Sebastian Lang

import sys

from ultimatepoker import Game

from random import seed
from random import gauss

import pandas

games_per_day = 400
number_of_days = 10000

bet_param = [
    {'bet_mean': 50, 'bet_std': 0},
    {'bet_mean': 100, 'bet_std': 0},
    {'bet_mean': 300, 'bet_std': 0},
    {'bet_mean': 400, 'bet_std': 0}
]

result_to_one_day = pandas.DataFrame(
    columns=[
        'GameNr',
        'PlayerCards',
        'DealerCards',
        'CommunityCards',
        'PlayerHand',
        'DealerHand',
        'AnteBet',
        'BlindBet',
        'PlayBet',
        'TripsBet',
        'PlayerGain',
        'PlayerTotalGain',
        'PlayerTotalBet'
    ],
    index=range(1, (games_per_day + 1))
)

totals_per_day = pandas.DataFrame(
    columns=[
        'PlayerTotalGain',
        'PlayerTotalBet',
        'PlayerMaxGain'
    ],
    index=range(1, (number_of_days + 1))
)

seed(42)

for cur_bet in bet_param:

    print(f"Simulation to bet parameter {cur_bet['bet_mean']}/{cur_bet['bet_std']} started ...")

    for cur_day in range(number_of_days):
        dailyGain = 0
        dailyBet = 0

        print(f"Running simulation for day {(cur_day + 1)}")
        for cur_game in range(games_per_day):
            bet_size = gauss(cur_bet['bet_mean'], cur_bet['bet_std'])

            game = Game(bet_size, False)
            gain, bet = game.playGame()

            result_to_one_day['GameNr'][cur_game + 1] = cur_game

            result_to_one_day['PlayerCards'][cur_game + 1] = str(game._player[0]) + ', ' + str(game._player[1])
            result_to_one_day['DealerCards'][cur_game + 1] = str(game._dealer[0]) + ', ' + str(game._dealer[1])
            result_to_one_day['CommunityCards'][cur_game + 1] = str(game._community[0]) + ', ' + \
                                                                str(game._community[1]) + ', ' + \
                                                                str(game._community[2]) + ', ' + \
                                                                str(game._community[3]) + ', ' + \
                                                                str(game._community[4])

            result_to_one_day['PlayerHand'][cur_game + 1] = str(game._playerHand)
            result_to_one_day['DealerHand'][cur_game + 1] = str(game._dealerHand)

            result_to_one_day['AnteBet'][cur_game + 1] = game._bet.ante
            result_to_one_day['BlindBet'][cur_game + 1] = game._bet.blind
            result_to_one_day['PlayBet'][cur_game + 1] = game._bet.play
            result_to_one_day['TripsBet'][cur_game + 1] = game._bet.trips

            dailyGain += gain
            dailyBet += bet

            result_to_one_day['PlayerGain'][cur_game + 1] = gain

            result_to_one_day['PlayerTotalGain'][cur_game + 1] = dailyGain
            result_to_one_day['PlayerTotalBet'][cur_game + 1] = dailyBet

        totals_per_day['PlayerTotalGain'][cur_day + 1] = dailyGain
        totals_per_day['PlayerTotalBet'][cur_day + 1] = dailyBet
        totals_per_day['PlayerMaxGain'][cur_day + 1] = max(result_to_one_day['PlayerTotalGain'])

    result_file_name = "results/UTH_Simulation_Days" + str(number_of_days) + \
                       "_GamesPerDay" + str(games_per_day) +\
                       "_BetMean" + str(cur_bet['bet_mean']) +\
                       "_BetStd" + str(cur_bet['bet_std']) + ".csv"

    totals_per_day.to_csv(result_file_name, sep=";", index=False)

    print(f"Simulation to bet parameter {cur_bet['bet_mean']}/{cur_bet['bet_std']} done!")


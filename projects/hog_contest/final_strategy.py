"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""
import sys
sys.path.append("..")
from hog.hog import extra_turn, free_bacon

PLAYER_NAME = 'Lain1385'  # Change this line!

def final_strategy(score, opponent_score):
    if opponent_score > 10 and score == opponent_score - 3:
        return 10
    elif opponent_score > 10 and score == opponent_score - 2:
        return 9
    elif opponent_score > 10 and score == opponent_score - 1:
        return 7
    elif opponent_score <= 10 and score == opponent_score - 3:
        return 9
    elif opponent_score <= 10 and score == opponent_score - 2:
        return 7
    elif extra_turn(score + free_bacon(opponent_score), opponent_score):
        return 0
    elif free_bacon(opponent_score) > 8 :
        return 0
    return 6

######################1
#74038 7.4038
#78798 7.8798
#83645 8.3645
#84374 8.4374
#85838 8.5838
#85359 8.5359
#82146 8.2146
#73925 7.3925
#58732 5.8732
#35194 3.5194
#when num_test = 6, expectation reaches max value
######################
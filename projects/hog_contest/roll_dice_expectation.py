import sys
sys.path.append("..")
from hog.hog import roll_dice, six_sided


######################
# Phase 1: Simulator #
######################

def expectation_1(num_rolls, dice=six_sided, num_test=10000):
	res = 0
	n = num_test
	while n:
		res = res + roll_dice(num_rolls, dice)
		n -= 1
	print(res, res / num_test)
	return res

def all_expectation_1():
	n = 10
	while n:
		expectation_1(n)
		n -= 1

#all_expectation_1()

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

def expectation_2(num_rolls, tolerance, dice=six_sided, num_test=10000):
	res = 0
	n = num_test
	while n:
		total = 0
		i = tolerance
		while i:
			m = roll_dice(num_rolls, dice)
			if not m == 1:
				total += m
				break
			else:
				total += m
				i -= 1
		res += total
		n -= 1
	print(res, res / num_test)
	return res

def all_expectation_2(n=10, tolerance=1):
	while n:
		expectation_2(n,tolerance)
		n -= 1

all_expectation_2(10, 4)
######################turn=2
#29-30 7-9
#137153 13.7153
#139429 13.9429
#144515 14.4515
#146046 14.6046
#144170 14.417
#138202 13.8202
#125503 12.5503
#104702 10.4702
#76553 7.6553
#40797 4.0797
#when num_test = 7, expectation reaches max value
######################

######################turn=3
#188767 18.8767
#194148 19.4148
#193711 19.3711
#192542 19.2542
#183954 18.3954
#169522 16.9522
#146969 14.6969
#118027 11.8027
#81748 8.1748
#41847 4.1847
#when num_test = 9, expectation reaches max value
######################

######################turn=4
#27-30 27,28,29,30
#226504 22.6504
#227909 22.7909
#230022 23.0022
#222672 22.2672
#208678 20.8678
#186437 18.6437
#158360 15.836
#123324 12.3324
#83963 8.3963
#41743 4.1743
#when num_test = 9, expectation reaches max value
######################
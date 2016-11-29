from random import random
heads = 0
tails = 0
for i in range(1,5001):
	coin = random()
	if(round(coin) == 0):
		heads += 1
		print "Attempt" + str(i) + ": throwing a coin... It's heads!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
	else:
		tails += 1
		print "Attempt" + str(i) + ": throwing a coin... It's tails!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."

def fibonnaciEvenSum(cap, evenSum=0, primeHistory=[]):
	print "Iter " + str(len(primeHistory))
	if not len(primeHistory):
		primeHistory = [1, 1]
	else:
		primeHistory.append(primeHistory[len(primeHistory) - 1] + primeHistory[len(primeHistory) - 2])
	lastPrimeValue = primeHistory[len(primeHistory) - 1]
	if not lastPrimeValue % 2:
		evenSum += lastPrimeValue
	if lastPrimeValue < cap:
		return fibonnaciEvenSum(cap, evenSum, primeHistory)
	else:
		return evenSum

print fibonnaciEvenSum(4000000)
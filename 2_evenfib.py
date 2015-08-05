def fibonnaciEvenSum(cap, evenSum=0, fibHistory=[]):
	print "Iter " + str(len(fibHistory))
	if not len(fibHistory):
		fibHistory = [1, 1]
	else:
		fibHistory.append(fibHistory[len(fibHistory) - 1] + fibHistory[len(fibHistory) - 2])
	lastFibValue = fibHistory[len(fibHistory) - 1]
	if lastFibValue < cap:
		if not lastFibValue % 2:
			evenSum += lastFibValue
		return fibonnaciEvenSum(cap, evenSum, fibHistory)
	else:
		return evenSum

print "Input a max/cap on the fib. series:"
cap = int(raw_input())
print fibonnaciEvenSum(cap)
def factorial(n):
	p = 1
	for i in xrange(1, n + 1):
		p *= i
	return p

def getUniqueDivisors(upperRangeLimit):
	divisors = [upperRangeLimit]
	for i in xrange(1, upperRangeLimit):
		if upperRangeLimit % i:
			divisors.append(i)
	return divisors

def getMultipleFromRange(upperRangeLimit):
	uniqueDivisors = getUniqueDivisors(upperRangeLimit) # Remove any irrelevant divisors
	for i in xrange(1, factorial(upperRangeLimit - 1) + 1):
		i *= upperRangeLimit # Largest increment we know we can increase by
		if not i % 1000000:
			print str(i) + "th iter"
		doesSatisfyDivision = True
		for j in uniqueDivisors:
			if i % j:
				doesSatisfyDivision = False
		if doesSatisfyDivision:
			return i

print "Input an upper range limit:"
upperRangeLimit = int(raw_input())
print "Multiple of 1..." + str(upperRangeLimit) + " is: " + str(getMultipleFromRange(upperRangeLimit))
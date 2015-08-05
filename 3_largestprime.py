import sys
import itertools
sys.setrecursionlimit(10000000)

def isPrime(n):
	if n < 2:
		return False
	else:
		return all(n % i for i in xrange(2, n))

def getSmallestPrimeDivisor(n): # Make this more efficient
	for i in xrange(2, n):
		if isPrime(i) and (not n % i):
			return i

def computePrimeFactorsFor(n, primeList=[]):
	smallestDivisor = getSmallestPrimeDivisor(n)
	if smallestDivisor:
		division = n / smallestDivisor
		if smallestDivisor not in primeList:
			primeList.append(smallestDivisor)
		if not isPrime(division):
			return computePrimeFactorsFor(division, primeList)
		else:
			if division not in primeList:
				primeList.append(division)
			return primeList

def getMaxPrimeFactor(n):
	primeFactors = computePrimeFactorsFor(n)
	if primeFactors and len(primeFactors):
		return max(primeFactors)
	else:
		return n

print "Input a number to get the max prime factor from:"
num = int(raw_input())
print "Max prime factor for " + str(num) + ": " + str(getMaxPrimeFactor(num))
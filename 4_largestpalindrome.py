def getPalindromeFromMaxDigits(digits):
	v1 = ((10 ** digits) - 1)
	v2 = v1
	shift = 10 ** (digits - 1)
	palindrome = 0
	for i in xrange(v1 - shift):
		for j in xrange(v2 - shift):
			p = (v1-i)*(v2-j)
			palindromeStr = str(p)
			length = len(palindromeStr)
			if length and (not length % 2) and palindromeStr[:length/2] == palindromeStr[length/2:][::-1]:
				if p > palindrome:
					palindrome = p
					print "Found higher palindrome: " + str(palindrome) + " with " + str(v1-i) + "*" + str(v2-j)
	return palindrome

print "Input number of max. digits:"
digits = int(raw_input())
print "Highest palindrome found: " + str(getPalindromeFromMaxDigits(digits)) # Inefficient for > 3 characters
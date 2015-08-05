def fizzBuzz(i):
	if not i % 3 and not i % 5:
		return "Fizz Buzz"
	elif not i % 3:
		return "Fizz"
	elif not i % 5:
		return "Buzz"

def sumOfFizzBuzz(cap, sum=0):
	i = 0
	while i < (cap - 1):
		i += 1
		fizzOrBuzz = fizzBuzz(i)
		if fizzOrBuzz:
			sum += i

print sumOfFizzBuzz(1000)
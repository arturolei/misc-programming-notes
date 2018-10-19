
#Here are my exercises for the List Comprehension study group.






'''
Bonus Question: Here is a baby's first version of calculating Factorial with a FOR loop.
The function "factorialize" takes an integer n and returns n!.

Rewrite the factorialize function so that it uses a list comprehension.
You might need to use a reduce. 

'''

def factorialize(n):
	n_factorial = 1
	for i in range(1,n+1):
		n_factorial=n_factorial*i
	return n_factorial

'''
Solution:
def factorialize(n):
	return reduce(lambda x,y: x*y, [i for i in range (1, n+1)])
'''

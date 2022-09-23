import pandas as pd 
import numpy as np 

#Question 1
def isprime (num):
	if (np.any(num % np.array([2,3,5,7]) == 0) and (not num in [2,3,5,7])):
		return False
	return True

primes = []
counter = 1
while (len(primes) <= 9):
	if (isprime(counter)):
		primes.append(counter)
	counter += 1
ans1 = pd.Series(primes)

#Question 2
ans2 = ans1.iloc[1::2]

#Question 3
ans3 = pd.Series(primes, index=['a','b','c','d','e','f','g','h','i','j'])

#Question 4
ans4 = ans3.loc['b':'j':2]

#Question 5
ans5 = pd.DataFrame([[2, "Jason", "Miller", 42, 4, 25], 
					 [5, "Jason", "Jacobson", 52, 24, 94],
					 [10, "Tina", "Ali", "36", 31, 57],
					 [15, "Jake", "Milner", 24, 2, 62],
					 [20, "Amy", "Cooze", 73, 3, 70]], 
		columns = ["id", "first_name", "last_name", "age", "preTestScore", "postTestScore"])

#Question 6
ans6 = ans5.set_index(["id"])

#Question 7
ans7 = ans6["first_name"]

#Question 8
ans8 = ans6.loc[10]['age']

#Question 9
pre = ans5["preTestScore"].mean()
post = ans5["postTestScore"].mean()
ans9 = post - pre

#Question 10
ans10 = ans6.copy()
ans10["postTestScore"][[15,20]] = np.nan

#Question 11
ans11 = ans10.dropna()

#Question 12
ans12 = ans6.reset_index()
ans12 = ans12.set_index(["first_name", "last_name"])

#Question 13
ans13 = ans12.loc["Tina", "age"]


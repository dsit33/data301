import numpy as np 
import math

#Question 1
def mult_table():
	return np.outer(range(1,11), range(1,11))
ans1 = mult_table()

#Question 2
ans2 = ans1[3:7,3:7]

#Question 3
ans3 = np.arange(1,17).reshape(4,4)

#Question 4
def same_val(v1, v2):
	return v1 % 2 == 0 and v2 % 2 == 0
q4 = np.vectorize(same_val)
ans4 = q4(ans2, ans3)

#Question 5
ans5 = np.sum(ans2 % 2 ==0)

#Question 6
q6 = np.vectorize(np.sqrt)
ans6 = q6(ans3)

#Question 7
diag = np.arange(0,100,11)
temp = ans1.copy()
flat = temp.flatten()
flat[diag] = flat[diag] + 1
ans7 = flat.reshape(10, 10)

#Question 8
ans8 = ans1[::-1,::-1]

#Question 9
ans9 = np.random.uniform(size=(10,10)) * 10

#Question 10
ans10 = np.apply_along_axis(np.mean, 0, ans1)

#Question 11
def mergesort(arr):
	if (arr.size <= 1):
		return arr
	p1,p2 = np.split(np.partition(arr, arr.size//2), [arr.size // 2])
	left = np.partition(mergesort(p1), p1.size//2)
	right = np.partition(mergesort(p2), p2.size//2)
	return np.hstack([left, right])
print(mergesort(np.array([5,4,3,2,1])))

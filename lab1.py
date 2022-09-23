import numpy as np 

scores_set = np.nan_to_num(np.genfromtxt("grades.txt", delimiter='\t'))

def eval_score(score, possible):
	return score/possible

eval_set = np.vectorize(eval_score)

def eval_student(scores, possible):
	overall = 0.0
	grades = eval_set(scores, possible)
	overall += np.delete(grades[0:4], np.argmin(grades[0:4])).mean() * .10
	overall += grades[4:13].mean() * .20
	overall += grades[14:16].mean() * .20
	overall += grades[13] * .20 + grades[18] * .20
	overall += grades[16] * .10 + grades[17] * .01
	overall *= 100
	if (grades[-1] >= 90.0 or overall >= 90.0):
		return 4
	elif (overall >= 80.0):
		return 3
	elif (overall >= 70.0):
		return 2
	elif (overall >= 60.0):
		return 1
	return 0

ids = scores_set[1:-1,0]
grades = np.apply_along_axis(eval_student, 1, scores_set[1:-1, 1:], scores_set[-1, 1:])
class_distribution = np.transpose(np.vstack([ids, grades]))
np.savetxt('class_grades.txt', class_distribution, fmt="%d")







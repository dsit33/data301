import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import itertools

def main():
	temp = pd.read_csv('chartPerformance.csv')
	temp = temp[['Song', 'Week Position', 'Weeks on Chart']]
	temp = temp.loc[temp['Week Position'] >= 20].drop(['Week Position'], axis=1)
	temp.columns = ['Song', 'Weeks as Top 20']
	performance = temp.groupby(['Song']).sum().reset_index().sort_values(by=['Weeks as Top 20'], ascending=False)

	song_data = pd.read_csv('dataset-of-10s.csv')
	df = pd.merge(performance, song_data, left_on=['Song'],right_on=['track']).drop(['track','uri','target'],axis=1)
	subsetNames = list(df.columns.values)
	subsetNames.remove('Weeks as Top 20')
	df.sort_values(by=['Weeks as Top 20'], inplace=True, ascending=False)
	df.drop_duplicates(subset=subsetNames, keep='last',inplace=True)

	random_indices = np.random.permutation(df.index)
	test_cutoff = len(df)//5
	test = df.loc[random_indices[1:test_cutoff]]
	train = df.loc[random_indices[test_cutoff:]]

	predictors = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
              'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
              'time_signature', 'chorus_hit', 'sections']
	to_predict = ['Weeks as Top 20']

	for p in list(itertools.permutations(predictors)):
  		knn = KNeighborsRegressor()
  		knn.fit(train[p], train[to_predict])
  		predictions = knn.predict(test[p])
  		actual = test[to_predict]

  		error = (abs(predictions - actual)).sum() / len(predictions)
  		print(error)

if __name__ == '__main__':
	main()
from pandas import read_csv
from matplotlib import pyplot
# load dataset
dataset = read_csv('pollution.csv', header=0, index_col=0)
values = dataset.values
# plot each column
pyplot.figure()
groups = [0, 1, 2, 3, 5, 6, 7]
for i, group in enumerate(groups, start=1):
	pyplot.subplot(len(groups), 1, i)
	pyplot.plot(values[:, group])
	pyplot.title(dataset.columns[group], y=0.5, loc='right')
pyplot.show()
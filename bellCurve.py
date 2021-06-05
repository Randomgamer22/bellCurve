import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('csvfiles/Students_Marks.csv')

marks_list = df['Marks In Percentage'].tolist()
sum_of_marks = 0

for mark in marks_list:
	sum_of_marks += mark

average = sum_of_marks / len(marks_list)

fig = ff.create_distplot([marks_list], ['Marks In Percentage'])
fig.show()
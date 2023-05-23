from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as sl

df = pd.read_csv('imdb_final.csv', sep = ',')

#def my_autopct(pct):
    #return ('%.2f' % pct) if pct >= 5 else ''

def tab_dataviz():
	sl.title('Dataviz')

	#visuel 1
	sl.subheader('Distribution par titleType')
	image_title_type = Image.open('title_type.png')
	sl.image(image_title_type)

	#visuel 2
	sl.subheader('Nombre de films au fils des années')
	image_number_movies = Image.open('number_movies.png')
	sl.image(image_number_movies)

	#visuel 3
	sl.subheader('Distribution par région')
	image_regions = Image.open('regions.png')
	sl.image(image_regions)

	#visuel 4
	sl.subheader('Distribution par sexe')
	col1, col2, col3 = sl.columns([1,1,1])
	image_gender = Image.open('gender.png')
	col2.image(image_gender)

	sl.divider()

	#visuel 5
	sl.subheader('Top 10 des films')
	
	#pondération
	v = df['numVotes']
	R = df['averageRating']
	C = df['averageRating'].mean()
	m = v.quantile(0.90)
	df['score'] = round(((v/(v+m)) * R) + ((m/(v+m)) * C), 2)

	x = df.sort_values(by = 'score', ascending = False)['score'].head(10)
	y = df.sort_values(by = 'score', ascending = False)['originalTitle'].head(10)
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, x)
	ax1.invert_yaxis()
	plt.xlabel('Score pondéré')
	plt.style.use('seaborn')
	sl.pyplot(fig)

	col1, col2 = sl.columns([1,1])

	#visuel 6
	col1.subheader('Top 10 des réalisateurs')
	x = df['director'].value_counts().head(10)
	y = df['director'].value_counts().head(10).index
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, width = x)
	ax1.invert_yaxis()
	plt.xlabel('Nombre de films')
	plt.style.use('seaborn')
	col1.pyplot(fig)

	#visuel 7
	col2.subheader('Top 10 des scénaristes')
	x = df['writer'].value_counts().head(10)
	y = df['writer'].value_counts().head(10).index
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, width = x)
	ax1.invert_yaxis()
	plt.xlabel('Nombre de films')
	plt.style.use('seaborn')
	col2.pyplot(fig)

	#visuel 8
	sl.subheader('Top 10 des acteurs/actrices')
	x = df['cast'].value_counts().head(10)
	y = df['cast'].value_counts().head(10).index
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, width = x)
	ax1.invert_yaxis()
	plt.xlabel('Nombre de films')
	plt.style.use('seaborn')
	sl.pyplot(fig)

	#visuel 9
	sl.subheader('Distribution par genre')
	image_genres = Image.open('genres.png')
	sl.image(image_genres)
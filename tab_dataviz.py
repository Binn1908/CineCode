from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as sl

df = pd.read_csv('imdb_final.csv', sep = ',')

#def my_autopct(pct):
    #return ('%.2f' % pct) if pct >= 5 else ''

def tab_dataviz():
	sl.title('Dataviz')

	sl.subheader('IMDb')

	tab1, tab2, tab3, tab4 = sl.tabs([
		'Distribution par type',
		'Nombre de films par année',
		'Distribution par région',
		'Distribution par sexe'
		])

	#visuel 1
	tab1.subheader('Distribution par type')
	image_title_type = Image.open('title_type.png')
	tab1.image(image_title_type)

	#visuel 2
	tab2.subheader('Nombre de films au fils des années')
	image_number_movies = Image.open('number_movies.png')
	tab2.image(image_number_movies)

	#visuel 3
	tab3.subheader('Distribution par région')
	image_regions = Image.open('regions.png')
	tab3.image(image_regions)

	#visuel 4
	tab4.subheader('Distribution par sexe')
	image_gender = Image.open('gender.png')
	with tab4:
		col1, col2, col3 = sl.columns([1,1,1])
		col2.image(image_gender)

	sl.divider()

	sl.subheader('IMDb final')

	tab1, tab2, tab3, tab4, tab5 = sl.tabs([
		'Top 10 des films',
		'Top 10 des réalisateurs',
		'Top 10 des scénaristes',
		'Top 10 des acteurs/actrices',
		'Distribution par genre'
		])

	#visuel 5
	tab1.subheader('Top 10 des films')
	
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
	tab1.pyplot(fig)

	#visuel 6
	tab2.subheader('Top 10 des réalisateurs')
	x = df['director'].value_counts().head(10)
	y = df['director'].value_counts().head(10).index
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, width = x)
	ax1.invert_yaxis()
	plt.xlabel('Nombre de films')
	plt.style.use('seaborn')
	tab2.pyplot(fig)

	#visuel 7
	tab3.subheader('Top 10 des scénaristes')
	x = df['writer'].value_counts().head(10)
	y = df['writer'].value_counts().head(10).index
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, width = x)
	ax1.invert_yaxis()
	plt.xlabel('Nombre de films')
	plt.style.use('seaborn')
	tab3.pyplot(fig)

	#visuel 8
	tab4.subheader('Top 10 des acteurs/actrices')
	x = df['cast'].value_counts().head(10)
	y = df['cast'].value_counts().head(10).index
	fig, ax = plt.subplots()
	ax1 = plt.subplot()
	ax1.barh(y, width = x)
	ax1.invert_yaxis()
	plt.xlabel('Nombre de films')
	plt.style.use('seaborn')
	tab4.pyplot(fig)

	#visuel 9
	tab5.subheader('Distribution par genre')
	image_genres = Image.open('genres.png')
	tab5.image(image_genres)

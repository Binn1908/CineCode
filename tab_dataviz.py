from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as sl

df = pd.read_csv('imdb_final.csv', sep = ',')

#pondération
v = df['numVotes']
R = df['averageRating']
C = df['averageRating'].mean()
m = v.quantile(0.90)
df['score'] = round(((v/(v+m)) * R) + ((m/(v+m)) * C), 2)

def tab_dataviz():
	sl.title('Dataviz')

	sl.subheader('IMDb')

	tab1, tab2, tab3, tab4 = sl.tabs([
		'Distribution par type',
		'Distribution par région',
		'Nombre de films par année',
		'Distribution par sexe'
		])

	#visuel 1
	tab1.subheader('Distribution par type')
	image_title_type = Image.open('title_type.png')
	tab1.image(image_title_type)

	#visuel 2
	tab2.subheader('Distribution par région')
	image_regions = Image.open('regions.png')
	tab2.image(image_regions)

	#visuel 3
	tab3.subheader('Nombre de films par année')
	image_number_movies = Image.open('number_movies.png')
	tab3.image(image_number_movies)

	#visuel 4
	tab4.subheader('Distribution par sexe')
	image_gender = Image.open('gender.png')
	tab4.image(image_gender)

	sl.divider()

	sl.subheader('IMDb (sélection CinéCode)')

	tab5, tab6, tab7, tab8, tab9 = sl.tabs([
		'Films',
		'Réalisateurs',
		'Scénaristes',
		'Acteurs/Actrices',
		'Distribution par genre'
		])

	#visuel 5
	with tab5:
		sl.subheader('Top 10 des films')
		visuel5_options = ['note moyenne', 'nombre de votes', 'score pondéré']
		visuel5_user = 'note moyenne'
		visuel5_user = sl.selectbox('Filtrer par', visuel5_options, key = 5)
		if visuel5_user == 'note moyenne':
			x = df.sort_values(by = 'averageRating', ascending = False)['averageRating'].head(10)
			y = df.sort_values(by = 'averageRating', ascending = False)['originalTitle'].head(10)
		elif visuel5_user == 'nombre de votes':
			x = df.sort_values(by = 'numVotes', ascending = False)['numVotes'].head(10)
			y = df.sort_values(by = 'numVotes', ascending = False)['originalTitle'].head(10)
		elif visuel5_user == 'score pondéré':
			x = df.sort_values(by = 'score', ascending = False)['score'].head(10)
			y = df.sort_values(by = 'score', ascending = False)['originalTitle'].head(10)
		fig, ax = plt.subplots(figsize = (9,4))
		ax1 = plt.subplot()
		ax1.barh(y, x)
		ax1.invert_yaxis()
		plt.xlabel(visuel5_user)
		plt.style.use('seaborn')
		fig.patch.set_facecolor('#0E1116')
		ax1.xaxis.label.set_color('white')
		ax1.yaxis.label.set_color('white')
		ax1.tick_params(axis='x', colors='white')
		ax1.tick_params(axis='y', colors='white')
		ax1.spines['left'].set_color('white')
		ax1.spines['top'].set_color('white')
		sl.pyplot(fig)

	#visuel 6
	with tab6:
		sl.subheader('Top 10 des réalisateurs')
		visuel6_options = ['nombre de film', 'note moyenne', 'nombre de votes', 'score pondéré']
		visuel6_user = 'nombre de film'
		visuel6_user = sl.selectbox('Filtrer par', visuel6_options, key = 6)
		if visuel6_user == 'nombre de film':
			x = df['director'].value_counts().head(10)
			y = df['director'].value_counts().head(10).index
		elif visuel6_user == 'note moyenne':
			x = df.groupby(by = 'director')['averageRating'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'director')['averageRating'].mean().sort_values(ascending = False).head(10).index
		elif visuel6_user == 'nombre de votes':
			x = df.groupby(by = 'director')['numVotes'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'director')['numVotes'].mean().sort_values(ascending = False).head(10).index
		elif visuel6_user == 'score pondéré':
			x = df.groupby(by = 'director')['score'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'director')['score'].mean().sort_values(ascending = False).head(10).index
		fig, ax = plt.subplots(figsize = (9,3))
		ax1 = plt.subplot()
		ax1.barh(y, width = x)
		ax1.invert_yaxis()
		plt.xlabel(visuel6_user)
		plt.style.use('seaborn')
		fig.patch.set_facecolor('#0E1116')
		ax1.xaxis.label.set_color('white')
		ax1.yaxis.label.set_color('white')
		ax1.tick_params(axis='x', colors='white')
		ax1.tick_params(axis='y', colors='white')
		ax1.spines['left'].set_color('white')
		ax1.spines['top'].set_color('white')
		sl.pyplot(fig)

	#visuel 7
	with tab7:
		sl.subheader('Top 10 des scénaristes')
		visuel7_options = ['nombre de film', 'note moyenne', 'nombre de votes', 'score pondéré']
		visuel7_user = 'nombre de film'
		visuel7_user = sl.selectbox('Filtrer par', visuel7_options, key = 7)
		if visuel7_user == 'nombre de film':
			x = df['writer'].value_counts().head(10)
			y = df['writer'].value_counts().head(10).index
		elif visuel7_user == 'note moyenne':
			x = df.groupby(by = 'writer')['averageRating'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'writer')['averageRating'].mean().sort_values(ascending = False).head(10).index
		elif visuel7_user == 'nombre de votes':
			x = df.groupby(by = 'writer')['numVotes'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'writer')['numVotes'].mean().sort_values(ascending = False).head(10).index
		elif visuel7_user == 'score pondéré':
			x = df.groupby(by = 'writer')['score'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'writer')['score'].mean().sort_values(ascending = False).head(10).index
		fig, ax = plt.subplots(figsize = (9,3))
		ax1 = plt.subplot()
		ax1.barh(y, width = x)
		ax1.invert_yaxis()
		plt.xlabel(visuel7_user)
		plt.style.use('seaborn')
		fig.patch.set_facecolor('#0E1116')
		ax1.xaxis.label.set_color('white')
		ax1.yaxis.label.set_color('white')
		ax1.tick_params(axis='x', colors='white')
		ax1.tick_params(axis='y', colors='white')
		ax1.spines['left'].set_color('white')
		ax1.spines['top'].set_color('white')
		sl.pyplot(fig)

	#visuel 8
	with tab8:
		sl.subheader('Top 10 des acteurs/actrices')
		visuel8_options = ['nombre de film', 'note moyenne', 'nombre de votes', 'score pondéré']
		visuel8_user = 'nombre de film'
		visuel8_user = sl.selectbox('Filtrer par', visuel8_options, key = 8)
		if visuel8_user == 'nombre de film':
			x = df['cast'].value_counts().head(10)
			y = df['cast'].value_counts().head(10).index
		elif visuel8_user == 'note moyenne':
			x = df.groupby(by = 'cast')['averageRating'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'cast')['averageRating'].mean().sort_values(ascending = False).head(10).index
		elif visuel8_user == 'nombre de votes':
			x = df.groupby(by = 'cast')['numVotes'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'cast')['numVotes'].mean().sort_values(ascending = False).head(10).index
		elif visuel8_user == 'score pondéré':
			x = df.groupby(by = 'cast')['score'].mean().sort_values(ascending = False).head(10)
			y = df.groupby(by = 'cast')['score'].mean().sort_values(ascending = False).head(10).index
		fig, ax = plt.subplots(figsize = (9,3))
		ax1 = plt.subplot()
		ax1.barh(y, width = x)
		ax1.invert_yaxis()
		plt.xlabel(visuel8_user)
		plt.style.use('seaborn')
		fig.patch.set_facecolor('#0E1116')
		ax1.xaxis.label.set_color('white')
		ax1.yaxis.label.set_color('white')
		ax1.tick_params(axis='x', colors='white')
		ax1.tick_params(axis='y', colors='white')
		ax1.spines['left'].set_color('white')
		ax1.spines['top'].set_color('white')
		sl.pyplot(fig)

	#visuel 9
	tab9.subheader('Distribution par genre')
	image_genres = Image.open('genres.png')
	tab9.image(image_genres)

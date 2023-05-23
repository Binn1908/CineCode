import json
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import requests
import streamlit as sl

#import final IMDb dataset (7123 movies)
df1 = pd.read_pickle('imdb_final_1.pickle')
df2 = pd.read_pickle('imdb_final_2.pickle')
df3 = pd.read_pickle('imdb_final_3.pickle')
df4 = pd.read_pickle('imdb_final_4.pickle')
imdb = pd.concat([df1, df2, df3, df4])

#set up k-NN algorithm based on genres, directors, writers and actors (cast)
X = imdb.drop(columns = ['tconst', 'originalTitle', 'startYear', 'runtimeMinutes', 'averageRating', 'numVotes'])
model = NearestNeighbors(n_neighbors=4).fit(X)

#import lists for select buttons
movie_options = pd.read_csv('movies.csv', sep = ',')
genre_options = pd.read_csv('genres.csv', sep = ',')
director_options = pd.read_csv('directors.csv', sep = ',')
writer_options = pd.read_csv('writers.csv', sep = ',')
cast_options = pd.read_csv('cast.csv', sep = ',')

#access key for IMDb API
headers = {
	'x-rapidapi-host': 'imdb8.p.rapidapi.com',
	'x-rapidapi-key': rapid_api_key
    }

def tab_main():
	sl.title('Recommendation de films')
	sl.write('Bonjour la Creuse !')
	sl.write('...')
	
	#ask user for a movie
	with sl.form('simple_search'):
		user_favorite = sl.selectbox('Sélectionnez un film.', movie_options)
		submit_simple = sl.form_submit_button('Envoyer')

	#return film recommendations
	if submit_simple:
		if user_favorite != 'aucun':
			
			#input user choice in k-NN model
			propo = model.kneighbors(X.loc[imdb['originalTitle'] == user_favorite])
			
			sl.write('Excellent choix ! Voici nos recommendations :')
			for n in range(1,4):
				tconst = imdb.iloc[propo[1][0][n], 0]
				title = imdb.iloc[propo[1][0][n], 1]
				release_year = imdb.iloc[propo[1][0][n], 2]
				duration = imdb.iloc[propo[1][0][n], 3]
				score = imdb.iloc[propo[1][0][n], 4]
				url_imdb = 'https://www.imdb.com/title/' + tconst

				#get more info via API
				url_basic = 'https://imdb8.p.rapidapi.com/auto-complete'
				tconst = {'q': imdb.iloc[propo[1][0][n], 0]}
				response = requests.request('GET', url_basic, headers = headers, params = tconst)
				image_url = response.json()['d'][0]['i']['imageUrl']

				url_synopsis = 'https://imdb8.p.rapidapi.com/title/get-plots'
				tconst = {'tconst': imdb.iloc[propo[1][0][n], 0]}
				response = requests.get(url_synopsis, headers = headers, params = tconst)
				synopsis = response.json()['plots'][0]['text']

				#display results in different columns on the main tab
				col1, col2 = sl.columns([1,3]) #size proportion of columns
				col1.image(image_url)
				col2.write(f'[**{title} ({release_year})**]({url_imdb})')
				col2.write(f'{str(duration)} min')
				col2.write(f'**Note IMDb:** {score}/10')
				col2.write(synopsis)
				#url_imdb_cast = url_imdb + '/fullcredits'
				#sl.markdown(f'**[casting principal]({url_imdb_cast})**')

	sl.divider()

	sl.subheader('Recherche avancée')

	#ask user for genre, director, writer and cast
	with sl.form('advanced_search'):
		genre = sl.multiselect('Genre', genre_options, max_selections = 3)
		director = sl.multiselect('Réalisateur', director_options, max_selections = 3)
		writer = sl.multiselect('Scénariste', writer_options, max_selections = 3)
		cast = sl.multiselect('Acteur / Actrice', cast_options, max_selections = 3)
		submit_advanced = sl.form_submit_button('Envoyer')

	if submit_advanced:

		#import template for advanced search
		template = pd.read_csv('template.csv', sep = ',')

		#update template based on user choices
		if len(genre) > 0:
			user_genre1 = genre[0]
			template[user_genre1] = True
			if len(genre) == 2:
				user_genre2 = genre[1]
				template[user_genre2] = True
			if len(genre) == 3:
				user_genre3 = genre[2]
				template[user_genre3] = True
		if len(director) > 0:
			user_director1 = 'd_' + director[0]
			template[user_director1] = True
			if len(director) == 2:
				user_director2 = 'd_' + director[1]
				template[user_director2] = True
			if len(director) == 3:
				user_director3 = 'd_' + director[2]
				template[user_director3] = True
		if len(writer) > 0:
			user_writer1 = 'w_' + writer[0]
			template[user_writer1] = True
			if len(writer) == 2:
				user_writer2 = 'w_' + writer[1]
				template[user_writer2] = True
			if len(writer) == 3:
				user_writer3 = 'w_' + writer[2]
				template[user_writer3] = True
		if len(cast) > 0:
			user_cast1 = 'a_' + cast[0]
			template[user_cast1] = True
			if len(cast) == 2:
				user_cast2 = 'a_' + cast[1]
				template[user_cast2] = True
			if len(cast) == 3:
				user_cast3 = 'a_' + cast[2]
				template[user_cast3] = True

		#input template in k-NN model
		propo = model.kneighbors([template.iloc[0]])
		
		sl.write('Voici nos recommendations :')
		for n in range(1,4):
			tconst = imdb.iloc[propo[1][0][n], 0]
			title = imdb.iloc[propo[1][0][n], 1]
			release_year = imdb.iloc[propo[1][0][n], 2]
			duration = imdb.iloc[propo[1][0][n], 3]
			score = imdb.iloc[propo[1][0][n], 4]
			url_imdb = 'https://www.imdb.com/title/' + tconst

			#get more info via API
			url_basic = 'https://imdb8.p.rapidapi.com/auto-complete'
			tconst = {'q': imdb.iloc[propo[1][0][n], 0]}
			response = requests.request('GET', url_basic, headers = headers, params = tconst)
			image_url = response.json()['d'][0]['i']['imageUrl']

			url_synopsis = 'https://imdb8.p.rapidapi.com/title/get-plots'
			tconst = {'tconst': imdb.iloc[propo[1][0][n], 0]}
			response = requests.get(url_synopsis, headers = headers, params = tconst)
			synopsis = response.json()['plots'][0]['text']

			#display results in different columns on the main tab
			col1, col2 = sl.columns([1,3]) #size proportion of columns
			col1.image(image_url)
			col2.write(f'[**{title} ({release_year})**]({url_imdb})')
			col2.write(f'{str(duration)} min')
			col2.write(f'**Note IMDb:** {score}/10')
			col2.write(synopsis)
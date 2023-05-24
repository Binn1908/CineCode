import streamlit as sl

def tab_ressources():
	sl.title('Ressources')

	sl.subheader('IMDb')
	sl.write('[Les datasets](https://datasets.imdbws.com/)')
	sl.write('[Documentation](https://developer.imdb.com/non-commercial-datasets/)')

	sl.subheader('Code')

	col1, col2 = sl.columns([1,2])
	sl.write('- Exploration des données IMDb')
	sl.write('- Nettoyage des données')
	sl.write('- Dataviz IMDb final')
	sl.write('- Machine learning')

	with open('cinecode.zip', 'rb') as f:
   		sl.download_button('Télécharger notebooks', f, file_name = 'cinecode.zip')

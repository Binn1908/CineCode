import streamlit as sl

def tab_ressources():
	sl.title('Ressources')

	sl.write("<span style='font-size: 29px; color: #F8B405;'>IMDb</span>", unsafe_allow_html=True)
	sl.write('[Les datasets](https://datasets.imdbws.com/)')
	sl.write('[Documentation](https://developer.imdb.com/non-commercial-datasets/)')

	sl.write("<span style='font-size: 29px; color: #F8B405;'>Code</span>", unsafe_allow_html=True)

	col1, col2 = sl.columns([1,2])
	sl.write('- Exploration des données IMDb')
	sl.write('- Nettoyage des données')
	sl.write('- Dataviz IMDb final')
	sl.write('- Machine learning')

	with open('cinecode.zip', 'rb') as f:
   		sl.download_button('Télécharger notebooks', f, file_name = 'cinecode.zip')

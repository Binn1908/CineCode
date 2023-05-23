import streamlit as sl

def tab_cinecode():
	sl.title('CinéCode')

	sl.subheader("L'équipe")

	sl.subheader('La mission')
	sl.write("création d'un outil de recommandation de films...")

	sl.subheader('Notre démarche')
	sl.write("sélection des films sur la base de données d'IMDb...")

	sl.subheader('Outils utilisés')
	sl.write('Pandas, Matplotlib, scikit-learn, Streamlit, API...')

	sl.subheader('Machine Learning')
	sl.write('k-NN...')

	sl.subheader('Difficultés rencontrées')
	sl.write('manque de diversité (genres), dataset trop volumineux...')

	sl.subheader("Points d'amélioration")
	sl.write("pour affiner les résultats : retravailler le dataset avec plus de choix et plus d'acteurs (vu que le format pickle permet des fichiers plus légers)")
	sl.write('dataviz : permettre la sélection de critères pour filtrer les résultats')
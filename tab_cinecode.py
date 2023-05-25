import streamlit as sl

def tab_cinecode():
	sl.title('CinéCode')

	tab1, tab2, tab3, tab4 = sl.tabs([
		'CinéCode',
		'Notre démarche',
		'Machine Learning',
		'Revue'
		])

	with tab1:
		sl.subheader("L'équipe")
		col1, col2, col3 = sl.columns([1,1,1])
		col1.write('Chinnawat')
		col2.write('Jacques')
		col3.write('Khalid')

		sl.subheader('Mission')
		sl.write("- Analyse d’une base de données IMDB et création d’un outil de recommandation de films sur cette même base de données après un nettoyage des données")

	with tab2:
		sl.subheader('Notre démarche')
		sl.write("- Nous avons commencé par nettoyer la base de données IMDB afin d’éliminer les données inutiles, corriger les erreurs et normaliser les formats et sélectionner uniquement les infos qui nous semblaient pertinentes. Ensuite, nous avons créé une interface utilisateur conviviale en utilisant Streamlit pour présenter les recommandations de films personnalisées aux utilisateurs et faciliter leur expérience de navigation.")

		sl.subheader('Outils utilisés')
		sl.write('- Pandas, Matplotlib, scikit-learn, Streamlit, API...')

	with tab3:
		sl.subheader('Machine Learning')
		sl.write("- KNN : Nous avons choisi d’utiliser l’algorithme KNN (proches voisins) pour notre projet de recommandation de films en raison de sa capacité à trouver des films similaires en fonction des préférences de l’utilisateur en se basant sur les caractéristiques des films et en identifiant les voisins les plus proches dans l’espace de caractéristiques.")

	with tab4:
		sl.subheader('Difficultés rencontrées')
		sl.write('- manque de diversité (genres)')
		sl.write('- dataset trop volumineux...')

		sl.subheader("Points d'amélioration")
		sl.write("- pour affiner les résultats : retravailler le dataset avec plus de choix et plus d'acteurs (vu que le format pickle permet des fichiers plus légers)")

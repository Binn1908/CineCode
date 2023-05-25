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
		sl.write("- Analyse d’une base de données IMDb et création d’un outil de recommandation de films pour un cinéma souhaitant passer le cap du digital")		

	with tab2:
		sl.subheader('Notre démarche')
		sl.write("- Nettoyer la BDD IMDb afin d’éliminer les données inutiles, corriger les erreurs et normaliser les formats et filtrer les données")
		sl.write('- Création d’une interface utilisateur conviviale en utilisant Streamlit pour présenter les recommandations de films personnalisées aux utilisateurs et faciliter leur expérience de navigation')
			 
		sl.subheader('Outils utilisés')
		sl.write('- Pandas, Matplotlib, scikit-learn, Streamlit, IMDb API')

	with tab3:
		sl.subheader('Machine Learning')
		sl.write("- KNN : Nous avons choisi d’utiliser l’algorithme KNN (proches voisins) en raison de sa capacité à trouver des films similaires en fonction des préférences de l’utilisateur en se basant sur les caractéristiques des films et en identifiant les voisins les plus proches dans l’espace de caractéristiques.")

	with tab4:
		sl.subheader('Difficultés rencontrées')
		sl.write('- Volume de base de données important')
		sl.write('- Filtrer la base de données sans perdre des films cultes/classiques')

		sl.subheader("Points d'amélioration")
		sl.write("- Pour affiner les résultats : retravailler le dataset avec plus de choix et plus d'acteurs")
		sl.write("- Traduction des synopsis en français")

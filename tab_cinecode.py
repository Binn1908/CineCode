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
		sl.write('Chinnawat, Jacques, Khalid')

		sl.subheader('Mission')
		sl.write("- création d'un outil de recommandation de films...")

	with tab2:
		sl.subheader('Notre démarche')
		sl.write("- sélection des films sur la base des données d'IMDb...")

		sl.subheader('Outils utilisés')
		sl.write('- Pandas, Matplotlib, scikit-learn, Streamlit, API...')

	with tab3:
		sl.subheader('Machine Learning')
		sl.write('- k-NN...')

	with tab4:
		sl.subheader('Difficultés rencontrées')
		sl.write('- manque de diversité (genres)')
		sl.write('- dataset trop volumineux...')

		sl.subheader("Points d'amélioration")
		sl.write("- pour affiner les résultats : retravailler le dataset avec plus de choix et plus d'acteurs (vu que le format pickle permet des fichiers plus légers)")

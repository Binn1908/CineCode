from PIL import Image
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
		#sl.subheader("L'équipe")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>L'équipe</span>", unsafe_allow_html=True)
		image_group = Image.open('group.png')
		sl.image(image_group, width = 350)
		sl.write("Chinnawat, Khalid, Jacques")

		#sl.subheader("Mission")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>Mission</span>", unsafe_allow_html=True)
		sl.write("- Création d'un outil de recommandation de films pour un cinéma dans la Creuse souhaitant passer le cap du digital")		

	with tab2:
		#sl.subheader("Notre démarche")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>Notre démarche</span>", unsafe_allow_html=True)
		sl.write("- Exploration et nettoyage de la BDD IMDb afin de proposer aux locaux de la Creuse une sélection de films pertinents :")
		sl.write("	- Eliminer les données inutiles")
		sl.write("	- Corriger les erreurs")
		sl.write("	- Fusionner les différents datasets")
		sl.write("	- Normaliser les formats et filtrer les données")
		sl.write("- Utilisation d'un algorithme de machine learning pour recommander des films en fonction de films qui ont été appréciés par le spectateur")
		sl.write("- Création d’une interface utilisateur conviviale en utilisant Streamlit pour présenter les propositions")
			 			
		#sl.subheader("Outils utilisés")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>Outils utilisés</span>", unsafe_allow_html=True)
		sl.write("- Analyse et nettoyage des données : Pandas, Matplotlib")
		sl.write("- Machine learning : scikit-learn")
		sl.write("- Expérience utilisateur : Streamlit, IMDb API")

	with tab3:
		#sl.subheader("Machine Learning")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>Machine Learning</span>", unsafe_allow_html=True)
		sl.write("- Utilisation de l’algorithme KNN (K plus proches voisins) en raison de sa capacité à trouver des films similaires en fonction des préférences de l’utilisateur en se basant sur les caractéristiques des films et en identifiant les voisins les plus proches dans l’espace de caractéristiques")

	with tab4:
		#sl.subheader("Difficultés rencontrées")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>Difficultés rencontrées</span>", unsafe_allow_html=True)
		sl.write("- Filtrer la base de données IMDb sans perdre des films cultes/classiques")
		sl.write("- Volume du dataset final important : ralentissement du moteur de recommandation")
		
		#sl.subheader("Points d'amélioration")
		sl.write("<span style='font-size: 29px; color: #F8B405;'>Points d'amélioration</span>", unsafe_allow_html=True)
		sl.write("- Traduction des synopsis en français")

import streamlit as sl
from tab_main import tab_main
from tab_dataviz import tab_dataviz
from tab_cinecode import tab_cinecode
from tab_ressources import tab_ressources

#sl.set_page_config(layout = 'wide')

#sl.sidebar.title('CinéCode')

affiche = Image.open('affiche.png')
sl.sidebar.image(affiche)

tabs = {'Recommandation de film': tab_main,
		'Dataviz': tab_dataviz,
		'CinéCode': tab_cinecode,
		'Ressources': tab_ressources
		}
tab_selection = sl.sidebar.radio('', list(tabs.keys()))
tabs[tab_selection]()

sl.divider()
sl.caption('**CinéCode** - un projet à la [Wild Code School](https://www.wildcodeschool.com/)')

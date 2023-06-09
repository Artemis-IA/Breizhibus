import data.data as dd
import streamlit as st
import streamlit.web.bootstrap as stb
import os
import assets.style as style
from PIL import Image

query = "Select l.nom as ligne,h.heure,a.libelle as arret,a.adresse from horaires h left join arrets a on a.id=h.arret left join lignes l on l.id=h.ligne"

def main():

    style.style()

    global query
    dataframe=dd.format_heure(dd.get_data(query))
    
    map=Image.open('assets/pictures/map.png')
    
    st.title('BREIZHIBUS')
    st.image(map)

    option = st.selectbox('Choisissez votre ligne', dataframe['ligne'].unique())
    st.dataframe(dataframe[dataframe['ligne'] == option].reset_index(drop=True).drop('ligne', axis=1))

if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        streamlit_script_path = os.path.join(os.getcwd(), "Main.py")
        stb.run(streamlit_script_path,'',[],flag_options=[])
        main()
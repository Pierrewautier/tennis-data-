import streamlit as st
import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Configuration de la page
st.set_page_config(page_title="Tennis Abstract Modern", layout="wide")
st.title("🎾 Classement ATP & Statistiques (2026)")

# Connexion sécurisée à Kaggle (via les Secrets que nous allons régler)
if 'KAGGLE_USERNAME' in st.secrets:
    os.environ['KAGGLE_USERNAME'] = st.secrets['KAGGLE_USERNAME']
    os.environ['KAGGLE_KEY'] = st.secrets['KAGGLE_KEY']

    try:
        api = KaggleApi()
        api.authenticate()
        # Téléchargement du dataset que vous avez trouvé
        api.dataset_download_files('dissfya/atp-tennis-2000-2023daily-pull', path="./", unzip=True)
        
        # Lecture des données
        df = pd.read_csv('atp_tennis.csv')
        
        # Affichage du tableau propre
        st.subheader("Derniers matchs et classements")
        st.dataframe(df.head(20), use_container_width=True)
        
    except Exception as e:
        st.error(f"Erreur lors de la récupération des données : {e}")
else:
    st.info("Veuillez configurer vos clés API dans les Secrets de Streamlit.")

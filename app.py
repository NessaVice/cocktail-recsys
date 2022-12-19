import streamlit as st
import pandas as pd
from recsys_functions import *

cocktails = get_data()

st.image("./images/cocktail_row_removebg_glow.png")
st.title('Cocktail Recommender System')


selected_cocktail_name = st.selectbox(
    "Type or select a Cocktail from the dropdown menu",
    cocktails['Cocktail'].values
)

nb_of_recs = st.number_input(
    "Select the amount of recommendations you wish for :",
    min_value=1,
    max_value=30,
    value=10
)


col1, col2 = st.columns(spec=(5,1))

with col1:
    if st.button('Show Recommendation', type='primary'):
        find_cocktails = get_data()
        transform_result = transform_data(find_cocktails)

        recommendations = recommend_cocktails(selected_cocktail_name, find_cocktails, transform_result, nb_of_recs)

        print_reco_list(recommendations, nb_of_recs)

with col2:
    st.image("./images/clovis_wood_removebg_glow.png")
    st.caption("Number of drinks in database:")
    st.metric(
        label= "Number of drinks in database",
        value= len(cocktails),
        label_visibility='collapsed'
    )  

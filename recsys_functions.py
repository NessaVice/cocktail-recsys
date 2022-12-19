import streamlit as st
import pandas as pd
import scipy.sparse as sp
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


def get_data():
    cocktails_df = pd.read_csv('./data/final_cocktails.csv')
    cocktails_df = cocktails_df.sort_values(by=['Cocktail'])
    return cocktails_df

def transform_data(cocktails_df):

    additional_stop_words = ['oz', 'simple', 'dash', 'bsp', 'drops']
    cocktail_stop_words = list(ENGLISH_STOP_WORDS.union(additional_stop_words))

    count = CountVectorizer(stop_words=cocktail_stop_words, token_pattern=r'\b[^\d\W][^\d\W]+\b')
    count_matrix = count.fit_transform(cocktails_df['Ingredients'])

    tfidf = TfidfVectorizer(stop_words=cocktail_stop_words, token_pattern=r'\b[^\d\W][^\d\W]+\b')
    tfidf_matrix = tfidf.fit_transform(cocktails_df['Ingredients'])

    combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')   
    cosine_sim = cosine_similarity(combine_sparse, combine_sparse)
    
    return cosine_sim

def recommend_cocktails(cocktail_name, data, transformed, nb_of_recs):
    indices = pd.Series(data.index, index = data['Cocktail'])
    index = indices[cocktail_name]

    sim_scores = list(enumerate(transformed[index]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:nb_of_recs+1]

    cocktail_indices = [i[0] for i in sim_scores]

    c_name = data['Cocktail'].iloc[cocktail_indices]
    c_ingredients = data['Ingredients'].iloc[cocktail_indices]

    reco_data = pd.DataFrame(columns=['Cocktail', 'Ingredients'])

    reco_data['Cocktail'] = c_name
    reco_data['Ingredients'] = c_ingredients

    reco_data.index = pd.np.arange(1,len(reco_data)+1)

    return reco_data

def print_reco_list(recommendations, nb_of_recs):

    st.subheader("**Top {} Recommended Cocktails are :**\n".format(nb_of_recs))
    st.table(recommendations)
    # for i in range(len(recommendations)):
    #     name = recommendations['Cocktail'].iloc[i]
    #     ingredients = recommendations['Ingredients'].iloc[i]

    #     st.markdown("Name: {}".format(name))
    #     st.markdown("Ingredients: {}".format(ingredients))
    #     st.text("\n")
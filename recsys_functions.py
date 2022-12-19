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

    # count = CountVectorizer(stop_words=cocktail_stop_words, token_pattern=r'\b[^\d\W][^\d\W]+\b')
    # count_matrix = count.fit_transform(cocktails_df['Ingredients'])

    tfidf = TfidfVectorizer(stop_words=cocktail_stop_words, token_pattern=r'\b[^\d\W][^\d\W]+\b')
    tfidf_matrix = tfidf.fit_transform(cocktails_df['Ingredients'])

    # combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')   
    # similarity_df = cosine_similarity(combine_sparse, combine_sparse)

    ## other method ---
    cocktail_feature_df = pd.DataFrame(tfidf_matrix.toarray() ,columns=tfidf.get_feature_names_out(), index=cocktails_df['Cocktail'])
    similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    similarity_df = pd.DataFrame(similarity_matrix, columns=cocktail_feature_df.index, index=cocktail_feature_df.index)

    return similarity_df

def recommend_cocktails(cocktail_name, data, transformed, nb_of_recs):

    recommendations = transformed[cocktail_name].sort_values(ascending=False)[1:nb_of_recs+1]
    recommendations.name = 'Similarity'

    cocktails_details = data[data['Cocktail'].isin(recommendations.index)].set_index('Cocktail')

    reco_data = pd.concat([cocktails_details,recommendations], axis=1).sort_values(by='Similarity', ascending=False)
    reco_data = reco_data[['Ingredients']]

    return reco_data

def print_reco_list(recommendations, nb_of_recs):

    st.subheader("**Top {} Recommended Cocktails are :**\n".format(nb_of_recs))
    st.table(recommendations)

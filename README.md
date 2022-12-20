# Cocktail Recommender System

A recommendation system that helps you discover new drinks and your next favourite cocktail when you just can’t choose one based on their complicated names that hide what's inside!

## Context

When people go out and/or abroad, they want to try new drinks. However, not everyone has the same tastes; some like sweet drinks, some like sour ones, others prefer bitterness, some just want to get the most alcohol possible in their cocktail (without drinking pure alcohol out of a bottle), and some just want nice new tastes without alcohol at all.
Yet, there are so many different drinks all around the world hidden behind names that do not explain what is inside, in terms of ingredients or dosage, that a lot of people prefer to stick to their usual drinks, in fear of wasting money on a cocktail they will not enjoy. Thus, it would be interesting to offer an application that could recommend cocktails based on similar liked ones and/or **ingredients**.

This application is up for (many) possible improvements.

## Data Collection - Cleaning - Preprocessing

1. **./preprocessing/exploring_data.ipynb** : a Python notebook where webscrapping from the Cocktail DB site was realized and all datasets were adjusted to fit together. Columns of interest were then selected for a final output CSV file used for the system
2. **3 CSV files** : 2 datasets from Kaggle and 1 from the web scrapping (see 1.)

## Algorithm

### Sources

- Streamlit with Heroku template : <https://github.com/patryk-oleniuk/streamlit-heroku-template>
- Streamlit : <https://www.streamlit.io/>
- Heroku : <https://www.heroku.com/home> Free plan
- The CocktailDB : <https://www.thecocktaildb.com/api.php>
- Kaggle dataset - "Cocktails data" : <https://www.kaggle.com/datasets/svetlanagruzdeva/cocktails-data>
- Kaggle dataset - "Cocktails (Hotaling & Co.)" : <https://www.kaggle.com/datasets/shuyangli94/cocktails-hotaling-co>

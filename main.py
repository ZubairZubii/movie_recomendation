import pandas as pd
import numpy as np

movies =  pd.read_csv('tmdb_5000_movies.csv')
credits =  pd.read_csv('tmdb_5000_credits.csv')

#print(movies.head())
#print(credits.head()['title'])
movies = movies.merge(credits, on='title')
#print(movies.columns.values)
movies = movies[['movie_id', 'title' , 'overview' , 'genres' , 'keywords' , 'cast' , 'crew']]
#print(movies.head())
#print(movies.isnull().sum())
movies.dropna(inplace=True)
#print(movies.isnull().sum())
#print(movies['genres'][0])

#if uou want to convert string into list then use ast funtion
import ast
def convert_genres_keyword(text):
    gen_array=[]
    for i in ast.literal_eval(text):
        gen_array.append(i['name'])
    return gen_array

movies['genres'] = movies['genres'].apply(convert_genres_keyword)
#print(movies['genres'][1])
#print(movies['keywords'][0])
movies['keywords'] = movies['keywords'].apply(convert_genres_keyword)
#print(movies['keywords'][0])

#print(movies['cast'][0])
def convert_cast(text):
    gen_array=[]
    count = 0
    for i in ast.literal_eval(text):
        if count!=3:
            gen_array.append(i['name'])
            count+=1
        else:
            break
    return gen_array

movies['cast'] = movies['cast'].apply(convert_genres_keyword)
#print(movies['cast'][0])
def convert_crew(text):
    gen_array=[]
    for i in ast.literal_eval(text):
            if i['job'] =='Director':
                gen_array.append(i['name'])
    return gen_array

movies['crew'] = movies['crew'].apply(convert_crew)

#print(movies.head())

movies['overview'] = movies['overview'].apply(lambda x: x.split())
#print(movies['overview'][0])

movies['genres'] = movies['genres'].apply(lambda x : [i.replace(' ','') for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x : [i.replace(' ','') for i in x])
movies['cast'] = movies['cast'].apply(lambda x : [i.replace(' ','') for i in x])
movies['crew'] = movies['crew'].apply(lambda x : [i.replace(' ','') for i in x])

#print(movies.head())
movies['tags'] = movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
new_movies = movies[['movie_id' , 'title' , 'tags']]
#print(new_movies.head())
new_movies  = pd.DataFrame(new_movies)
new_movies['tags'] = new_movies['tags'].apply(lambda x : " ".join(x))
#print(new_movies['tags'][0])
new_movies['tags'] = new_movies['tags'].apply(lambda x : x.lower())
#print(new_movies['tags'][0])

#from sklearn.feature_extraction.text import CountVectorizer
#c = CountVectorizer(max_features=5000 , stop_words='english')
#vector  = c.fit_transform(new_movies['tags']).toarray()
#print(vector[0])
#print(c.get_feature_names_out())

import nltk
from nltk.stem.porter import PorterStemmer
st = PorterStemmer()
def stem(text):
    s = []
    for i in text.split():
        s.append(st.stem(i))
    return ' '.join(s)

new_movies['tags'] = new_movies['tags'].apply(stem)
from sklearn.feature_extraction.text import CountVectorizer

c = CountVectorizer(max_features=5000 , stop_words='english')
vector  = c.fit_transform(new_movies['tags']).toarray()
#print(vector[0])
#print(c.get_feature_names_out())

from sklearn.metrics.pairwise import cosine_similarity
simmilarity = cosine_similarity(vector)

def recommend(movie):
    movie_index = new_movies[new_movies['title'] == movie].index[0]
    distance =simmilarity[movie_index]
    movie_list = sorted(list(enumerate(distance)) , reverse=True ,key=lambda x: x[1])[1:6]
    recomm_movie=[]
    recomm_movie_path=[]
    for i in movie_list:
        movieid = new_movies.iloc[i[0]].movie_id
        recomm_movie.append(new_movies.iloc[i[0]].title)
        recomm_movie_path.append(fetch_poster(movieid))
    return recomm_movie,recomm_movie_path


import requests
#recommend('Avatar')
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9000b5b1d98bb152aa1f762fecb8e38d&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w185/" + data['poster_path']


import streamlit as st
st.title('MOVIE RECOMMEND SYSTEM')

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    (new_movies['title'].values))


if st.button('Recommend '):
    names,posters=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

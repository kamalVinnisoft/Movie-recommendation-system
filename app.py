import streamlit as st
import pickle 
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-Us')
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
       recommend_movies.append(movies.iloc[i[0]].title)
    #    recommend_movies_posters.append(fetch_poster(i[1]))
    return recommend_movies


# Load the movies dictionary
with open('movies_dict.pkl', 'rb') as f:
    movie_dict = pickle.load(f)

# Convert dictionary to a DataFrame
movies = pd.DataFrame(movie_dict)
print(movies['title'])
# Load the similarities dictionary
with open('similarity.pkl', 'rb') as f:
    similarity_dict = pickle.load(f)

# Convert dictionary to a DataFrame
similarity = pd.DataFrame(similarity_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('How would you like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
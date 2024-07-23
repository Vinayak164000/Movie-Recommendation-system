import pickle
import streamlit as st
import requests

st.header('Movies Recommendation System')
movies = pickle.load(open('mvoies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    print(index)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show recommendation'):
    recommended_movie_name = recommend(selected_movie)
    st.write(recommended_movie_name)
    # with col1:
    #     st.text(recommended_movie_name[0])
    # with col2:
    #     st.text(recommended_movie_name[1])
    # with col3:
    #     st.text(recommended_movie_name[2])
    # with col4:
    #     st.text(recommended_movie_name[3])
    # with col5:
    #     st.text(recommended_movie_name[4]) 



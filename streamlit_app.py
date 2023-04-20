import streamlit
import pandas
streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 omeg 3 & Blueberry oatmeal')
streamlit.text('🥗 kale,spinach and Rocket smoothie')
streamlit.text(' 🐔 Hard-boiled freerange eggs')
streamlit.text(' 🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
               

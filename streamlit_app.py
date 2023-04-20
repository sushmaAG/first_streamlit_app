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
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.Fruit)) - can be used instead  of 11 and 13 works better than no 11.

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
               

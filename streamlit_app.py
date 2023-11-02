import streamlit 
import pandas

streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Kale, Spinach & Rocket smoothie')
streamlit.text('🥗Hard Boiled egg free range egg')
streamlit.text('🥑🍞Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

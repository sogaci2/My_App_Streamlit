import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
  
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandans

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruityvice_normalized)
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')   #,'Kiwi') 
   if not fruit_choice:
        streamlit.error("Please select a fruit ot get information. ")
   else:
        back_from_function=get_fruityvice_date(fruit_choice)
        streamlit.dataframe(back_from_function)
        
#streamlit.text(fruityvice_response.json())
except URLError as e:
    streamlit.error()


#don't run anything past here while troubleshoot

streamlit.stop()

#import snowflake.connector 

streamlit.header("The fruit load list contains :")

#snowflake-related functins

def get_fruit_load():
    whith my_cnx.cursor() as my_cur:
          my_cur.execute("SELECT * FROM fruit_load_list")
          retrn my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load()
   streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add ?','jackfruit')
#streamlit.write('The user entered ', add_my_fruit)


fruityvice_replay = requests.get("https://fruityvice.com/api/fruit/" + "jackfruit")
streamlit.write('Thanks for adding ', add_my_fruit)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")


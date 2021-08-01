#----------- Welcome to the Streamlit template provided by So you want to be a data scientist? -----------#

#	In this template, we will:
# 		* go over the commonly used Streamlit structures
#		* learn how to collect input from the user
#		* see how to import data
# 		* learn how to customize the app
#		* have some examples on visualizing the data

# FIRST: Run the app, interact with it, and then come back and go through the code

# TO RUN THE APP:
#	* open terminal
#	* navigate to streamlit file location
#	* to install required libraries, run: "pip install -r requirements.txt"
#	* use command: "streamlit run streamlit_template.py"


# Need more help understanding and setting up your Streamlit app? Check out my tutorial on YouTube: https://www.youtube.com/watch?v=-IM3531b1XU&list=PLM8lYG2MzHmTATqBUZCQW9w816ndU0xHc
# You can get more information on everything on the Streamlit documentation: https://docs.streamlit.io/en/stable/api.html


# The data being used in this app is a truncated version of the data that you can download here: https://s3.amazonaws.com/tripdata/index.html
# more info about the data can be found here: https://www.citibikenyc.com/system-data


# I've added ToDos for you to interact with the template and get familiar with it
# Search for the phrase "TODO" and you'll see them


# 1 --- first and foremost, we import the necessary libraries
import pandas as pd
import streamlit as st


#######################################





# 2 --- you can add some css to your Streamlit app to customize it
# TODO: Change values below and observer the changes in your app
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
#######################################






# 3 --- build the structure of your app


# Streamlit apps can be split into sections


# container -> horizontal sections
# columns -> vertical sections (can be created inside containers or directly in the app)
# sidebar -> a vertical bar on the side of your app


# here is how to create containers
header_container = st.beta_container()
stats_container = st.beta_container()	
#######################################



# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container
with header_container:

	# for example a logo or a image that looks like a website header
	st.image('logo.png')

	# different levels of text you can include in your app
	st.title("NBA 2K League Stats Explorer")
	st.header("All Data from https://2kleague.nba.com/stats/")
	st.subheader("WEB APP Created by @IAMHKTR")
	








# Another container
with stats_container:





	# 4 --- You import datasets like you always do with pandas
	# 		if you'd like to import data from a database, you need to set up a database connection
	data = pd.read_csv('JC-202103-citibike-tripdata.csv')







	# 5 --- You can work with data, change it and filter it as you always do using Pandas or any other library
	start_station_list = ['All'] + data['start station name'].unique().tolist()
	end_station_list = ['All'] + data['end station name'].unique().tolist()








	# 6 --- collecting input from the user
	#		Steamlit has built in components to collect input from users


	

	# collect input usinga list of options in a drop down format
	# TODO: change the option list to end_station_list and see what happens
	st.write('You can filter data by team')
	s_station = st.selectbox('Which team would you like to see?', start_station_list, key='start_station')

	# display the collected input
	st.write('You selected the Player: ' + str(s_station))

	# you can filter/alter the data based on user input and display the results in a plot
	st.write('And display things based on what the user has selected')
	if s_station != 'All':
		display_data = data[data['start station name'] == s_station]

	else:
		display_data = data.copy()


	# display the dataset in a table format
	# if you'd like to customize it more, consider plotly tables: https://plotly.com/python/table/
	# I have a YouTube tutorial that can help you in this: https://youtu.be/CYi0pPWQ1Do
	st.write(display_data)


	





	
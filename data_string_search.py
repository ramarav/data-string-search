import streamlit as st
import streamlit_analytics
import pandas as pd
from IPython.display import HTML
from functools import reduce

streamlit_analytics.start_tracking()

#Page configuration
st.set_page_config(layout="wide")


#Dataframe from imported JIRA query (as CSV)
df = pd.read_csv('t1.csv')

#Page starting
st.header(':rainbow[Welcome to Data String Search]')
#Showing raw data to user
see_data = st.expander("Click here to see the raw data")
with see_data:
    st.dataframe(data=df.reset_index(drop=True))



#Increase font size of user input
tabs_font_css = """
<style>

div[class*="stTextInput"] label p {
  font-size: 26px;
  color: blue;
}

</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

#User query
key=st.text_input("Search car category")

#Get keywords from user query
key1=key.split()

#Search the query elements in dataframe & make the key clickable (Main logic)
if key1:
    st.write(df[reduce(lambda a,b : a&b,(df['category'].str.casefold().str.contains(s.casefold()) for s in key1))])

st.markdown("")
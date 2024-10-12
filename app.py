import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import os

from pathlib import Path


file_path = Path('vehicles_us.csv')

if file_path.exists():
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print("File does NOT exist.")

file_path = Path("C:/Users/nsuka/Desktop/Project/Car_Sales_Project/vehicles_us.csv")
df = pd.read_csv(file_path)



df.head()



# Add a header
st.header("Car Listings Analysis")

# create a plotly express histogram
fig = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig)

# st.write(fig_hist)

show_only_4wd = st.checkbox("Show only 4WD vehicles")

if show_only_4wd:
    df = df[df['is_4wd'] == 1.0]


fig_hist = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.write(fig_hist)
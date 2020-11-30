#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangYicheng
@file:test.py
@time:2020/11/27
"""
import streamlit as st
import pandas as pd

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_excel('results.xlsx', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.dataframe(data.style.highlight_max(axis=0), width=10000, height=10000)

import time

'Starting a long computation...'

def inner_func(a, b):
    st.write("inner_func(", a, ",", b, ") ran")
    return a ** b


@st.cache(suppress_st_warning=True)  # Changed this
def expensive_computation(a, b):
    # Added this
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return inner_func(a, b) + 1


a = 2
b = 20
res = expensive_computation(a, b)
st.write("Result:", res)

# left_column, right_column = st.beta_columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")
# chosen = right_column.radio('Sorting hat',
#                             ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
# right_column.write(f"You are in {chosen} house!")

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
# # Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)
# '...and now we\'re done!'


if __name__ == '__main__':
    pass

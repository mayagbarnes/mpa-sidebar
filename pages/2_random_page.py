import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.set_page_config(page_title='Random')


# Build a bunch of data to display
df1 = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=[0, 1, 2], columns=['AA', 'BB', 'CC'])
df4 = (df1 * 111).rename(columns={'AA': 'DD', 'BB': 'EE', 'CC': 'FF'}).copy()
df2 = df1.join(df4) * 1000
df3 = df4.join(df1) * 11111

c1, c2, c3 = st.columns((1, 2, 3))

c1.subheader('Data A')
c1.write(df1)
c2.subheader('Data B')
c2.write(df2)
c3.subheader('Data C')
c3.write(df3)
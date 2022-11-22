import streamlit as st
import numpy as np
import pandas as pd

st.write("#Web test : sunglasses:")

st.write("## Chart : heart:")
#num = [100, 150, 50]

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
#st.line_chart(num)
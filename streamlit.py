#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go
import time


# In[ ]:


data=pd.read_csv("finvizdata.csv")


# In[ ]:


#price_=data.price.tolist()
#change_percentage_=data.change_percentage.tolist()
#ticker_=data.ticker.tolist()
fig=px.treemap(data, path=[px.Constant('Athens Stock Exchange'),'group','tickerperc'],values = 'capitalization', color = 'change_percentage',color_continuous_scale=['Red','Red','Red','Red','Red','Red','Red','crimson','firebrick','gray','Green','limegreen','limegreen','lime','lime','lime','lime','lime','lime'],color_continuous_midpoint=0)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.update_traces(marker_line=dict(color="black"))
fig.update_traces(marker_line_width = 0.5)
#fig.data[0].customdata = np.column_stack([price_, change_percentage_,ticker_])
#fig.data[0].texttemplate = "Ticker:%{customdata[2]}<br>Price:$%{customdata[0]}<br>Percentage Change:%{customdata[1]:.2f}%"
st.header('Athens Stock Exchange Tree Map')
st.subheader("This is a map that shows the Greek stock market's performance. The map is being refreshed every 10 minutes.")
st.write('To view in full screen, hover your mouse over the map and click on the expand arrows on the top right corner')
st.plotly_chart(fig, use_container_width=True)


# In[ ]:





# In[ ]:





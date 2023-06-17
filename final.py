#!/usr/bin/env python
# coding: utf-8

# In[314]:


get_ipython().system('pip install --upgrade yfinance')
import yfinance as yf
import pandas as pd
get_ipython().system('pip install nbformat==5.7')
from bs4 import BeautifulSoup


# In[315]:


import requests as re
get_ipython().system('pip install plotly')
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[316]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[317]:


ticker = yf.Ticker('TSLA')


# In[318]:


tesla_data = ticker.history(period="max")


# In[319]:


tesla_data.reset_index(inplace=True)


# In[320]:


tesla_data.head(5)


# In[321]:


url = ' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
r = re.get(url)


# In[322]:


soup = BeautifulSoup(r.content, 'html.parser')


# In[323]:


tesla_revenue = pd.read_html(str(soup))[0]


# In[324]:


tesla_revenue.columns=['Date','Revenue']


# In[325]:


tesla_revenue.Date = pd.to_datetime(tesla_revenue.Date,format='%Y')


# In[343]:


tesla_revenue['Revenue']=tesla_revenue['Revenue'].str.replace(',','')
tesla_revenue['Revenue']=tesla_revenue['Revenue'].str.replace('$','')


# In[344]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[345]:


tesla_revenue.tail(5)


# In[328]:


stock = yf.Ticker('GME')


# In[329]:


gme=stock.history(period = 'max')


# In[330]:


gme_data=gme.reset_index()


# In[331]:


gme_data.head(5)


# In[332]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"


# In[333]:


html_data = re.get(url)


# In[334]:


beautiful_soup = BeautifulSoup(r.content, 'html.parser')


# In[335]:


reader = pd.read_html(str(beautiful_soup))


# In[336]:


gme_revenue = reader[1]


# In[337]:


gme_revenue.columns = ["Date", "Revenue"]


# In[338]:


gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace(',','')
gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace('$','')
gme_revenue.dropna(inplace=True)


# In[339]:


gme_revenue.tail()


# In[340]:


make_graph(tesla_data, tesla_revenue, 'Historical share price and revenue of Tesla')


# In[341]:


make_graph(gme_data, gme_revenue, 'Historical Share Price and Revenue of GameStop')


# In[ ]:





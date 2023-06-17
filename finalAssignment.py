#!/usr/bin/env python
# coding: utf-8

# In[401]:


get_ipython().system('pip install --upgrade yfinance')
import yfinance as yf
import pandas as pd
get_ipython().system('pip install nbformat==5.7')
from bs4 import BeautifulSoup


# In[402]:


import requests as re
get_ipython().system('pip install plotly')
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[403]:


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


# In[404]:


ticker = yf.Ticker('TSLA')


# In[405]:


tesla_data = ticker.history(period="max")


# In[406]:


tesla_data.reset_index(inplace=True)


# In[407]:


tesla_data.head(5)


# In[408]:


url = ' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
r = re.get(url)


# In[409]:


soup = BeautifulSoup(r.content, 'html.parser')


# In[410]:


tesla_revenue=pd.read_html(str(soup))[1]


# In[411]:


tesla_revenue.columns=['Date','Revenue']


# In[412]:


tesla_revenue['Revenue']=tesla_revenue['Revenue'].str.replace(',','')
tesla_revenue['Revenue']=tesla_revenue['Revenue'].str.replace('$','')


# In[413]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[414]:


tesla_revenue.tail(5)


# In[415]:


stock = yf.Ticker('GME')


# In[416]:


gme=stock.history(period = 'max')


# In[417]:


gme_data=gme.reset_index()


# In[418]:


gme_data.head(5)


# In[419]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"


# In[420]:


html_data = re.get(url)


# In[421]:


k = BeautifulSoup(html_data.content, 'html.parser')


# In[422]:


reader = pd.read_html(str(k))


# In[423]:


gme_revenue = reader[1]


# In[424]:


gme_revenue.columns = ["Date", "Revenue"]


# In[425]:


gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace(',','')
gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace('$','')
gme_revenue.dropna(inplace=True)


# In[426]:


gme_revenue.tail()


# In[429]:


get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.prototype._should_scroll = function(lines) {\n    return false;\n}\n')


# In[430]:


make_graph(tesla_data, tesla_revenue, 'Historical share price and revenue of Tesla')


# In[428]:


make_graph(gme_data, gme_revenue, 'Historical Share Price and Revenue of GameStop')


# In[ ]:





# In[ ]:





# In[ ]:





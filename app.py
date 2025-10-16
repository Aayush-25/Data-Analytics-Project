import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

DB_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/etl_demo")
engine = create_engine(DB_URL, future=True)

st.title("ETL Dashboard — Orders KPIs")

@st.cache_data(ttl=300)
def get_kpis():
    q = "SELECT count(*) as orders, coalesce(sum(total_price),0) as revenue FROM orders;"
    return pd.read_sql(q, engine)

kpis = get_kpis()
st.metric("Total orders", int(kpis['orders'].iloc[0]))
st.metric("Total revenue", float(kpis['revenue'].iloc[0]))

st.subheader("Top cities by revenue")
df_city = pd.read_sql("SELECT city, sum(total_price) as revenue FROM orders GROUP BY city ORDER BY revenue DESC LIMIT 20", engine)
st.dataframe(df_city)
st.bar_chart(df_city.set_index('city')['revenue'])
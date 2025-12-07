import streamlit as st
import pandas as pd
from storage import load_reviews

st.title("📊 Admin Dashboard")

data = load_reviews()

if not data:
    st.info("No reviews yet.")
else:
    df = pd.DataFrame(data)
    st.subheader("All Reviews")
    st.dataframe(df)

    st.subheader("Analytics")
    st.write("Total Reviews:", len(df))
    st.write("Average Rating:", df["rating"].mean().round(2))

    st.bar_chart(df["rating"])

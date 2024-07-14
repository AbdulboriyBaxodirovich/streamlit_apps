import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Auto")


st.write("## Tahlil")

df = pd.read_csv("ped_crashes.csv")
st.dataframe(df)

st.line_chart(df["Speed Limit at Crash Site"])
bin = st.select_slider(
    "select bin number",
    options=list(range(1, 26)))

fig, ax = plt.subplots()
sns.histplot(df['Speed Limit at Crash Site'], bins=bin, ax=ax)
st.pyplot(fig)

genre = st.radio(
    label = "Tajriba Darajasini Tanlang",
    options = df['Crash Month'].unique().tolist(),
    index=None,
)

if st.button("Show Table"):
    st.write("You selected:", genre)
    
    # Har bir oy uchun mos shartlar
    match genre:
        case "January":
            st.dataframe(df[df["Crash Month"] == "January"])
        case "February":
            st.dataframe(df[df["Crash Month"] == "February"])
        case "March":
            st.dataframe(df[df["Crash Month"] == "March"])
        case "April":
            st.dataframe(df[df["Crash Month"] == "April"])
        case "May":
            st.dataframe(df[df["Crash Month"] == "May"])
        case "June":
            st.dataframe(df[df["Crash Month"] == "June"])
        case "July":
            st.dataframe(df[df["Crash Month"] == "July"])
        case "August":
            st.dataframe(df[df["Crash Month"] == "August"])
        case "September":
            st.dataframe(df[df["Crash Month"] == "September"])
        case "October":
            st.dataframe(df[df["Crash Month"] == "October"])
        case "November":
            st.dataframe(df[df["Crash Month"] == "November"])
        case "December":
            st.dataframe(df[df["Crash Month"] == "December"])
else:
    pass

tab1, tab2, tab3, tab4 = st.tabs(["Crash Year", "Crash Month", "Crash Day", "Speed Limit at Crash Site"])

with tab1:
    st.header("Crash Year")
    # Crash Year uchun grafik chizish
    if "Crash Year" in df.columns:
        st.line_chart(df["Crash Year"].value_counts().sort_index())
    else:
        st.error("Crash Year ustuni topilmadi.")

with tab2:
    st.header("Crash Month")
    # Crash Month uchun grafik chizish
    if "Crash Month" in df.columns:
        st.line_chart(df["Crash Month"].value_counts().sort_index())
    else:
        st.error("Crash Month ustuni topilmadi.")

with tab3:
    st.header("Crash Day")
    # Crash Day uchun grafik chizish
    if "Crash Day" in df.columns:
        st.line_chart(df["Crash Day"].value_counts().sort_index())
    else:
        st.error("Crash Day ustuni topilmadi.")

with tab4:
    st.header("Speed Limit at Crash Site")
    # Speed Limit at Crash Site uchun grafik chizish
    if "Speed Limit at Crash Site" in df.columns:
        st.line_chart(df["Speed Limit at Crash Site"].value_counts().sort_index())
    else:
        st.error("Speed Limit at Crash Site ustuni topilmadi.")
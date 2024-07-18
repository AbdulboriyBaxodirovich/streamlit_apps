import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Rielter")


st.write("## Uylar bo'yicha ma'lumotlar")

df = pd.read_csv("2.csv")
st.dataframe(df)

st.line_chart(df["Price"])
bin = st.select_slider(
    "select bin number",
    options=list(range(1, 30)))

fig, ax = plt.subplots()
sns.histplot(df['Built Year'], bins=bin, ax=ax)
st.pyplot(fig)

genre = st.radio(
    label = "Tajriba Darajasini Tanlang",
    options = ["Lot area < 1000", "1000 <= Lot area < 10000", "10000 <= Lot area < 20000", "20000 <= Lot area < 30000", "30000 <= Lot area < 40000", "40000 <= Lot area < 50000", "50000 <= Lot area < 60000", "60000 <= Lot area < 70000", "70000 <= Lot area < 80000", 
               "80000 <= Lot area < 90000", "90000 <= Lot area < 100000", "100000 <= Lot area < 150000", "150000 <= Lot area < 200000", "200000 <= Lot area < 250000", "250000 <= Lot area"],
    index=None,
)

if st.button("Show Table"):
    st.write("You selected:", genre)
    
    # Har bir oy uchun mos shartlar
    match genre:
        case "Lot area < 1000":
            st.dataframe(df[df["lot area"] < 1000])
        case "1000 <= Lot area < 10000":
            st.dataframe(df[(df["lot area"] >= 1000) & (df["lot area"] < 10000)])
        case "10000 <= Lot area < 20000":
            st.dataframe(df[(df["lot area"] >= 10000) & (df["lot area"] < 20000)])
        case "20000 <= Lot area < 30000":
            st.dataframe(df[(df["lot area"] >= 20000) & (df["lot area"] < 30000)])
        case "30000 <= Lot area < 40000":
            st.dataframe(df[(df["lot area"] >= 30000) & (df["lot area"] < 40000)])
        case "40000 <= Lot area < 50000":
            st.dataframe(df[(df["lot area"] >= 40000) & (df["lot area"] < 50000)])
        case "50000 <= Lot area < 60000":
            st.dataframe(df[(df["lot area"] >= 50000) & (df["lot area"] < 60000)])
        case "60000 <= Lot area < 70000":
            st.dataframe(df[(df["lot area"] >= 60000) & (df["lot area"] < 70000)])
        case "70000 <= Lot area < 80000":
            st.dataframe(df[(df["lot area"] >= 70000) & (df["lot area"] < 80000)])
        case "80000 <= Lot area < 90000":
            st.dataframe(df[(df["lot area"] >= 80000) & (df["lot area"] < 90000)])
        case "90000 <= Lot area < 100000":
            st.dataframe(df[(df["lot area"] >= 90000) & (df["lot area"] < 100000)])
        case "100000 <= Lot area < 150000":
            st.dataframe(df[(df["lot area"] >= 100000) & (df["lot area"] < 150000)])
        case "150000 <= Lot area < 200000":
            st.dataframe(df[(df["lot area"] >= 150000) & (df["lot area"] < 200000)])
        case "200000 <= Lot area < 250000":
            st.dataframe(df[(df["lot area"] >= 200000) & (df["lot area"] < 250000)])
        case "250000 <= Lot area":
            st.dataframe(df[df["lot area"] >= 250000])
else:
    pass
# Ustunlar ro'yxati
columns = ['number of bedrooms', 'number of bathrooms',
            'living area', 'lot area', 'number of floors', 'waterfront present',
            'number of views', 'condition of the house', 'grade of the house',
            'Area of the house(excluding basement)', 'Area of the basement',
            'Built Year', 'Renovation Year', 'Postal Code', 'Lattitude',
            'Longitude', 'living_area_renov', 'lot_area_renov',
            'Number of schools nearby', 'Distance from the airport', 'Price']

# Zakladkalarni yaratish
tabs = st.tabs(columns)

# Har bir zakladka uchun mos grafik chizish
for tab, column in zip(tabs, columns):
    with tab:
        st.write(f"**{column}** uchun ma'lumotlar:")
        ustun1 = ['living area', 'lot area', 'Area of the house(excluding basement)', 
                        'Area of the basement', 'living_area_renov', 'lot_area_renov', 'Price']
            
        plt.figure(figsize=(10, 6))
            
        if column in ['number of bedrooms', 'number of bathrooms', 'number of floors', 
                        'waterfront present', 'number of views', 'condition of the house', 
                        'grade of the house', 'Number of schools nearby', 
                        'Distance from the airport']:
            # Barplot
            st.subheader("Barplot")
            bar_fig, ax = plt.subplots()
            df['Number of schools nearby'].value_counts().plot(kind='bar', color='blue', edgecolor='black', ax=ax)
            ax.set_xlabel(column)
            ax.set_ylabel('Count')
            ax.set_title(f'Barplot for {column}')
            st.pyplot(bar_fig)

            if column == "Number of schools nearby":

                # Pirog grafik
                st.subheader("Pirog Grafik")
                schools_count = df['Number of schools nearby'].value_counts()
                pie_fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(schools_count, labels=schools_count.index, autopct='%1.1f%%', startangle=90)
                ax.set_title('Pirog Grafik for Number of Schools Nearby')
                ax.axis('equal')  # Tenglikni ta'minlash
                st.pyplot(pie_fig)

            if column == "number of bedrooms":

                # Pirog grafik
                st.subheader("Pirog Grafik")
                schools_count = df['number of bedrooms'].value_counts()
                bed_fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(schools_count, labels=schools_count.index, autopct='%1.1f%%', startangle=90)
                ax.set_title('Pirog Grafik for number of bedrooms')
                ax.axis('equal')  # Tenglikni ta'minlash
                st.pyplot(bed_fig)

        elif column in ustun1:
            st.write(df[[column]].describe())
            # Box plot
            sns.boxplot(x=df[column], color='blue')
            plt.xlabel(column)
            plt.title(f'{column} uchun Boxplot')
            st.pyplot(plt)

        elif column in ['Lattitude', 'Longitude', 'Built Year', 'Renovation Year']:
            # Histogram
            plt.hist(df[column].dropna(), bins=30, color='blue', edgecolor='black')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'{column} uchun Histogram')
            st.pyplot(plt)

            if column == "Renovation Year":
                # Pirog grafik
                st.subheader("Pirog Grafik")
                schools_count = df['Renovation Year'].value_counts()
                pie_fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(schools_count, labels=schools_count.index, autopct='%1.1f%%', startangle=90)
                ax.set_title('Pirog Grafik for Number of Schools Nearby')
                ax.axis('equal')  # Tenglikni ta'minlash
                st.pyplot(pie_fig)  

        elif column == 'Date':
            # Line plot
            df['Date'] = pd.to_datetime(df['Date'])
            df.groupby(df['Date'].dt.to_period('M')).size().plot(kind='line')
            plt.xlabel('Date')
            plt.ylabel('Count')
            plt.title(f'{column} uchun Line Plot')
            st.pyplot(plt)

        else:
            # Scatter plot for Unnamed: 0 and id
            plt.scatter(df.index, df[column], color='blue')
            plt.xlabel('Index')
            plt.ylabel(column)
            plt.title(f'{column} uchun Scatter Plot')
            st.pyplot(plt)

        plt.grid(True)
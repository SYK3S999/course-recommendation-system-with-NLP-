import streamlit as st
import streamlit.components.v1 as stc
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


@st.cache_data
def about_page(df):
    
    st.title("Here are some visualisations about our dataset")
    st.write(f"Number of Rows: {df.shape[0]}")
    st.markdown("### Dataset Overview")
    st.write(f"Number of Columns: {df.shape[1]}")
    st.write("Data Types:")
    st.write(df.dtypes)
    st.write("Summary Statistics:")
    st.write(df.describe())

        # Data Visualizations

    st.markdown("### Data Visualizations")
        # Distribution of Course Prices
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(figsize=(10, 6))
    st.subheader("Distribution of Course Prices")
    sns.histplot(df['price'], bins=20, kde=True)
    st.pyplot()

        # Word Cloud for Course Titles
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['course_title']))
    st.subheader("Word Cloud for Course Titles")
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

        # Distribution of Subscribers
    st.subheader("Distribution of Subscribers")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['num_subscribers'], bins=20, kde=True)
    st.pyplot()

        # Price Distribution by Category
    st.subheader("Price Distribution by Subject")
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='subject', y='price', data=df)
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

        # Course Duration Distribution
    st.subheader("Course Duration Distribution")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['content_duration'], bins=20, kde=True)
    st.pyplot()

        # Display a sample of the dataset
    st.markdown("### Sample of the Dataset")
    st.dataframe(df.head(10))
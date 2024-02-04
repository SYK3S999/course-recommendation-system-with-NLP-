import streamlit as st
import pandas as pd
import spacy
import streamlit.components.v1 as stc
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

from about_page import about_page
from home_page import home_page

# Load spaCy model 
spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_md')

# Load DataFrame

df = pd.read_csv("data/udemy_course_data.csv")

# Recommendation function incorporating spaCy word embeddings
@st.cache_data
def get_recommendation_nlp(title, df, num_of_rec=10):
    # Process the search term using spaCy
    search_doc = nlp(title)

    # Calculate similarity using word embeddings
    sim_scores = df['course_title'].apply(lambda doc: search_doc.similarity(nlp(doc)))

    # Get the indices of courses with the highest similarity
    selected_course_indices = sim_scores.argsort()[:-num_of_rec-1:-1]
    selected_course_scores = sim_scores[selected_course_indices]

    result_df = df.iloc[selected_course_indices].copy()
    result_df['similarity_score'] = selected_course_scores

    return result_df

# Main Streamlit app
def main():
    # Set page title and favicon
    st.set_page_config(
        
        page_icon=":mortar_board:",
        layout="wide"
    )

    # Custom CSS styling
    st.markdown("""
        <style>
            .streamlit-container {
                max-width: 90%;
            }
            .streamlit-button {
                background-color: #3498db;
                color: #ffffff;
                padding: 8px 16px;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .streamlit-button:hover {
                background-color: #2980b9;
            }
            .streamlit-input {
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 8px 12px;
                margin-bottom: 16px;
            }
            .streamlit-table {
                background-color: #ffffff;
            }
        </style>
    """, unsafe_allow_html=True)

 

    menu = ["Home", "Recommend", "Visualisations"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home_page()

    elif choice == "Recommend":
        st.subheader("Recommend Courses")

        search_term = st.text_input("Search")
        num_of_rec = st.sidebar.number_input("Number", 4, 30, 7)

        if st.button("Recommend"):
            if search_term is not None:
                    with st.spinner("Finding Recommendations..."):
                        try:
                            result = get_recommendation_nlp(search_term, df, num_of_rec=num_of_rec)
                        except:
                            result = "Not Found"

                        if isinstance(result, str):
                            st.warning(result)
                        else:
                            # Sort the recommendations by multiple criteria
                            result = result.sort_values(by=["similarity_score", "num_subscribers", "price"],
                                                        ascending=[False, False, True])

                            # Display recommendations in colorful cards
                            for index, row in result.iterrows():
                                st.markdown(
                                    f'<div style="background-color: #e6f7ff; padding: 15px; border-radius: 10px; margin-bottom: 15px;">'
                                    f'<h2 style="color: #005580;">{row["course_title"]}</h2>'
                                    f'<p style="color: #1a1a1a;">Price: ${row["price"]} | Students: {row["num_subscribers"]} | Similarity Score: {row["similarity_score"]:.2f}</p>'
                                    f'<a href="{row["url"]}" style="color: #ff6600; font-weight: bold;">Link to Course</a>'
                                    f'</div>', unsafe_allow_html=True)

                    
            else:
                st.warning("Please enter a search term.")


    elif choice == "Visualisations":
        
        about_page(df)

if __name__ == '__main__':
    main()

import streamlit as st
import streamlit.components.v1 as stc




@st.cache_data
def home_page():

    stc.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }

                .about-container {
                    max-width: 800px;
                    margin: 70px;
                    padding: 20px;
                    
                    box-shadow: 2px 4px 6px rgba(0, 0, 0, 0.2);
                    border-radius: 10px;
                }

                h1 {
                    color: #3498db;
                }

                h2 {
                    color: #333;
                }

                p {
                    margin: 10px 0;
                }
            </style>
        </head>
        <body>
            <div class="about-container">
                <h1>Welcome to the Course Recommendation App!</h1>
                <p>This app uses natural language processing (NLP) techniques to recommend Udemy courses based on their titles.</p>
                <h2>How it works:</h2>
                <p>1. Enter a search term related to the course you're interested in.</p>
                <p>2. The app will use NLP to find courses with similar titles and recommend them to you.</p>
                <p>Feel free to explore and discover new courses!</p>
            </div>
        </body>
        </html>
        """,
        height=500,
    )
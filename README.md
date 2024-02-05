# Course Recommendation App

This Streamlit web application recommends Udemy courses based on the similarity of the entered search term. It uses spaCy for natural language processing and includes visualizations of the dataset.

## Getting Started

### Prerequisites

Make sure you have the required Python packages installed:

```bash
pip install streamlit pandas spacy matplotlib seaborn wordcloud streamlit-components streamlit-reveal-slides
python -m spacy download en_core_web_lg
```

# Installation
Clone the repository:
```bash
git clone https://github.com/your-username/course-recommendation-app.git
cd course-recommendation-app
```

# Run the Streamlit app:
```bash
streamlit run app.py
```
# Usage
### Home:
Overview of the dataset, visualizations, and summary statistics.
### Recommend:
Enter a search term to get course recommendations based on similarity.
### About:
Information about the application.


# Customization
Modify the dataset: Replace the `udemy_course_data.csv` file with your dataset.

Adjust styling: Modify the custom CSS in the `main()` function to change the appearance.

## Built with
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [spaCy](https://spacy.io/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [WordCloud](https://github.com/amueller/word_cloud)


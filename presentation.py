# presentation.py

import streamlit as st
import streamlit.components.v1 as components
import reveal_slides as rs


def presentation_page():
    detailed_content_with_animations = r"""
    # Udemy Courses Recommendation System and MLOps
    ---
    #### Udemy Courses Recommendation System

    - **Objective:** Enhancing the user experience on Udemy.
    - **Implementation:**
        - **NLP Approaches:**
            - Utilized cosine similarity for initial exploration.
            - Experimented with smaller versions of spaCy en_core_web models.
            - Found spaCy Large to provide superior performance.
            - Adopted spaCy Large model for robust course recommendations, leveraging word embeddings to enhance similarity assessments.

    ---

    ## MLOps for Optimization

    #### Introduction to MLOps

    - **Objective:** Improving the Udemy Courses Recommendation System.
    - **Agenda:** 
        - Overview of MLOps in the context of recommendation systems.
        - Key components and their roles.

    ---

    ### Deployment Frameworks

    - **Streamlit:** 
        - Interactive web-based deployment.
        - Provides a Python-centric approach for creating engaging interfaces.
        - Enables the easy integration of data visualization and recommendation algorithms.
       
    - **Docker:**
        - Containerization for portability.
        - Ensures a consistent deployment environment across different systems.
        - Facilitates seamless integration with other technologies in the MLOps pipeline.
       

    - **Cloud Platforms (e.g., Heroku, AWS):**
        - Scalable solutions for cloud deployment.
        - Supports efficient resource management, ensuring optimal system performance.
        - Enables elastic scalability to handle varying user loads.
        

    ---

    ### Monitoring framworks

    - **MLflow:**
        - Experiment tracking and model management.
        - Streamlines the machine learning lifecycle.
        - Enables reproducibility by tracking experiment parameters and results.
        

    - **Custom Logging and Alerting:**
        - Implementation for real-time monitoring.
        - Customized alerts for system performance.
        - Monitors key system metrics and user interactions.
        

    ---

    ### Challenges and Best Practices

    #### Challenges

    - **Dynamic Data and Model Updates:**
        - Adapting to changes in course data and models.
        - Implemented a dynamic update mechanism to seamlessly incorporate changes.
        - Utilized versioned models and data for compatibility.
    

    - **Real-time Recommendations:**
        - Ensuring timely and relevant course suggestions.
        - Implemented real-time recommendation logic to provide instant suggestions.
        - Optimized algorithms to handle large datasets efficiently.


    - **Scalability:**
        - Meeting demand as the user base grows.
        - Implemented scalable solutions for handling increased user traffic.
        - Utilized cloud platforms for elastic scalability.
    

    #### Best Practices

    - **Continuous Integration/Continuous Deployment (CI/CD):**
        - Seamless updates for enhanced functionality.
        - Implemented CI/CD pipelines to automate testing and deployment.
        - Ensured quick and reliable delivery of new features.
     

    - **Versioned Models and Data:**
        - Handling changes while maintaining compatibility.
        - Adopted versioning for models and data to manage changes effectively.
        - Ensured backward compatibility for a smooth user experience.


    - **Automated Testing and Validation:**
        - Ensuring the accuracy and effectiveness of recommendations.
        - Implemented automated testing for recommendation algorithms.
        - Validated recommendations against user interactions for continuous improvement.
      

    ---

    ### Conclusion
    - **Ongoing Improvements:**
        - Continuous refinement of the Recommendation System.
        - Prioritizing user feedback for feature enhancements.
        - Exploring opportunities for further optimization.
        

    - **Future Enhancements:**
        - Exploring opportunities for further optimization.
        - Investigating emerging technologies to enhance recommendation algorithms.
    """

    st.title("Udemy Courses Recommendation System and MLOps Presentation")
    st.markdown(rs.slides(detailed_content_with_animations), unsafe_allow_html=True)


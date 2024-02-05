# presentation.py

import streamlit as st
import reveal_slides as rs
import streamlit.components.v1 as components

# presentation.py

def presentation_page():
    detailed_content_with_animations = r"""
    # MLOps for Udemy Courses Recommendation System

    ## Introduction

    - **Objective:** Enhancing the Udemy Courses Recommendation System using MLOps.
    - **Agenda:** 
        - Overview of the Recommendation System.
        - Role of MLOps in improving performance.

    ---

    ## Deployment Frameworks

    - **Streamlit:** 
        - Interactive web-based deployment.
        - Easy integration with Python scripts.
        - User-friendly interface for recommendations.
        - ![Streamlit](./images/streamlit.gif)  # Update the path accordingly

    - **Docker:**
        - Containerization for portability.
        - Ensures consistent deployment across environments.
        - ![Docker](./images/docker.gif)  # Update the path accordingly

    - **Cloud Platforms (e.g., Heroku, AWS, Streamlit Cloud):**
        - Scalable solutions for cloud deployment.
        - Enables efficient resource management.
        - ![Cloud](./images/streamlit_cloud.gif)  # Update the path accordingly

    ---

    ## Monitoring Frameworks

    - **MLflow:**
        - Experiment tracking and model management.
        - Streamlines the machine learning lifecycle.
        - ![MLflow](./images/mlflow.gif)  # Update the path accordingly

    - **Custom Logging and Alerting:**
        - Implementation for real-time monitoring.
        - Customized alerts for system performance.
        - ![Logging](./images/logging.gif)  # Update the path accordingly

    ---

    ## Challenges and Best Practices

    ### Challenges

    - **Dynamic Data and Model Updates:**
        - Adapting to changes in course data and models.
        - ![Dynamic Updates](./images/dynamic_updates.gif)  # Update the path accordingly

    - **Real-time Recommendations:**
        - Ensuring timely and relevant course suggestions.
        - ![Real-time](./images/real_time.gif)  # Update the path accordingly

    - **Scalability:**
        - Meeting demand as the user base grows.
        - ![Scalability](./images/scalability.gif)  # Update the path accordingly

    ### Best Practices

    - **Continuous Integration/Continuous Deployment (CI/CD):**
        - Seamless updates for enhanced functionality.
        - ![CI/CD](./images/cicd.gif)  # Update the path accordingly

    - **Versioned Models and Data:**
        - Handling changes while maintaining compatibility.
        - ![Versioning](./images/versioning.gif)  # Update the path accordingly

    - **Automated Testing and Validation:**
        - Ensuring the accuracy and effectiveness of recommendations.
        - ![Testing](./images/testing.gif)  # Update the path accordingly

    ---

    ## Conclusion

    - **Recap of Key MLOps Considerations:**
        - Deployment and monitoring strategies.
        - Addressing challenges and implementing best practices.
        - ![Recap](./images/recap.gif)  # Update the path accordingly

    - **Ongoing Improvements:**
        - Continuous refinement of the Recommendation System.
        - ![Improvements](./images/improvements.gif)  # Update the path accordingly

    - **Future Enhancements:**
        - Exploring opportunities for further optimization.
        - ![Future](./images/future.gif)  # Update the path accordingly

    """

    st.title("MLOps Presentation")
    components.html(rs.slides(detailed_content_with_animations), width=900, height=900, key="reveal-slides")



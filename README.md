# Mongolian General Entrance Examination Results Analysis & Dashboard

## Project Overview

This project analyzes student performance data from the result of Mongolian General Entrance Examinations across multiple subjects and provinces. The objective is to consolidate various subject-specific exam datasets into a unified structure and develop interactive tools to uncover insights about student scores, regional disparities, percentile benchmarks, and exam participation trends.

The project follows a complete data science workflow, including data cleaning, exploratory data analysis (EDA), visualization, and predictive modeling.

## Data Source

The datasets used in this project were obtained from Kaggle:
**Mongolian General Entrance Exam (ЭЕШ) 2025**  (https://www.kaggle.com/datasets/gantugsgantulga/mongolian-general-university-entrance-exam-2025)

## Objectives

- Understand the distribution and relationship between First Score and Converted Score across all subjects.
- Analyze regional disparities in exam performance across Mongolian provinces.
- Identify percentile thresholds and the score requirements to reach key benchmarks such as the 90th, 75th, and 50th percentiles.
- Build predictive models to estimate a student’s percentile based on their score.
- Develop two interactive tools for real-time filtering and visualization of results.

## Interactive Platforms

This project offers two platforms with similar functionalities for exploring the examination results:

### Streamlit App

An interactive web application for:
- Visualizing trends and distributions across subjects and provinces
- Predicting percentiles using Machine Learning (Random Forest)
- Estimating percentile via ECDF (Empirical Cumulative Distribution Function)

[Open the Streamlit App](https://zzzillo-mongolia-general-entrance-e-streamlit1-dashboard-padsre.streamlit.app//)

### Google Looker Dashboard

A business intelligence dashboard that provides:
- Filterable visualizations of exam results by subject, region, and score range
- Percentile thresholds and subject-specific score summaries
- Interactive geographic maps of exam taker distributions

[View the Looker Dashboard](https://lookerstudio.google.com/reporting/51297d2d-2535-4117-9b0f-0931244e8104)

## Repository Structure

- **Notebook/**  
  This folder contains the data science and analysis components:
  - **dataset/**: Contains all raw datasets used in the project.
  - **Documentation.ipynb**: A Jupyter notebook that includes the full data science workflow, from data cleaning to analysis and visualization.

- **Streamlit/**  
  This folder contains the code for the interactive web application:
  - **1_Dashboard.py**: The main Streamlit app used for user interaction and deployment.
  - Other necessary files used by the app are also included in this folder.

- **requirements.txt**  
  Lists all the Python libraries needed to run the project.

- **README.md**  
  Explains the project overview, purpose, usage, and structure.

## Setup Instructions

Follow these steps to run the project locally:

   ```bash
# 1. Clone the repository
git clone https://github.com/zzzillo/Mongolia-University-Entrance-Examination-Results-Dashboard-and-Prediction.git

# 2. Navigate to the project directory
cd Mongolia-University-Entrance-Examination-Results-Dashboard-and-Prediction

# 3. (Optional) Create a virtual environment Version Python: 3.13.5
python3.13 -m venv venv 

#4 . Activate the virtual environment
  #On macOS/Linux:
  source venv/bin/activate
  #On Windows:
  venv\Scripts\activate

# 5. Install the required packages
pip install -r requirements.txt

# 6. Run the Streamlit application
streamlit run Streamlit/1_Dashboard.py





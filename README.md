# Mongolian University Entrance Examination Results Analysis & Dashboard

## Project Overview

This project analyzes student performance data from the Mongolian University Entrance Examinations across multiple subjects and provinces. The objective is to consolidate various subject-specific exam datasets into a unified structure and develop interactive tools to uncover insights about student scores, regional disparities, percentile benchmarks, and exam participation trends.

The project follows a complete data science workflow, including data cleaning, exploratory data analysis (EDA), visualization, and predictive modeling.

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

[Open the Streamlit App](https://zzzillo-mongolia-university-entrance-examina-1-dashboard-sjx8tr.streamlit.app/)

### Google Looker Dashboard

A business intelligence dashboard that provides:
- Filterable visualizations of exam results by subject, region, and score range
- Percentile thresholds and subject-specific score summaries
- Interactive geographic maps of exam taker distributions

[View the Looker Dashboard](https://lookerstudio.google.com/reporting/51297d2d-2535-4117-9b0f-0931244e8104)

## Repository Structure

├── Notebook/
│ ├── dataset/
│ │ └── [Contains all raw datasets used in the project]
│ ├── Documentation.ipynb # Contains the data science workflow and analysis
│
├── Streamlit/
│ ├── 1_Dashboard.py # Main Streamlit application
│ └── [Additional files for deployment and app logic]
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## Installation Guide

To run this project locally:

### 1. Clone the repository

```bash
git clone https://github.com/zzzillo/Mongolia-University-Entrance-Examination-Results-Dashboard-and-Prediction.git
cd Mongolia-University-Entrance-Examination-Results-Dashboard-and-Prediction
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
streamlit run Streamlit/1_Dashboard.py


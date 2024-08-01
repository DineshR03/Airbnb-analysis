# Airbnb Data Analysis

## Overview

This project involves analyzing Airbnb data from 2019, focusing on property listings such as descriptions, pricing, location, and reviews. The process includes data transformation, database integration, and interactive visualization.

## Process

1. **Data Extraction & Preprocessing**
   - Extracted and cleaned the 2019 Airbnb dataset.
   - Transformed data into structured DataFrames for analysis.

2. **Database Integration**
   - Used MySQL and SQLAlchemy for efficient data storage and management.

3. **Data Visualization**
   - Created an interactive dashboard with Streamlit.
   - Utilized Plotly for dynamic visualizations and insights.

## Features

- **Home**: View detailed hotel information by selecting a country, including price, room type, description, and ratings.
- **Discover**: Explore countries with geo-visualizations and price insights. Filter results by property type and room type.
- **Insight**: Access 'Top Insights' for general analysis or 'Filtered Insights' for tailored visualizations based on specific criteria.

## Skills & Tools

- **Skills**: Python, Data Preprocessing, Visualization, Exploratory Data Analysis (EDA), Streamlit, Power BI
- **Tools**:
  - Python 3.12.2
  - MySQL
  - Streamlit
  - Plotly
  - Power BI

## Packages & Libraries

```python
import json
import time
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from sqlalchemy import create_engine
import mysql.connector

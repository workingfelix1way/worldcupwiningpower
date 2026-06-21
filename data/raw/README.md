# World-cup-prediction-2026

## 📌 Project Overview

This project demonstrates a complete Data Analysis workflow using Python. The objective is to clean, transform, analyze, and visualize data to uncover meaningful insights and support data-driven decision-making.

The project includes data preprocessing, exploratory data analysis (EDA), visualization, feature engineering, and documentation following industry-standard practices.

## 🎯 Objectives

* Load and explore the dataset
* Handle missing values and inconsistencies
* Detect and analyze outliers
* Transform and encode data
* Perform Exploratory Data Analysis (EDA)
* Generate meaningful visualizations
* Extract actionable insights
* Document the entire analysis process
* Maintain project version control using Git and GitHub

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

## 📂 Project Structure

│
├── data/
│   ├── test (2).csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── scripts/
│   └── analysis.py
│
├── visuals/
│   ├── fifa_points_distribution.png
│   ├── market_vs_fifa.png
│   └── correlation_heatmap.png
│
├── README.md
├── requirements.txt
└── .gitignore

## 📊 Data Analysis Process

### 1. Data Collection and Loading

* Imported dataset using Pandas.
* Verified dataset structure and dimensions.

### 2. Data Exploration

* Examined data types and column information.
* Generated summary statistics.
* Identified missing values and potential data quality issues.

### 3. Data Cleaning

* Handled missing numerical values using median imputation.
* Handled missing categorical values using mode imputation.
* Checked for duplicate records.

### 4. Outlier Detection

* Used the Interquartile Range (IQR) method.
* Visualized outliers using boxplots.

### 5. Data Transformation

* Applied One-Hot Encoding for categorical variables.
* Created new features to improve analysis.
* Prepared data for further analytical tasks.

### 6. Exploratory Data Analysis (EDA)

* Distribution analysis using histograms.
* Relationship analysis using scatter plots.
* Correlation analysis using heatmaps.
* Statistical summary generation.

### 7. Visualization

* FIFA Points Distribution
* Market Value vs FIFA Points
* Correlation Heatmap

## 📈 Key Findings

* Teams with higher market values generally achieve higher FIFA rankings.
* Goal difference is an important indicator of team performance.
* Player ratings and recent form scores strongly influence FIFA points.
* Several variables show strong positive correlations.
  
## 🚀 How to Run the Project

### Run Analysis

python analysis.py

or open the Jupyter Notebook:
jupyter notebook

## 📋 Requirements

pandas
numpy
matplotlib
seaborn
jupyter

## 📷 Sample Visualizations

* Distribution of FIFA Points
* Market Value vs FIFA Points Scatter Plot
* Correlation Heatmap

## 👨‍💻 Author

Bibas Basnet

## 📄 License

This project is intended for educational and portfolio purposes.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df = pd.read_csv(r'c:\Users\User\OneDrive\Desktop\World_Cup_Test_Match.csv')

#display first 5 rows
print(df.head())

#shape of dataset
print(df.shape)

#column names
print(df.columns)

#data types
print(df.dtypes)

#information
print(df.info())

#summary
print(df.describe())

#check missing values
print(df.isnull().sum())
#select numerical cols
numerical_cols = df.select_dtypes(include=np.number).columns

#fill missing values with median
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())
#select categorical cols
categorical_cols = df.select_dtypes(include='object').columns

#fill missing categorical values using mode
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])  
# Detect outliers

for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"{col} = {len(outliers)} outliers")
#visualize Outliers using Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(data=df[numerical_cols])
plt.xticks(rotation=90)
plt.title("Boxplot for Numerical Columns")
plt.show()
# One-hot encoding
df_encoded = pd.get_dummies(df, columns=['confederation'], drop_first=True)
print(df_encoded.head())
#create new features
df_encoded['goal_difference'] = df_encoded['goals_scored_avg'] - df_encoded['goals_conceded_avg']
#Histogram of FIFA points
plt.figure(figsize=(8,5))
plt.hist(df['fifa_points'], bins=20)
plt.xlabel('FIFA Points')
plt.ylabel('Frequrency')
plt.title("Distribution of FIFA Points")
plt.show()
#Density plot
plt.figure(figsize=(8,5))
sns.kdeplot(df['fifa_points'], fill=True)
plt.title("Density plot of FIFA Points")
plt.show()
#scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(x='market_value_million_eur', y='fifa_points', data=df)
plt.title("Market Value vs FIFA Points")
plt.xlabel("Market Value")
plt.ylabel("FIFA Points")
plt.show()
#pair plot
sns.pairplot(df[numerical_cols])
plt.show()
#correlation Matrix
correlation_matrix = df[numerical_cols].corr()
print(correlation_matrix)
#Heatmap Visualization
plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
#saved cleaned dataset
df_encoded.to_csv(r'c:\Users\User\OneDrive\Desktop\World_Cup_Test_Match_Cleaned.csv', index=False)
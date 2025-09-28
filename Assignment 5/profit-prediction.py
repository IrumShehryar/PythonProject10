"""
Consider the dataset 50_Startups.csv which contains data for companies' profit etc.
0) Read the dataset into pandas dataframe paying attention to file delimeter.
1) Identify the variables inside the dataset
2) Investigate the correlation between the variables
3) Choose appropriate variables to predict company profit. Justify your choice.
4) Plot explanatory variables against profit in order to confirm (close to) linear dependence
5) Form training and testing data (80/20 split)
6) Train linear regression model with training data
7) Compute RMSE and R2 values for training and testing data separately
Include your own findings and explanations in code comments or inside triple quotes

--------------------------------------------------------------------------------------------------------------------
FINDINGS:

Train R² = 0.944, Test R² = 0.968; Train RMSE =9,359, Test RMSE =7,074 (same units as Profit).

EXPLANATION:

Using R&D Spend and Marketing Spend to predict Profit gives a strong linear model.
Test performance is excellent: R2 =0.968 and RMSE =7,074 (in profit units). That means the model
explains about 97% of the variance on unseen data, with an average prediction error of about 7k.
Train performance is also strong: R2 = 0.944, RMSE = 9,359.

CONCLUSION: Profit rises mostly with R&D and Marketing spend.

----------------------------------------------------------------------------------------------------------------------
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,root_mean_squared_error
from sklearn.model_selection import train_test_split

# 0 Reading the dataset and reading values separated by delimiter(which is comma in this file)

df = pd.read_csv("../AI with Python/50_Startups.csv",delimiter=',')

#1 Identifying the variables

print(f'{df}\n{df.dtypes}\n')

#2 Using only numeric daya types for generating heatmap as the file contains State(a non numeric value)
# Generating heatmap to study the correlation between variables and the target
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, fmt=".2f")
plt.show()

# 3 choosing R&D spend (0.97) and marketing Spend(0.75) as they are strongly correlated to profit (closer to 1)

#4 Plotting explanatory variables against profit in order to confirm (close to) linear dependence
plt.subplot(1,2,1)
plt.scatter(df['R&D Spend'],df['Profit'])
plt.xlabel('R&D Spend')
plt.ylabel('Profit')

plt.subplot(1,2,2)
plt.scatter(df['Marketing Spend'],df['Profit'])
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')
plt.show()

#5 Forming training and testing data (80/20 split)
x = df[['R&D Spend','Marketing Spend']]
y = df['Profit']

x_train, x_test, y_train,y_test = train_test_split(x,y, random_state=5 , test_size=0.2)

#6 Training linear regression model with training data

lm = LinearRegression()
lm.fit(x_train,y_train)
y_train_predict = lm.predict(x_train)
y_test_predict = lm.predict(x_test)

#7 Computing RMSE and R2 values for training and testing data separately
rmse_train = root_mean_squared_error(y_train, y_train_predict)
rmse_test  = root_mean_squared_error(y_test,  y_test_predict)
r2_train   = r2_score(y_train, y_train_predict)
r2_test   = r2_score(y_test,  y_test_predict)
print(f' RMSE Train = {rmse_train}\n RMSE Test = {rmse_test}\n R2 Train = {r2_train}\n R2 Test = {r2_test}')



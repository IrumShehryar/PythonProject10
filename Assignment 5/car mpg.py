"""
Consider car performance data from the file Auto.csv.
1) Read the data into pandas dataframe
2) Setup multiple regression X and y to predict 'mpg' of cars using all the variables except 'mpg', 'name' and
'origin'
3) Split data into training and testing sets (80/20 split)
4) Implement both ridge regression and LASSO regression using several values for alpha
5) Search optimal value for alpha (in terms of R2 score) by fitting the models with training data and
computing the score using testing data
6) Plot the R2 scores for both regressors as functions of alpha
7) Identify, as accurately as you can, the value for alpha which gives the best score
Include your own findings and explanations in code comments or inside triple quotes

-----------------------------------------------------------------------------------------
FINDINGS:

Ridge regression worked best at alpha = 91.14 with R2 = 0.7717.
Lasso regression worked best at alpha = 0.32 with R2 = 0.7749.
Lasso gave a slightly higher score than Ridge.

EXPLANATION:

Ridge shrinks all coefficients but keeps them non-zero, while Lasso can make some coefficients
exactly zero.In my plots, Ridge improved as alpha increased and then flattened around
alpha = 90.Lasso peaked around alpha = 0.32 and then dropped as alpha got bigger.

CONCLUSION:

The best model here is Lasso with alpha = 0.32 (R2 = 0.7749).
Ridge is very close (R2 = 0.7717 at alpha = 91).
Lasso is slightly better, while Ridge is more stable across a wider range of alpha values.
----------------------------------------------------------------------------------------------
"""

import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('../AI with Python/Auto.csv')
#print(df)
X = df[['cylinders','displacement','horsepower','weight','year','acceleration']]
y = df['mpg']

X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 5, test_size = 0.2)
alphas = np.linspace(0.001,120,800)

"""
alphas = np.linspace(0.001, 20, 80)
alphas = np.linspace(0.001, 50, 100)
alphas = np.linspace(0.001, 100, 120)

-------------------------------------------------------------------------------------------
“I tested several alpha ranges (0.001–20, 0.001–50, 0.001–100, 0.001–120). 
Lasso consistently peaked around alpha = 0.3, while Ridge peaked much later near alpha =90.
Using a dense grid (0.001–120 with 800 points) confirmed that the best model is Lasso with
alpha = 0.32, giving the highest test R² = 0.775.”
--------------------------------------------------------------------------------------------

#alphas = [0.1,0.2,0.3,0.4,0.5,1,2,3,4 ,5,6,7,8]
#alphas = np.logspace(-3, 2, 60)
#print('alphas=',alphas)
"""

r2ValuesRidge = []
r2ValuesLasso = []

for alp in alphas:
    # implementing Ridge regression
    rr = linear_model.Ridge(alpha = alp)
    rr.fit(X_train,y_train)
    r2_testRidge = r2_score(y_test,rr.predict(X_test))
    r2ValuesRidge.append(r2_testRidge)

    # implementing Lasso regression
    lr = linear_model.Lasso(alpha = alp)
    lr.fit(X_train, y_train)
    r2_testLasso = r2_score(y_test, lr.predict(X_test))
    r2ValuesLasso.append(r2_testLasso)

# calculating best alpha  and best R2 for Ridge
best_r2Ridge = max(r2ValuesRidge)
idxRidge = r2ValuesRidge.index(best_r2Ridge)
best_alphaRidge = alphas[idxRidge]

# calculating best alpha  and best R2 for Lasso
best_r2Lasso = max(r2ValuesLasso)
idxLasso = r2ValuesLasso.index(best_r2Lasso)
best_alphaLasso = alphas[idxLasso]

#printing best alpha and r2 for ridge and lasso
print('--------------------------------')
print('Values      Ridge        Lasso')
print('--------------------------------')
print(f'Best r2:{best_r2Ridge:10.4f}{best_r2Lasso:12.4f}')
print(f'Best alpha:{best_alphaRidge:8.4f}{best_alphaLasso:11.4f}')

#plotting alpha vs r2 for Ridge
plt.subplot(1,2,1)
plt.plot(alphas,r2ValuesRidge)
plt.title('Ridge regression')
plt.xlabel('alpha')
plt.ylabel('r2')
#plt.show()

#plotting alpha vs r2 for Lasso
plt.subplot(1,2,2)
plt.plot(alphas,r2ValuesLasso)
plt.title('Lasso regression')
plt.xlabel('alpha')
plt.ylabel('r2')
plt.show()



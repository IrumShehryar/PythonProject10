"""
Consider the data from the file weight-height.csv.
1) Inspect the dependence between height and weight using a scatter plot. You may use either of the variables as independent variable.
2) Choose appropriate model for the dependence
3) Perform regression on the data using your model of choice
4) Plot the results
5) Compute RMSE and R2 value
6) Assess the quality of the regression (visually and using numbers) in your own words.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from  sklearn.metrics import r2_score,root_mean_squared_error
from sklearn.linear_model import LinearRegression
df = pd.read_csv('../AI with Python/weight-height.csv')
x = df['Height'].to_numpy().reshape(-1,1)
y = df['Weight'].to_numpy()
plt.scatter(x,y,s=6, alpha=0.3,)
#plt.show()

# I am choosing linear regression as scatter shows a simple upward trend
lr = LinearRegression()
lr.fit(x,y)

xval = np.linspace(50,80,200).reshape(-1,1)
yval = lr.predict(xval)

plt.plot(xval,yval,color ='red')
plt.title('Dependence between height and weight')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
yhat = lr.predict(x)
print(f'RMSE ={root_mean_squared_error(y,yhat)}')
print(f'R Square ={r2_score(y,yhat)}')

"""
Ans: Visually: The scatter shows a clear upward trend. The fitted line goes through the middle of the points. Points are 
fairly close to the line, with some spread (people with the same height can have different weights).

Numbers: My model gives R2 = 0.856, so about 86% of the variation in weight is explained by height. The RMSE = 12 
(in weight units), meaning the typical prediction error is around 12 units.(i.e. on average the error for predicted values
fluctuates round 12 units) 

Conclusion: The linear model fits well. It shows the relationship between (taller tends to be heavier) and errors are 
reasonable.(i.e. large R2 and smaller RMSE)
 
"""
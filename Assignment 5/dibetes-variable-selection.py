"""
Investigate the model for predicting Diabetes disease progression by adding more explanatory variables to it 
in addition to bmi and s5. 
a) Which variable would you add next? Why? 
b) How does adding it affect the model's performance? Compute metrics and compare to having just bmi 
and s5. 
d) Does it help if you add even more variables? 
Include your own findings and explanations in code comments or inside triple quotes.
Each step above is worth a point. You need 2 points in order to complete this problem. 

------------------------------------------------------------------------------------------------------------------------------------
FINDINGS:
(a) I am choosing 'bp' as the Next variable as it has the strongest correlation to the target after bmi and s5.
(b) Adding 'bp' gives small but consistent improvements in test R2 and RMSE. The R2 increases slightly and
RMSE decreases slightly.

EXPLANATION:
(d) Using bmi and s5 as the baseline, adding bp slightly improves performance. Test metrics  R2(bmi+s5) move from 0.482 to 0.491
and RMSE(bmi+s5) decreases from 57.176 to 56.626 (bmi+s5+bp).
Adding s4 does not help: the test metrics become R2 = 0.480 and RMSE = 57.260 (bmi+s5+bp+s4), which is worse than with bp.

CONCLUSION:
Therefore, based on these results, adding more variables is not benefiting us; three variables (bmi, s5, bp) are sufficient here.
-------------------------------------------------------------------------------------------------------------------------------------

"""
import pandas as pd
import  numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,root_mean_squared_error
from sklearn.model_selection import train_test_split


data = load_diabetes(as_frame= True)
#print(data.keys())
df = data['frame']
#print(df)

sns.heatmap(data=df.corr().round(2),annot= True)
plt.show()

plt.subplot(1,2,1)
plt.scatter(df['bmi'],df['target'])
plt.xlabel('BMI')
plt.ylabel('Target')

plt.subplot(1,2,2)
plt.scatter(df['s5'],df['target'])
plt.xlabel('s5')
plt.ylabel('Target')
plt.show()

x= pd.DataFrame(df[['bmi','s5']],columns = ['bmi','s5'])
y = df['target']

x_train, x_test, y_train,y_test = train_test_split(x,y, random_state=5 , test_size=0.2)
lm = LinearRegression()
lm.fit(x_train,y_train)
y_train_predict = lm.predict(x_train)
y_test_predict = lm.predict(x_test)

rmse_train_base = root_mean_squared_error(y_train, y_train_predict)
rmse_test_base  = root_mean_squared_error(y_test,  y_test_predict)
r2_train_base   = r2_score(y_train, y_train_predict)
r2_test_base    = r2_score(y_test,  y_test_predict)


# Next adding bp and calculating the metrices

x_bp = df[['bmi', 's5', 'bp']].copy()
x_trainBp, x_testBp, y_trainBp, y_testBp = train_test_split(x_bp, y, test_size=0.2, random_state=5)

lmBp = LinearRegression()
lmBp.fit(x_trainBp, y_trainBp)

y_trainBp_predict = lmBp.predict(x_trainBp)
y_testBp_predict  = lmBp.predict(x_testBp)

rmse_train_bp = root_mean_squared_error(y_trainBp, y_trainBp_predict)
rmse_test_bp  = root_mean_squared_error(y_testBp,  y_testBp_predict)
r2_train_bp   = r2_score(y_trainBp, y_trainBp_predict)
r2_test_bp    = r2_score(y_testBp,  y_testBp_predict)


# Next adding s4(the next strong correlation with target after bmi,s5 and bp) and calculating the metrices to see if r2 and rmse shows improvements

x_bp_s4 = df[['bmi', 's5', 'bp', 's4']].copy()
x_trainBpS4, x_testBpS4, y_trainBpS4, y_testBpS4 = train_test_split(x_bp_s4, y, test_size=0.2, random_state=5)

lmBpS4 = LinearRegression()
lmBpS4.fit(x_trainBpS4, y_trainBpS4)

y_trainBpS4_predict = lmBpS4.predict(x_trainBpS4)
y_testBpS4_predict  = lmBpS4.predict(x_testBpS4)

rmse_train_bpS4 = root_mean_squared_error(y_trainBpS4, y_trainBpS4_predict)
rmse_test_bpS4  = root_mean_squared_error(y_testBpS4,  y_testBpS4_predict)
r2_train_bpS4   = r2_score(y_trainBpS4, y_trainBpS4_predict)
r2_test_bpS4    = r2_score(y_testBpS4,  y_testBpS4_predict)

#  Train RMSE,R2 comparison
print("\nTRAIN metrics")
print("----------------------------------------")
print("Feature      base(bmi+s5) +bp    +bp+s4")
print("----------------------------------------")
print(f"R2           {r2_train_base:8.3f} {r2_train_bp:8.3f} {r2_train_bpS4:8.3f}")
print(f"RMSE         {rmse_train_base:8.3f} {rmse_train_bp:8.3f} {rmse_train_bpS4:8.3f}")


# TEST RMSE R2 comparison
print("\nTEST metrics")
print("----------------------------------------")
print("Feature      base(bmi+s5)  +bp   +bp+s4")
print("----------------------------------------")
print(f"R2           {r2_test_base:8.3f} {r2_test_bp:8.3f} {r2_test_bpS4:8.3f}")
print(f"RMSE         {rmse_test_base:8.3f} {rmse_test_bp:8.3f} {rmse_test_bpS4:8.3f}")


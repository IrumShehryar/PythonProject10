import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.odr import polynomial
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
data_pd = pd.read_csv("../AI with Python/quadreg_data.csv", skiprows= 0, names =["x","y"])

xpd = np.array(data_pd[["x"]])

ypd = np.array(data_pd[["y"]])

xpd = xpd.reshape(-1,1)

ypd = ypd.reshape(-1,1)
print(xpd)

poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(xpd)
print("X_poly",X_poly)
pol_reg = LinearRegression()
print("poly_reg",pol_reg)
pol_reg.fit(X_poly,ypd)
plt.scatter(xpd,ypd,color = 'red')
xval = np.linspace(-1,1,50).reshape(-1,1)
yhat = pol.reg_predict(poly_reg.fit_transform(xval))

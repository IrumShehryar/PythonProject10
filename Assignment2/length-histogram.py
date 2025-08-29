"""

3- Read from CSV-file weight-height.csv to numpy-table information about the lengths and weights (in inches and pounds) of a group of students.
Collect the lengths for the variable length and the weights for the variable weight by cutting the table.Convert lengths from inches to centimeters
and weights from pounds to kilograms.Calculate the means of the lengths and weights.Finally draw a histogram of the lengths.

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

INCH_CM = 2.54
POUND_KG = 0.453592

df = pd.read_csv('../AI with Python/weight-height.csv')
data = df.to_numpy()
print(df,data)
length = data[:,1]
weight = data[:,2]
#print("length:",length,"weight",weight)
inches_to_cm = length * INCH_CM
pounds_to_kgs = weight* POUND_KG
print("Length in inches\n",length,"\nLength in cm\n",inches_to_cm,"\nWeight in pounds\n",weight,"\nWeight in kgs\n",pounds_to_kgs)
mean_length = np.mean(inches_to_cm)
mean_weight = np.mean(pounds_to_kgs)
print(" Mean length = ", mean_length, "Mean Weight = ",mean_weight)
plt.hist(length,bins=30, color="red", edgecolor="black")
plt.xlabel("Heights (inches)")
plt.ylabel("Number of students")
plt.title("Heights Of Students")
plt.show()
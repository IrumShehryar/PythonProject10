"""
0) Write a for loop which repeats the steps 1)-3) below for values of n  ranging as 500, 1000, 2000, 5000, 10000, 15000,
20000, 50000, 100000
1) Use numpy to simulate throwing of two dice n times. Compute the sum of the dice.
2) Use numpy’s histogram() function to compute the frequencies as h,h2 = np.histogram(s,range(2,14)) where s contains the sum.
3) Use matplotlib's bar function to plot the histogram as plt.bar(h2[:-1],h/n) and show the value of n in the title.
4) What do you observe? You may need to run the loop a few times to see it.
5) How is this related to "regression to the mean"?
"""
import numpy as np
import matplotlib.pyplot as plt

for n in [500, 1000, 2000, 5000, 10000, 15000,20000, 50000, 100000]:
    dice1 = np.random.randint(1, 7, size =n)
    dice2 = np.random.randint(1,7,size=n)
    s = dice1 + dice2
    h,h2 = np.histogram(s,range(2,14))
    plt.figure()
    plt.bar(h2[:-1],h/n)
    plt.title(f'n={n}')
    plt.xlabel('Sum of dice')
    plt.ylabel('Frequencies')
    plt.show()

"""
Ans to Q5 and 6

4) What I observe:

Each time I ran the program, the bar graph was different from the actual pyramid in the beginning (when sample size was 
small, n = 500, 1000, 2000), but it shows consistent output when n becomes large (like 100,000). In the end it looks exactly
as it’s supposed to be(a true pyramid). If I run it a few times, small-n bars change a lot, but big-n bars hardly change.

5) How is this related to “regression to the mean”?

Regression to the mean means going back to or converging to mean values. The randomly generated values show fluctuation
from the actual probability with small sample size (like 500, 1000), but they move toward the mean or actual predicted value
as the sample size increases.

This is due to the Law of Large Numbers : when we repeat a random experiment many times, the observed proportions get closer to the true 
probabilities,because of the Law of Large Numbers, the early fluctuations regress toward the mean, so the bar chart 
settles into the true pyramid as n grows.

"""



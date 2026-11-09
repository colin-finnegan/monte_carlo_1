"""

Sample Monte Carlo simulation to predict commsision expenses
Author: Colin Finnegan
Date: 11/9/2026

"""

import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

avg = 1
std_dev = .1
num_reps = 500
num_simulations = 1000

#use numpy to generate list of % that replicate the historical normal distribution, rounded to 2 decimal places
pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)
sales_taget_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]
sales_target = np.random.choice(sales_taget_values, num_reps, p=sales_target_prob)

#pandas dataframe
df = pd.DataFrame(index=range(num_reps), data={'Pct_to_Target': pct_to_target, 'Sales_Target': sales_target})
df['Sales'] = df['Pct_to_Target'] * df['Sales_Target']

def calc_commission_rate(x):
    # Return the commission rate based on the table:
    # 0-90% = 2%
    # 91-99% = 3%
    # >= 100% = 4%
    
    if x <= .90:
        return .02
    if x <= .99:
        return .03
    else:
        return .04

df['Commission_Rate'] = df['Pct_to_Target'].apply(calc_commission_rate)
df['Commission_Amount'] = df['Commission_Rate'] * df['Sales']

print(df.head(5))
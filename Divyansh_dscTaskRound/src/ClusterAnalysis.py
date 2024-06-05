
#2. Implement cluster analysis and understand the characteristics of new coders in each cluster. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
print(f"Numerical columns: {numerical_cols}")

corr = data[numerical_cols].corr()
print("\nCorrelation matrix:")
print(corr)

corr = corr.fillna(0)

short_names = {
    '7. About how many hours do you spend learning each week?': 'Hours Learning',
    '8. About how many months have you been programming?': 'Months Programming',
    '9. Aside from university tuition, about how much money have you spent on learning to code so far (in US Dollars)?': 'Money Spent Learning',
    '23. How old are you?': 'Age',
    '36. How many children do you have? By children, we mean any biological, step, or adopted children.': 'Children',
    '39. How much debt does your household have? [Medical Loans]': 'Medical Debt',
    '39. How much debt does your household have? [Other]': 'Other Debt',
    '41. Before you got your last job, how many months did you spend looking for a job?': 'Months Job Hunting',
    '42. If you are working, thinking about the next 12 months, how likely do you think it is that you will lose your job or be laid off?': 'Job Loss Likelihood',
    '43. If you are working, how easy would it be for you to find a job with another employer with approximately the same income and fringe benefits you now have?': 'Job Finding Ease'
}
corr.rename(columns=short_names, index=short_names, inplace=True)

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


num_numerical_cols = len(numerical_cols)
print(f"Number of numerical columns: {num_numerical_cols}")
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 4, i + 1)
    data[col].hist(bins=20)
    plt.title(col)
    plt.tight_layout()
plt.show()








import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('Covid Data.csv')

# Data Cleaning
data['DATE_DIED'] = pd.to_datetime(data['DATE_DIED'], errors='coerce')
data['Is_Dead'] = data['DATE_DIED'].notna().astype(int)

# Sample data for visualization
sampled_data = data[['AGE', 'SEX', 'DIABETES', 'HIPERTENSION', 'OBESITY', 'Is_Dead']].sample(500)

# Plot
sns.pairplot(sampled_data, hue='Is_Dead')
plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(context='notebook', style='darkgrid', palette='deep')  # Set the theme

# Load the 'tips' dataset
tips_df = sns.load_dataset('tips')

# Create the line plot
sns.lineplot(x='size', y='total_bill', data=tips_df, hue='sex', palette='hot', dashes=False, markers=['o', '<'], legend='brief')

# Set plot labels and title
plt.xlabel('Size')
plt.ylabel('Total Bill')
plt.title('Line Plot')

# Show the plot
plt.show()

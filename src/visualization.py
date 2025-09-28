import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['Temperature_Anomaly'], label='Temperature Anomaly (°C)', color='red')
    plt.plot(df['Year'], df['CO2_Emissions'], label='CO2 Emissions (Mt)', color='green')
    plt.plot(df['Year'], df['Sea_Level'], label='Sea Level (mm)', color='blue')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.title('Global Climate Change Trends')
    plt.legend()
    plt.grid(True)
    plt.show()

def correlation_heatmap(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation between Climate Variables')
    plt.show()

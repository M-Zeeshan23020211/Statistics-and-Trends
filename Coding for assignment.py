import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load and preprocess data
data_path = 'co2 concentration.csv'
co2_data = pd.read_csv(data_path)
co2_data['date'] = pd.to_datetime(co2_data[['year', 'month', 'day']])
co2_data['month_name'] = co2_data['date'].dt.month_name()

# Define functions for each plot and statistics

def plot_time_series(data):
    """Plots the CO₂ Levels Over Time for Cycle and Trend."""
    plt.figure(figsize=(14, 6))
    plt.plot(data['date'], data['cycle'], label='Cycle', alpha=0.7)
    plt.plot(data['date'], data['trend'], label='Trend', color='orange', alpha=0.7)
    plt.title("CO₂ Levels Over Time (Cycle & Trend)", fontweight='bold')
    plt.xlabel("Date", fontweight='bold')
    plt.ylabel("CO₂ Concentration (ppm)", fontweight='bold')
    plt.legend(fontsize=10, loc='upper left', frameon=True, title="Legend", title_fontsize='12')
    plt.show()

def plot_monthly_bar_chart(data):
    """Plots the monthly average CO₂ levels."""
    monthly_avg_co2 = data.groupby('month_name')[['cycle', 'trend']].mean().reindex([
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    monthly_avg_co2.plot(kind='bar', figsize=(14, 6))
    plt.title("Average CO₂ Levels by Month", fontweight='bold')
    plt.xlabel("Month", fontweight='bold')
    plt.ylabel("CO₂ Concentration (ppm)", fontweight='bold')
    plt.legend(['Cycle', 'Trend'], fontsize=10, loc='upper left', frameon=True, title="Legend", title_fontsize='12')
    plt.show()

def plot_boxplot(data):
    """Plots a box plot for the distribution of CO₂ Cycle and Trend."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[['cycle', 'trend']])
    plt.title("Distribution of CO₂ Cycle and Trend", fontweight='bold')
    plt.ylabel("CO₂ Concentration (ppm)", fontweight='bold')
    plt.show()

def generate_statistics(data):
    """Generates descriptive statistics, correlation, skewness, and kurtosis."""
    # Descriptive statistics
    descriptive_stats = data[['cycle', 'trend']].describe()
    
    # Correlation matrix
    correlation = data[['cycle', 'trend']].corr()
    
    # Skewness and Kurtosis
    skewness = data[['cycle', 'trend']].apply(skew)
    kurtosis_vals = data[['cycle', 'trend']].apply(kurtosis)
    
    print("Descriptive Statistics:\n", descriptive_stats)
    print("\nCorrelation Matrix:\n", correlation)
    print("\nSkewness:\n", skewness)
    print("\nKurtosis:\n", kurtosis_vals)

# Call each function
plot_time_series(co2_data)
plot_monthly_bar_chart(co2_data)
plot_boxplot(co2_data)
generate_statistics(co2_data)
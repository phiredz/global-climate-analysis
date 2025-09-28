# Global Climate Change Analysis

## Overview
This project analyzes global climate change trends over the years using Python. It focuses on three key indicators:

- **Global Temperature Anomaly (°C)**
- **CO₂ Emissions (Megatonnes)**
- **Sea Level Rise (mm)**

The analysis leverages **Pandas** for data manipulation and **Matplotlib/Seaborn** for visualization, providing insights into climate patterns and correlations among these variables.

---

## Project Structure

```

global_climate_analysis/
│
├── data/
│   ├── co2_emissions.csv        # CO2 emission data per country/year
│   ├── global_temperatures.csv  # Temperature anomaly data
│   └── sea_levels.csv           # Sea level rise data
│
├── notebooks/
│   └── climate_analysis.ipynb   # Main exploratory analysis notebook
│
├── src/
│   ├── data_processing.py       # Data cleaning and merging functions
│   ├── visualization.py         # Functions to plot graphs
│   └── analysis.py              # Data summarization and analysis
│
├── requirements.txt             # Required Python packages
└── README.md                    # Project overview

````

---

## Features
- Load and clean datasets using Pandas.
- Merge temperature, CO₂ emissions, and sea level data by year.
- Summarize the data and check for missing values.
- Visualize trends over time:
  - Line plots for temperature, CO₂ emissions, and sea level rise.
  - Correlation heatmap between climate variables.
  
---

## Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd global_climate_analysis
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the notebook**
   Open `notebooks/climate_analysis.ipynb` in Jupyter Notebook or Jupyter Lab to explore the analysis.

---

## Usage

* Update the CSV files in the `data/` folder with the latest datasets if needed.
* Modify visualization functions in `src/visualization.py` to customize plots.
* Extend analysis in `src/analysis.py` for deeper insights, e.g., forecasting future trends.

---

## Sample Output

* **Trend Plot:** Shows the historical progression of temperature, CO₂ emissions, and sea level rise.
* **Correlation Heatmap:** Highlights the relationships between the climate variables.

---

## Technologies Used

* Python 3.x
* Pandas
* Matplotlib
* Seaborn
* NumPy

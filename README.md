# Demand Forecasting for a Retail Store

This project develops a time series forecasting model to predict the demand for products in a retail store. The model uses historical sales data, considering seasonality and trends, to forecast future demand.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Features

- Loads and preprocesses sales data.
- Removes malformed rows and renames columns for easier reference.
- Converts 'Month' column to datetime format and sets it as the index.
- Decomposes the time series to identify trend, seasonal, and residual components.
- Applies Holt-Winters Exponential Smoothing for demand forecasting.
- Visualizes historical sales and forecasts.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/demand-forecasting.git
    cd demand-forecasting
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the dataset file (`SAMPLE.csv`) is in the root directory of the project.

## Usage

1. Run the script:

    ```bash
    python app.py
    ```

2. The script will preprocess the data, apply the Holt-Winters Exponential Smoothing algorithm, and visualize the historical sales along with the forecast.

## Dataset

The script expects a CSV file named `SAMPLE.csv` with the following columns:

- `Month`: The month of the sales data (in a format that can be converted to datetime).
- `Sales`: The sales figures.

Ensure that the 'Month' column is in a format that can be converted to datetime and that the 'Sales' column is numeric.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Statsmodels

## Time Series Decomposition Plot

![Screenshot 2024-06-21 231729](https://github.com/swar41/CodeClauseInternship_Demand-Forecasting-for-a-Retail-Store/assets/141357728/0e433591-4e4d-4583-a0f0-5bd1b3158216)


## Forecast Plot

![Screenshot 2024-06-21 231738](https://github.com/swar41/CodeClauseInternship_Demand-Forecasting-for-a-Retail-Store/assets/141357728/0fc68d8d-ba82-43b8-9ae6-343070f655c3)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request


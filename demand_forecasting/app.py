import pandas as pd

# Load the data
file_path = 'SAMPLE.csv'
data = pd.read_csv(file_path)

# Remove malformed rows
data = data.drop([105, 106])

# Rename the columns for easier reference
data.columns = ['Month', 'Sales']

# Convert 'Month' to datetime format and set as index
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)

# Remove leading/trailing whitespace in 'Sales' column and convert to numeric
data['Sales'] = pd.to_numeric(data['Sales'])

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Decompose the time series
decomposition = seasonal_decompose(data['Sales'], model='multiplicative')
decomposition.plot()
plt.show()

# Fit the model
model = ExponentialSmoothing(data['Sales'], trend='add', seasonal='mul', seasonal_periods=24)
fit = model.fit()

# Forecast
forecast = fit.forecast(36)
plt.plot(data['Sales'], label='Historical Sales')
plt.plot(forecast, label='Forecast', linestyle='--')
plt.legend()
plt.show()


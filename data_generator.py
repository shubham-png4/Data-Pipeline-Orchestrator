import pandas as pd
import datetime

# Simulate data
data = {'id': [1, 2], 'name': ['Sensor_A', 'Sensor_B'], 'value': [23.5, 45.2]}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)
print("Data generated and saved to data.csv")
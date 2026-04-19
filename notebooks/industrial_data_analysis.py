# ==========================================
# Industrial Sensor Data Analysis
# Predictive Maintenance Prototype
# Author: Rick Rios
# ==========================================

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt

print("Libraries loaded successfully")

# 2. Load dataset
df = pd.read_csv("../data/sample_sensor_data.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\nDataset preview:")
print(df.head())

# 3. Plot temperature
plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["temperature"])
plt.title("Temperature Trend")
plt.xlabel("Time")
plt.ylabel("°C")
plt.grid()
plt.show()

# 4. Plot vibration
plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["vibration"])
plt.title("Vibration Trend")
plt.xlabel("Time")
plt.ylabel("mm/s")
plt.grid()
plt.show()

# 5. Detect anomalies
df["anomaly"] = (df["temperature"] > 80) | (df["vibration"] > 12)

print("\nAnomalies detected:")
print(df[df["anomaly"]])

print(f"\nTotal anomalies: {df['anomaly'].sum()}")

print("\nEngineering Insight:")
print("Possible overheating or bearing wear detected.")

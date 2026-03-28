import pandas as pd

# Load the datasets
results = pd.read_csv('data/Race_Results.csv')
races = pd.read_csv('data/Race_Schedule.csv')
drivers = pd.read_csv('data/Driver_Details.csv')
constructors = pd.read_csv('data/Team_Details.csv')

# Get a quick overview of each file.
print("=== RACE RESULTS ===")
print(results.shape)
print(results.head())

print("=== RACE SCHEDULE ===")
print(races.shape)
print(races.head())

print("=== DRIVERS ===")
print(drivers.shape)
print(drivers.head())

print("=== CONSTRUCTORS ===")
print(constructors.shape)
print(constructors.head())


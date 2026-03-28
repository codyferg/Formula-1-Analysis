import pandas as pd

# Load all datasets
results = pd.read_csv('data/Race_Results.csv')
races = pd.read_csv('data/Race_Schedule.csv')
drivers = pd.read_csv('data/Driver_Details.csv')
constructors = pd.read_csv('data/Team_Details.csv')
constructor_results = pd.read_csv('data/Constructor_Performance.csv')
constructor_standings = pd.read_csv('data/Constructor_Rankings.csv')
driver_standings = pd.read_csv('data/Driver_Rankings.csv')
pit_stops = pd.read_csv('data/Pit_Stop_Records.csv')
qualifying = pd.read_csv('data/Qualifying_Results.csv')
lap_times = pd.read_csv('data/Lap_Timings.csv')

# Filter races to 2018 - 2024
races_filtered = races[races['year'].between(2018, 2024)]

# Get the raceIDs for that period
valid_race_ids = races_filtered['raceId']

# Filter all other tables to only include those raceIds
results_filtered = results[results['raceId'].isin(valid_race_ids)]
constructor_results_filtered = constructor_results[constructor_results['raceId'].isin(valid_race_ids)]
constructor_standings_filtered = constructor_standings[constructor_standings['raceId'].isin(valid_race_ids)]
driver_standings_filtered = driver_standings[driver_standings['raceId'].isin(valid_race_ids)]
pit_stops_filtered = pit_stops[pit_stops['raceId'].isin(valid_race_ids)]
qualifying_filtered = qualifying[qualifying['raceId'].isin(valid_race_ids)]
lap_times_filtered = lap_times[lap_times['raceId'].isin(valid_race_ids)]

# Print shapes to confirm working filter
print("=== FILTERED SHAPES (should all be 2018 - 2024 ONLY) ===")
print(f"Races: {races_filtered.shape}")
print(f"Results: {results_filtered.shape}")
print(f"Constructor Results: {constructor_results_filtered.shape}")
print(f"Constructor Standings: {constructor_standings_filtered.shape}")
print(f"Driver Standings: {driver_standings_filtered.shape}")
print(f"Pit Stops: {pit_stops_filtered.shape}")
print(f"Qualifying: {qualifying_filtered.shape}")
print(f"Lap Times: {lap_times_filtered.shape}")

# Save filtered datasets to new .csv files
races_filtered.to_csv('data/cleaned/races.csv', index=False)
results_filtered.to_csv('data/cleaned/results.csv', index=False)
constructor_results_filtered.to_csv('data/cleaned/constructor_results.csv', index=False)
constructor_standings_filtered.to_csv('data/cleaned/constructor_standings.csv', index=False)
driver_standings_filtered.to_csv('data/cleaned/driver_standings.csv', index=False)
pit_stops_filtered.to_csv('data/cleaned/pit_stops.csv', index=False)
qualifying_filtered.to_csv('data/cleaned/qualifying.csv', index=False)
lap_times_filtered.to_csv('data/cleaned/lap_times.csv', index=False)

# Save dimension tables as-is (no filtering needed)
drivers.to_csv('data/cleaned/drivers.csv', index=False)
constructors.to_csv('data/cleaned/constructors.csv', index=False)

print("\nAll cleaned files saved to data/cleaned/")
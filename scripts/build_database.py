import pandas as pd
import sqlite3

# Create a connection to a new SQLite database
conn = sqlite3.connect('data/f1_analysis.db')

# Load all cleaned CSVs and write them to the database
tables = {
    'races': 'data/cleaned/races.csv',
    'results': 'data/cleaned/results.csv',
    'drivers': 'data/cleaned/drivers.csv',
    'constructors': 'data/cleaned/constructors.csv',
    'constructor_results': 'data/cleaned/constructor_results.csv',
    'constructor_standings': 'data/cleaned/constructor_standings.csv',
    'driver_standings': 'data/cleaned/driver_standings.csv',
    'pit_stops': 'data/cleaned/pit_stops.csv',
    'qualifying': 'data/cleaned/qualifying.csv',
    'lap_times': 'data/cleaned/lap_times.csv',
}

for table_name, filepath in tables.items():
    df = pd.read_csv(filepath)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Loaded {table_name}: {df.shape}")

print("\nDatabase built successfully at data/f1_analysis.db")
conn.close()
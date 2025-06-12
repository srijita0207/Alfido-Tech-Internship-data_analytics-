import pandas as pd

# Load the dataset
df = pd.read_csv('traffic.csv')

# Convert the 'date' column to datetime objects
df['date'] = pd.to_datetime(df['date'])

# Handle missing values
df['country'].fillna('Unknown', inplace=True)
df['city'].fillna('Unknown', inplace=True)
df['artist'].fillna('Unknown', inplace=True)
df['album'].fillna('Unknown', inplace=True)
df['track'].fillna('Unknown', inplace=True)
df['isrc'].fillna('Unknown', inplace=True)

# Display the first few rows after preprocessing
print(df.head())

# Display column names and their data types after preprocessing
print(df.info())

#Step 2 Key Metrics Calculation
total_events = len(df)
print(f"Total events: {total_events}")
event_counts = df['event'].value_counts()
print("\nEvent Distribution:\n", event_counts)

#Unique Visitors/Sessions
unique_linkids = df['linkid'].nunique()
print(f"\nNumber of unique links/sessions: {unique_linkids}")

#Traffic by Country and City
top_countries = df['country'].value_counts().head(10)
print("\nTop 10 Countries by Traffic:\n", top_countries)

top_cities = df['city'].value_counts().head(10)
print("\nTop 10 Cities by Traffic:\n", top_cities)

#Most Popular Content
top_artists = df['artist'].value_counts().head(10)
print("\nTop 10 Artists:\n", top_artists)

top_albums = df['album'].value_counts().head(10)
print("\nTop 10 Albums:\n", top_albums)

top_tracks = df['track'].value_counts().head(10)
print("\nTop 10 Tracks:\n", top_tracks)

#Step 3: Time-Based Analysis
#Daily Trends
daily_events = df.groupby('date').size()
print("\nDaily Events:\n", daily_events)

#Step 4: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns


#Daily Events Line Chart:
plt.figure(figsize=(12, 6))
sns.lineplot(x=daily_events.index, y=daily_events.values, marker='o', color='blue')
plt.title('Daily Website Events')
plt.xlabel('Date')
plt.ylabel('Number of Events')
plt.grid(True)
plt.show()




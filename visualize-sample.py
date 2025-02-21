import pandas as pd
from pandas_profiling import ProfileReport

# Read your CSV file into a DataFrame
csv_file = "sample/paraguay_fixed.csv"
df = pd.read_csv(csv_file)

# Generate a profile report
profile = ProfileReport(df, title="Paraguay Address Data Report", explorative=True)

# Save the report as an HTML file
profile.to_file("paraguay_report.html")

print("Report generated: paraguay_address_report.html")

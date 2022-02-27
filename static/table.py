import pandas as pd

# read csv file
csv_file = '../Resources/cities.csv'
data_df = pd.read_csv(csv_file)

# render as HTML table
data_df.to_html('html/table.html', index=False)

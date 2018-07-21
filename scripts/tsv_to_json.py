import pandas as pd
csv_file = pd.DataFrame(pd.read_csv("elections.tsv", sep = "\t", header = 0, parse_dates=['registration_deadline', 'next_primary_date', 'general_election_date']))
csv_file.to_json("elections.json", orient = "records", date_format='%Y%m%d', double_precision = 0, force_ascii = True, default_handler = None)
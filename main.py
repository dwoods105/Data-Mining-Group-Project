import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("chronicdata.cdc.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(chronicdata.cdc.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")


results = client.get("hfr9-rurv", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
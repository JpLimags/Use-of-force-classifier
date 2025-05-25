import os 
import pandas as pd 
from sodapy import Socrata

client = Socrata("data.seattle.gov", None)

count_query = client.get("ppi5-g2bj", select="count(*)")
total_records = int(count_query[0]['count'])

results = client.get("ppi5-g2bj", limit=total_records)

df = pd.DataFrame.from_records(results)

output_dir = r'C:\Users\Jp Lima\Desktop\Use-of-force-classifier\Use-of-force-classifier\data\external'

os.makedirs(output_dir, exist_ok=True)
df.to_csv(os.path.join(output_dir, 'dataset.csv'), index=False)
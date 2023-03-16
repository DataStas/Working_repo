import json
import pandas as pd

with open('Batches.js') as file:
    data = pd.read_json(file)
    print(data.head(5))
# Mixing dicts with non-Series may lead to ambiguous ordering 

import json

import pandas as pd

data = json.load(open('example.json'))

df = pd.DataFrame(data['body'])

#     name  salary
# 0  Alice     100
# 1  Bobby      50
# 2   Carl      75
print(df)
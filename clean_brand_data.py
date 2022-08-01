# Creating dictionary of:
#   partner_data = {companyName: {'companyField': set([values.enumerate()])}}
import pandas as pd
dummy_df = pd.read_csv("./dummy.csv")
partner_data = {}
for i in dummy_df.index:
    current_col = {k: v.split(',') for k, v in dummy_df.loc[i].items()}
    # Converting Yes/No string to Bool
    if current_col['brandIsOpenToPartnerIntly'] == 'No':
      current_col['brandIsOpenToPartnerIntly'] = [False]
    else: 
      current_col['brandIsOpenToPartnerIntly'] = [True]
    partner_data[str(current_col['companyName'].pop())] = current_col
    del current_col['companyName']

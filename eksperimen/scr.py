import pandas as pd
import sklearn
import numpy as np
from sklearn import preprocessing

main_df = pd.read_csv("CencusIncome.data.txt", header = None, delimiter = ",")
main_df = main_df.rename(columns={0: 'age', 1: 'workclass', 2: 'fnlwgt', 3: 'education', 4: 'education-num', 5: 'marital-status', 6: 'occupation',7: 'relationship', 8: 'race',9: 'sex', 10: 'capital-gain', 11: 'capital-loss', 12: 'hours-per-week', 13: 'native-country', 14: 'label'})

main_df['education'] = pd.to_numeric(main_df['education'], errors='ignore')

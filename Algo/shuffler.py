import pandas as pd
from sqlalchemy import null
from sympy import frac
from matplotlib import pyplot as plt
import pandas as pd

path_file = 'odds_shuf.csv'
path_out_sh = 'odds_shuf10.csv'

df_full = pd.read_csv(path_file, delimiter=',')

df_notPPN = df_full[df_full['Result']!=4]
df_notPPN = df_notPPN[df_full['Result']!=5]
df_notPPN = df_notPPN[df_notPPN['Result']!=null]
df_notPPN = df_notPPN[df_notPPN['Result']!=34]

df_selected = df_notPPN.loc[:,['HomeTeam','AwayTeam','HomeAvgPolarity', 'HomeElo', 'AwayAvgPolarity', 'AwayElo', 'Result','HomeWinOdds','DrawOdds','AwayWinOdds']]

df_selected['diffElo'] = df_selected.HomeElo- df_selected.AwayElo
df_selected['diffSent'] = 1000 * (df_selected.HomeAvgPolarity- df_selected.AwayAvgPolarity)

df_diff = df_selected.loc[:,['diffElo', 'diffSent', 'Result']]

shuffled_Data = df_selected.sample(frac=1,random_state = 10)

shuffled_Data.to_csv(path_out_sh, index=False)

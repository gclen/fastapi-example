import pandas as pd
from sqlalchemy import create_engine

win_counts = {'Arizona Diamondbacks': 1,
             'Atlanta Braves': 3,
             'Baltimore Orioles': 3,
             'Boston Red Sox': 9,
             'Chicago Cubs': 3,
             'Chicago White Sox': 3,
             'Cincinnati Reds': 5,
             'Cleveland Indians': 2,
             'Colorado Rockies': 0,
             'Detroit Tigers': 4,
             'Houston Astros': 1,
             'Kansas City Royals': 2,
             'Los Angeles Angels': 1,
             'Los Angeles Dodgers': 6,
             'Miami Marlins': 2,
             'Milwaukee Brewers': 0,
             'Minnesota Twins': 3,
             'New York Mets': 2,
             'New York Yankees': 27,
             'Oakland Athletics': 9,
             'Philadelphia Phillies': 2,
             'Pittsburgh Pirates': 5,
             'San Diego Padres': 0,
             'San Francisco Giants': 8,
             'Seattle Mariners': 0,
             'St. Louis Cardinals': 11,
             'Tampa Bay Rays': 0,
             'Texas Rangers': 0,
             'Toronto Blue Jays': 2,
             'Washington Nationals': 1}

win_list = [(k, v) for k, v in win_counts.items()]
df = pd.DataFrame(win_list, columns=['team', 'wins'])
engine = create_engine('sqlite:///sql_app.db')

df.to_sql('teams', engine, index_label='id', if_exists='replace')

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('./spotify.csv')

print(df.head())

# streams & playlists
r, p = stats.pearsonr(df['streams'], df['in_spotify_playlists']) 
print(f'r (Pearson correlation coefficient): {r:.3f}')
print(f'p-value:                             {p:.3f}')

print('')

# bpm & released month
r, p = stats.pearsonr(df.bpm, df.released_month)
print(f'r (Pearson correlation coefficient): {r:.3f}')
print(f'p-value:                             {p:.3f}')


# practice code to understand 


r, p = # take the results produced and put them into r and p variables 
       # stats.pearsonr(...) produces 2 results:
            # 1st result -> correlation coefficient
            # 2nd result -> p-value 

stats.pearsonr(...) # Pearson correlation. Its job is to take two sets of numbers and calculate correlation 
                    # ex. stats.pearson(x, y) means calculate the correlation between x and y. Remember it gives us two results to store in r and p

print(f'r (Pearson correlation coefficient: {r:.3f}') # Fancy formatting to display the r variable which pulled the result out of streams/in_spotify_playlists
# same thing for the p value 

# it is the same thing below just for different tables in our data.

# For analyzing the data 

# Strength: range from 0.0 - 1.0 
# Direction: positive or negative or neutral 

# p = statistical significance 
# p < 0.05 -> statistically significant 
# p >= 0.05 -> not statistically significant 


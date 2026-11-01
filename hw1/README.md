# CSE 583 Homework 1

## Project Overview

This project analyzes hourly bicycle counts recorded at the Fremont Bridge base on the data from 2016.

## Analysis 

I first downloaded the CSV data via the link on the canvas page and loaded it into a pandas DataFrame.

I inspected the columns and their original data types. 
The `Date` column was originally stored as an object, so I converted it to pandas datetime format. 
The bicycle-count columns were originally stored as `float64` and I converted these columns to pandas nullable `Int64`.

I added columns for the combined east and west bicycle count, the hour of the day, and the year. 
Then created a new DataFrame containing only observations from 2016.

The 2016 dataset contained one row missing bicycle-count data:`2016-03-13 02:00:00`. 
To make sure the missing will not influence the further exploration I removed it directly.

I grouped the cleaned data by hour and created a plot of bicycle counts for each hour. 
I also calculated the average bicycle count for each hour.


## Output

1. The analysis creates the following figure:
- `counts_by_hour.png`

2. We get the busiest hour is 5 PM

## AI Assistance

I used ChatGPT/Codex to understand pandas operations and review the code and set .gitignore. 
I wrote and ran the code step by step in VS Code and checked the output after each part.

## Bonus: Datetime Formats

I converted the entire `Date` column using `pd.to_datetime()`.

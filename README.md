
# Boca Data Analyst

A small data analysis project exploring Boca Juniors' performance in the 2026 Torneo Apertura (Argentine league) group stage, built with pure Python — no external libraries.

## What this does

The script stores 16 matches (Boca's full Zone A group stage) as a list of dictionaries, then uses functions to calculate:

- Wins, draws, and losses
- Win rate (overall, home, and away)
- Goals scored and conceded (overall, home, and away)
- Goal difference
- Average goals scored/conceded per match

## Findings

Looking at the data, Boca didn't necessarily lose their home advantage — they remained unbeaten at home defensively — but offensively they were poor at La Bombonera, scoring more goals and winning more often away from home than they did at home.

## Why pure Python

This project was built while learning the basics of Python (lists, dictionaries, functions, comprehensions) before moving on to NumPy and pandas. The goal was to practice turning raw structured data into real conclusions using only built-in tools.

## Next steps

- Add more matches as the season continues
- Rebuild this same analysis using pandas for comparison
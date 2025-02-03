# Forex Currency Strength Meter
Retrieves Forex data from MT5 and calculates the strength of currency. Afterward, result is sent to a messaging application (Telegram). Used AWS EC2 to keep the script running 24/7.

## Dataset
Open, high, low, and close values of the last 'n' candles of the eight major currencies (EUR, GBP, AUD, NZD, USD, CAD, CHF, JPY).

## Output
A message about the cumulative percent change of each currency displayed as values and as a bar chart image. Additionally, provides recommendation of tradeable currency pairs depending on the cutoff value set.

# Process
## Choosing the data

I chose rainfall data because the Chinese character “雨” (rain) is part of my name. This personal connection made me curious about using rainfall as the subject of my visualization. I used daily rainfall data for 2026 published by the Hong Kong Observatory and saved the original CSV file in the `data/` folder.
## Working with the data

I first opened the CSV file to understand its structure. I then wrote `plot.py` to read the data and select February 2026. I converted “Trace” rainfall values to 0 so that they could be plotted as numbers.
## Making the visualization

I used a bar chart to show the daily rainfall in February. Each bar represents one day, and its height represents the rainfall in millimetres. The result makes the contrast easy to see: most days had little or no rain, while February 28 had a much higher rainfall of 39 mm.

## What I kept and changed

I kept the bar chart because it makes the difference between dry and rainy days easy to see. While working with the data, I found that “Trace” values could not be read directly as numbers, so I changed them to 0 for the visualization. I also fixed blank rows in the CSV and removed a mistake that added each rainfall value twice.

I kept the final version with one bar for each day because it is simple and clearly shows the unusual rainfall on February 28. I rejected the incorrect version with duplicated rainfall values because it did not match the 28 days in February.
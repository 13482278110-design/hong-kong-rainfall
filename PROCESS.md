# Process

## Choosing the data

I chose rainfall data because the Chinese character “雨” (rain) is part of my name. This personal connection made me curious about using rainfall as the subject of my visualization. I used daily rainfall data for 2026 published by the Hong Kong Observatory and saved the original CSV file in the `data/` folder.

## Working with the data

I first opened the CSV file to understand its structure. I then wrote `plot.py` to read the data and select February 2026. I converted “Trace” rainfall values to 0 so that they could be plotted as numbers. I also fixed blank rows in the CSV and removed a mistake that added each rainfall value twice.

## Making the visualization

My first version used a simple bar chart. It clearly showed that most days were dry and February 28 had much more rainfall, but I felt that the bars were too generic and did not visually connect to the phenomenon of rain.

I changed each rainy day into a raindrop generated directly in Python. The rainfall value controls the size of the drop, while days with no rainfall are shown as small pale dots. I used a square-root scale so that small rainfall values remain visible while the 39 mm rainfall on February 28 still stands out.

## What I kept and rejected

I kept the horizontal sequence of 28 days because it makes the month easy to read from beginning to end. I also kept the actual rainfall values next to rainy days so that the visualization remains connected to the original data.

I rejected the original bar chart because it communicated the numbers but felt too generic. I also tested several raindrop shapes and proportions. Some were too narrow and looked more like leaves or needles, while others were too wide and covered nearby data. I kept the final, slightly narrower raindrop shape because it makes the rainfall metaphor clearer without hiding the neighbouring days.
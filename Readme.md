
# The Unequal Price of Progress

## Project Overview

An interactive data visualization dashboard exploring
global development and environmental change from 2000 to 2022.

The project uses World Bank data to examine the relationship
between economic growth, human well-being, digital inclusion,
and environmental sustainability.

## Dataset

Source: World Bank development indicators

Main variables:
- Country
- Country_Code
- Region
- Year
- Life_Expectancy
- GDP_Per_Capita
- CO2e_Per_Capita
- Internet_Users_Pct
- Population

## Dashboard Features

- Interactive region and year filters
- Development summary metrics
- Life expectancy trend
- Internet usage trend
- CO2e emissions trend
- GDP per capita vs life expectancy scatter plot
- Interactive life expectancy map
- Country comparison
- Filtered data table

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

## How to Run

1. Install Python.
2. Install the required packages:

   pip install -r requirements.txt

3. Run the dashboard:

   streamlit run app.py

4. Open the local URL shown in the terminal.

## Research Message

Progress should not be measured through economic growth alone.
It must also be evaluated through human well-being, digital
inclusion, regional equality, and environmental sustainability.

## Data Limitations

Annual averages are unweighted averages of available country
observations. Missing data and differences in country coverage
should be considered when interpreting the results.


import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="The Unequal Price of Progress",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 The Unequal Price of Progress")
st.subheader(
    "Global Development and Environmental Change (2000–2022)"
)

st.markdown("""
Explore how economic growth, human well-being,
digital inclusion and environmental change vary
across countries and regions.
""")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("world_bank_development_cleaned.csv")
    return df

data = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Dashboard Filters")

regions = sorted(data["Region"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

years = sorted(data["Year"].dropna().unique())

selected_years = st.sidebar.slider(
    "Select Year Range",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=(int(min(years)), int(max(years)))
)

filtered_data = data[
    (data["Region"].isin(selected_regions)) &
    (data["Year"].between(
        selected_years[0],
        selected_years[1]
    ))
].copy()

# -----------------------------
# KPI METRICS
# -----------------------------
st.header("Development Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Countries / Economies",
    filtered_data["Country"].nunique()
)

c2.metric(
    "Average Life Expectancy",
    f'{filtered_data["Life_Expectancy"].mean():.1f} years'
)

c3.metric(
    "Average GDP per Capita",
    f'${filtered_data["GDP_Per_Capita"].mean():,.0f}'
)

c4.metric(
    "Average Internet Usage",
    f'{filtered_data["Internet_Users_Pct"].mean():.1f}%'
)

# -----------------------------
# COUNTRY SELECTION
# -----------------------------
st.sidebar.subheader("Country Comparison")

countries = sorted(filtered_data["Country"].dropna().unique())

selected_countries = st.sidebar.multiselect(
    "Choose Countries",
    countries,
    default=countries[:3]
)

country_data = filtered_data[
    filtered_data["Country"].isin(selected_countries)
]

# -----------------------------
# LIFE EXPECTANCY TREND
# -----------------------------
st.header("1. Human Well-being Over Time")

life_trend = (
    filtered_data.groupby("Year", as_index=False)
    ["Life_Expectancy"].mean()
)

fig1 = px.line(
    life_trend,
    x="Year",
    y="Life_Expectancy",
    markers=True,
    title="Average Life Expectancy (2000–2022)"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# INTERNET USAGE TREND
# -----------------------------
st.header("2. Digital Inclusion")

internet_trend = (
    filtered_data.groupby("Year", as_index=False)
    ["Internet_Users_Pct"].mean()
)

fig2 = px.line(
    internet_trend,
    x="Year",
    y="Internet_Users_Pct",
    markers=True,
    title="Internet Usage Trend"
)

fig2.update_yaxes(title="Internet Users (%)")

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# CO2e EMISSIONS TREND
# -----------------------------
st.header("3. Environmental Sustainability")

co2_trend = (
    filtered_data.groupby("Year", as_index=False)
    ["CO2e_Per_Capita"].mean()
)

fig3 = px.line(
    co2_trend,
    x="Year",
    y="CO2e_Per_Capita",
    markers=True,
    title="CO2e Emissions per Capita"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# GDP VS LIFE EXPECTANCY
# -----------------------------
st.header("4. Economic Development and Well-being")

scatter_data = filtered_data.dropna(
    subset=["GDP_Per_Capita", "Life_Expectancy"]
)

fig4 = px.scatter(
    scatter_data,
    x="GDP_Per_Capita",
    y="Life_Expectancy",
    color="Region",
    hover_name="Country",
    size="Population",
    log_x=True,
    title="GDP per Capita vs Life Expectancy"
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# LIFE EXPECTANCY MAP
# -----------------------------
st.header("5. Geographical Distribution")

map_year = int(selected_years[1])

map_data = data[
    (data["Year"] == map_year)
].dropna(
    subset=["Life_Expectancy", "Country_Code"]
)

fig5 = px.choropleth(
    map_data,
    locations="Country_Code",
    color="Life_Expectancy",
    hover_name="Country",
    hover_data=["Region", "Life_Expectancy"],
    locationmode="ISO-3",
    color_continuous_scale="YlGnBu",
    title=f"Life Expectancy Across Countries ({map_year})"
)

st.plotly_chart(fig5, use_container_width=True)

# -----------------------------
# COUNTRY COMPARISON
# -----------------------------
st.header("6. Country Comparison")

if not country_data.empty:
    fig6 = px.bar(
        country_data,
        x="Country",
        y="Life_Expectancy",
        color="Region",
        title="Life Expectancy by Selected Country",
        barmode="group"
    )

    st.plotly_chart(fig6, use_container_width=True)

# -----------------------------
# DATA TABLE
# -----------------------------
st.header("7. Filtered Dataset")

st.dataframe(
    filtered_data,
    use_container_width=True
)

# -----------------------------
# CONCLUSION
# -----------------------------
st.header("Key Message")

st.markdown("""
Progress should not be measured through economic growth alone.
It must also be evaluated through human well-being,
digital inclusion, regional equality, and environmental sustainability.
""")

st.caption(
    "Source: World Bank development indicators, 2000–2022. "
    "Annual averages are unweighted averages of available observations."
)

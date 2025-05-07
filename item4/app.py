import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import random

st.title("🦠 COVID-19 Dashboard")

# --- User input ---
country = st.text_input("Enter country", "USA")

# --- Fetch Data ---
url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # ✅ Parse data
    cases = data["timeline"]["cases"]
    deaths = data["timeline"]["deaths"]
    recovered = data["timeline"]["recovered"]

    df = pd.DataFrame({
        "Date": pd.to_datetime(list(cases.keys())),
        "Cases": list(cases.values()),
        "Deaths": list(deaths.values()),
        "Recovered": list(recovered.values())
    }).set_index("Date")

    df["New Cases"] = df["Cases"].diff().fillna(0)
    df["New Deaths"] = df["Deaths"].diff().fillna(0)
    df["New Recovered"] = df["Recovered"].diff().fillna(0)

    # --- Metrics ---
    st.subheader(f"📊 Key Metrics for {country}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Cases", f"{df['Cases'].iloc[-1]:,.0f}")
    col2.metric("Total Deaths", f"{df['Deaths'].iloc[-1]:,.0f}")
    col3.metric("Total Recovered", f"{df['Recovered'].iloc[-1]:,.0f}")

    # --- Chart 1: Line chart ---
    st.subheader("1️⃣ Daily New Cases – Line Chart")
    st.line_chart(df["New Cases"])

    # --- Chart 2: Bar chart ---
    st.subheader("2️⃣ Daily New Deaths – Bar Chart")
    st.bar_chart(df["New Deaths"])

    # --- Chart 3: Area chart ---
    st.subheader("3️⃣ Daily Recoveries – Area Chart")
    st.area_chart(df["New Recovered"])

    # --- Chart 4: Pie chart ---
    st.subheader("4️⃣ Pie Chart – Current Case Breakdown")
    latest_totals = {
        "Active": df["Cases"].iloc[-1] - df["Deaths"].iloc[-1] - df["Recovered"].iloc[-1],
        "Recovered": df["Recovered"].iloc[-1],
        "Deaths": df["Deaths"].iloc[-1],
    }
    pie_df = pd.DataFrame(latest_totals.items(), columns=["Status", "Count"])
    fig = px.pie(pie_df, values="Count", names="Status", title="COVID-19 Case Status Breakdown")
    st.plotly_chart(fig)

    # --- Chart 5: Scatter plot ---
st.subheader("5️⃣ Scatter Plot – New Cases vs. New Deaths")
scatter_df = df[["New Cases", "New Deaths"]].copy()
scatter_df["Date"] = scatter_df.index
scatter_df["Size"] = scatter_df["New Deaths"].clip(lower=0.1)  # FIXED LINE

fig2 = px.scatter(
    scatter_df,
    x="New Cases",
    y="New Deaths",
    size="Size",  # Now safe
    color="Date",
    title="New Cases vs. New Deaths",
    labels={"New Cases": "New Cases", "New Deaths": "New Deaths"}
)
st.plotly_chart(fig2)


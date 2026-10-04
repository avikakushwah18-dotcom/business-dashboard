import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Business Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sample business data
data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Revenue": [
        120000, 135000, 142000, 155000, 168000, 175000,
        182000, 195000, 205000, 218000, 230000, 245000
    ],
    "Marketing_Spend": [
        18000, 19000, 20000, 21000, 22000, 23000,
        24000, 25000, 26000, 27000, 28000, 30000
    ],
    "Customers": [
        240, 260, 275, 290, 310, 325,
        340, 360, 380, 400, 425, 450
    ],
    "Orders": [
        300, 325, 350, 370, 395, 415,
        435, 460, 485, 510, 540, 575
    ],
    "Churn_Rate": [
        8.2, 7.9, 7.5, 7.2, 6.9, 6.7,
        6.5, 6.2, 6.0, 5.8, 5.6, 5.4
    ],
    "Region": [
        "Central", "West", "North", "South",
        "Central", "West", "North", "South",
        "Central", "West", "North", "South"
    ]
}

df = pd.DataFrame(data)

# KPI calculations
total_revenue = df["Revenue"].sum()
total_customers = df["Customers"].sum()
total_orders = df["Orders"].sum()

avg_order_value = total_revenue / total_orders
cac = df["Marketing_Spend"].sum() / total_customers
avg_churn = df["Churn_Rate"].mean()

# Dashboard title
st.title("📊 Business Performance Dashboard")
st.markdown("### Executive Overview")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")

with col2:
    st.metric("🎯 Customer Acquisition Cost", f"₹{cac:,.2f}")

with col3:
    st.metric("📉 Churn Rate", f"{avg_churn:.1f}%")

with col4:
    st.metric("🛒 Average Order Value", f"₹{avg_order_value:,.0f}")

st.divider()

# Sidebar filter
st.sidebar.header("🔎 Dashboard Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[df["Region"].isin(selected_region)]

# Revenue Trend
st.subheader("📈 Revenue Trend")

fig_revenue = px.area(
    filtered_df,
    x="Month",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig_revenue, use_container_width=True)

# Customer Growth and Orders
col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Customer Growth")

    fig_customers = px.line(
        filtered_df,
        x="Month",
        y="Customers",
        markers=True,
        title="Monthly Customer Growth"
    )

    st.plotly_chart(fig_customers, use_container_width=True)

with col2:
    st.subheader("🛒 Orders")

    fig_orders = px.bar(
        filtered_df,
        x="Month",
        y="Orders",
        title="Monthly Orders"
    )

    st.plotly_chart(fig_orders, use_container_width=True)

# Churn Rate
st.subheader("📉 Churn Rate Trend")

fig_churn = px.line(
    filtered_df,
    x="Month",
    y="Churn_Rate",
    markers=True,
    title="Monthly Churn Rate"
)

st.plotly_chart(fig_churn, use_container_width=True)

# Regional Performance
st.subheader("🌍 Geographic / Regional Performance")

region_data = (
    filtered_df.groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_data,
    x="Region",
    y="Revenue",
    color="Region",
    title="Revenue by Region"
)

st.plotly_chart(fig_region, use_container_width=True)

# Data table
st.subheader("📋 Detailed Business Data")

st.dataframe(filtered_df, use_container_width=True)

# Conclusion
st.success(
    "Dashboard successfully analyzes revenue, customer acquisition cost, "
    "churn rate, average order value, customer growth and regional performance."
)

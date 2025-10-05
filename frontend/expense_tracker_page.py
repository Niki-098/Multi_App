import streamlit as st
import pandas as pd
from datetime import datetime

def expense_tracker_app():
    st.title("💰 Personal Expense Tracker")
    st.write("Track your weekly or monthly expenses easily.")

    if "expenses" not in st.session_state:
        st.session_state["expenses"] = []

    category = st.selectbox("Select category:", ["Food", "Rent", "Travel", "Entertainment", "Other"])
    amount = st.number_input("Enter amount:", min_value=0.0, step=0.5)
    date = st.date_input("Date:", datetime.today())

    if st.button("Add Expense"):
        st.session_state["expenses"].append({"Category": category, "Amount": amount, "Date": date})
        st.success("Expense added!")

    if st.session_state["expenses"]:
        df = pd.DataFrame(st.session_state["expenses"])
        st.subheader("All Expenses")
        st.dataframe(df)

        period = st.radio("View summary by:", ["Weekly", "Monthly"])
        df["Date"] = pd.to_datetime(df["Date"])

        if period == "Weekly":
            summary = df.groupby(df["Date"].dt.isocalendar().week)["Amount"].sum()
        else:
            summary = df.groupby(df["Date"].dt.month)["Amount"].sum()

        st.subheader(f"{period} Summary")
        st.bar_chart(summary)

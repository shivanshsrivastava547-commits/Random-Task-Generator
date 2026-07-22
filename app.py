import streamlit as st
import pandas as pd
import random

st.title("🎯 Random Task Generator")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

name = st.text_input("Employee Name")

if st.button("Generate Task"):

    if uploaded_file is None:
        st.error("Please upload an Excel file.")

    elif name.strip() == "":
        st.warning("Please enter an employee name.")

    else:
        df = pd.read_excel(uploaded_file)

        df.columns = df.columns.str.strip()
        df["NAME"] = df["NAME"].str.strip().str.upper()

        row = df[df["NAME"] == name.strip().upper()]

        if row.empty:
            st.error("Employee not found!")

        else:
            tasks = row.iloc[0, 1:].dropna().str.strip().tolist()

            task = random.choice(tasks)

            st.success(f"Task Assigned: {task}")
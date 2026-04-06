import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Document Q&A Chatbot", layout="wide")

st.title("📄🤖 Document Q&A Chatbot")

# Upload document
file = st.file_uploader("Upload CSV Document", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.write("### 📊 Data Preview")
    st.dataframe(df.head())

    st.write("### 🧠 Ask Questions")
    question = st.text_input("Type your question:")

    if question:
        q = question.lower()
        st.write("### 🤖 Answer")

        # Detect column names
        cols = df.columns.tolist()
        matched_col = None

        for col in cols:
            if col.lower() in q:
                matched_col = col
                break

        # ===== Q&A Logic =====

        # Average
        if "average" in q or "mean" in q:
            if matched_col:
                result = np.mean(df[matched_col])
                st.success(f"Average of '{matched_col}' = {result:.2f}")

        # Sum
        elif "sum" in q or "total" in q:
            if matched_col:
                result = np.sum(df[matched_col])
                st.success(f"Total of '{matched_col}' = {result:.2f}")

        # Max
        elif "max" in q or "highest" in q:
            if matched_col:
                result = np.max(df[matched_col])
                st.success(f"Maximum of '{matched_col}' = {result}")

        # Min
        elif "min" in q or "lowest" in q:
            if matched_col:
                result = np.min(df[matched_col])
                st.success(f"Minimum of '{matched_col}' = {result}")

        # Count
        elif "count" in q:
            st.success(f"Total rows = {len(df)}")

        # Correlation
        elif "correlation" in q:
            st.write(df.corr(numeric_only=True))

        # Plotting
        elif "plot" in q or "graph" in q or "chart" in q:
            numeric_cols = df.select_dtypes(include=np.number).columns

            if len(numeric_cols) >= 2:
                x = numeric_cols[0]
                y = numeric_cols[1]

                fig, ax = plt.subplots()
                ax.scatter(df[x], df[y], color='blue')
                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title(f"{x} vs {y}")

                st.pyplot(fig)

        # Summary
        elif "summary" in q or "describe" in q:
            st.write(df.describe())

        # Column list
        elif "columns" in q:
            st.write("Columns:", cols)

        else:
            st.warning("❌ I can answer only basic data-related questions.")

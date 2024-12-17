import streamlit as st
import pandas as pd
from backend.api_connections import connect_google_sheets
from backend.data_processing import process_file
import io

def render_ui():
    st.title("AI Agent: Data Extraction")

    # Option to choose file type: CSV or Google Sheets
    file_type = st.selectbox("Choose File Type", ["CSV", "Google Sheets"])

    # Input for Google Sheets
    if file_type == "Google Sheets":
        sheet_url = st.text_input("Enter Google Sheets URL:")
        if sheet_url:
            sheet_data = connect_google_sheets(sheet_url)
            st.write("Google Sheets Data Preview:")
            st.write(sheet_data.head())  # Displaying first few rows of Google Sheets

    # Input for CSV upload
    if file_type == "CSV":
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("CSV Data Preview:")
            st.write(df.head())  # Displaying first few rows of CSV

    # Query input from user
    query = st.text_input("Enter your query:")

    # Submit Button (centered)
    submit_button = st.button("Submit", use_container_width=True)

    if submit_button:
        # Processing the file and getting query results
        if file_type == "CSV" and uploaded_file is not None:
            result = process_file(df, query)
        elif file_type == "Google Sheets":
            result = process_file(sheet_data, query)

        # Display results from LLM
        if result:
            st.write(f"**Query Result:** {result}")

            # Provide a download button
            download_button = st.download_button(
                label="Download Results",
                data=result,
                file_name="result.csv",
                mime="text/csv"
            )

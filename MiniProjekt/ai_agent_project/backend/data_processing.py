import pandas as pd
from backend.llm_integration import get_llm_response  # Import the LLM function

def process_file(data, query):
    # First, prepare the data context (columns, first few rows, and any relevant metadata)
    columns = data.columns.tolist()  # Get all column names
    sample_data = data.head().to_string(index=False)  # Get a preview of the first few rows
    data_summary = f"Columns available in the data: {', '.join(columns)}\n\nSample data:\n{sample_data}"

    # Prepare the full context for the LLM
    context = f"Dataset information:\n{data_summary}\n\nQuery: {query}"

    # Get LLM's response based on the data and the query
    response = get_llm_response(context)
    
    return response

# AICharts
AI-based chart generation code from uploaded data.

This repo utilizes the Streamlit library and the ChatGPT API to automatically generate charts and tables from an uploaded dataset. Users can simply upload their data in CSV format, specify the desired chart or table type, and the code will handle the rest, returning a dynamic visualization powered by ChatGPT.

Prerequisites:
Python 3
Streamlit
OpenAI API Key (for ChatGPT)
Pandas
Installation:
Install the required libraries:
Bash
pip install streamlit pandas openai
Use code with caution. Learn more
Create a file named app.py and paste the following code:
Python
import streamlit as st
import pandas as pd
import openai

# Configure ChatGPT access
openai.api_key = "YOUR_OPENAI_API_KEY"

# Define available chart and table types
chart_types = ["Bar chart", "Line chart", "Pie chart", "Table"]
table_types = ["Simple table", "Pivot table"]

# Upload and read dataset
uploaded_file = st.file_uploader("Upload your data file (CSV)", type=".csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.write("Please upload a CSV file to proceed.")
    exit()

# Choose chart or table type
chart_type = st.selectbox("Choose a chart type", chart_types)
table_type = st.selectbox("Choose a table type", table_types)

# Generate prompt for ChatGPT
prompt = f"Create a {chart_type} from the following data:\n{df}"

# Send prompt to ChatGPT and parse response
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
)
chart_code = response.choices[0].text

# Display the chart or table using Streamlit
if chart_type in chart_types:
    st.plotly_chart(chart_code)
elif table_type in table_types:
    st.write(chart_code)
else:
    st.write("Invalid selection. Please choose a valid chart or table type.")
Use code with caution. Learn more
Replace YOUR_OPENAI_API_KEY with your OpenAI API key.

Run the code:

Bash
python app.py
Use code with caution. Learn more
Access the Streamlit app at http://localhost:8501.
Features:
Upload CSV data.
Choose desired chart or table type.
ChatGPT automatically generates chart code based on data and user selection.
Streamlit displays the chart or table dynamically.
Limitations:
ChatGPT response quality depends on the prompt and data structure.
The code currently supports a limited number of chart and table types.
This is a basic example and can be further enhanced with additional features and functionalities.
Future Enhancements:
Support more chart and table types.
Allow customization of chart and table styles.
Integrate with other data analysis libraries.
Implement error handling and robustness checks.

from langchain.chains import create_tagging_chain_pydantic

from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, Field
import streamlit as st
import pandas as pd
import os
import json

os.environ["OPENAI_API_KEY"] = "INSERT YOUR KEY HERE"

df_now = pd.DataFrame()

#def conv_json()

st.set_page_config(page_title="AI Chart")



st.title("AI Chart")

uploaded_file = st.file_uploader("Upload a dataset file in .csv or .xlsx format. Make sure that the first row contains column names.", type=['csv'])

if uploaded_file is not None:
    df_now = pd.read_csv(uploaded_file)
    st.dataframe(df_now, use_container_width=True)
    dfcolumns = df_now.columns.tolist()
    text_input = df_now.to_string()


if df_now is None:
    st.stop()

def show_chart(chartType, x_axis, y_axis):
    if chartType == "bar_chart":
        st.bar_chart(df_now, x=x_axis, y=y_axis, use_container_width=True)
    elif chartType == "area_chart":
        st.area_chart(df_now, x=x_axis, y=y_axis, use_container_width=True)
    elif chartType == "line_chart":
        st.line_chart(df_now, x=x_axis, y=y_axis, use_container_width=True)
    elif chartType == "scatter_plot":
        st.scatter_chart(df_now, x=x_axis, y=y_axis, use_container_width=True)
    return True

class DataFeature(BaseModel):
    chartType: str = Field(..., enum=["bar_chart", "line_chart", "area_chart","scatter_plot"],description="""
                        the chart type to visualize the dataframe strickly following rules:
                        Use 'area_chart': if the dataframe is monthly-basis, daily-basis, or yearly-basis
                        Use 'bar_chart': if the dataframe contains categorical data.
                        Use 'line_chart': if the dataframe is seconds-basis or smaller periods.
                        """)
    x_axis: str = Field(..., enum= dfcolumns, description="""
                        the column name in the dataframe that is best for the x-axis
                        """)
    y_axis: str = Field(..., enum= dfcolumns)#, description="""
                        #describes the x_axis name in the dataframe that is best for the x-axis.
                        #""")

def main():
    llm = ChatOpenAI(temperature=1, model="gpt-3.5-turbo-0613")

    tagging_chain = create_tagging_chain_pydantic(DataFeature, llm)
    st.write(tagging_chain)
    res = tagging_chain.run(text_input)
    
    st.write(res)
    show_chart(res.chartType, res.x_axis, res.y_axis)
    

main()
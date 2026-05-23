import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(model='openai/gpt-oss-20b',task='coversational',temperature=0.8,huggingfacehub_api_token=my_token)

model = ChatHuggingFace(llm=llm)

st.header("May i Help you !!")

input=st.text_input("whats on your mind today")

if st.button("-Send-"):
    result=model.invoke(input)
    st.write(result.content)

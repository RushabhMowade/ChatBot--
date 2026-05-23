import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(model='openai/gpt-oss-20b',task='coversational',temperature=0.8)

model = ChatHuggingFace(llm=llm)

st.header("May i Help you !!")
chat_history=[
    SystemMessage(content='You are helpful assistant')
]
input=st.text_input("whats on your mind today")
chat_history.append(HumanMessage(content=input))

if st.button("-Send-"):
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    st.write(result.content)

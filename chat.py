import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(model='openai/gpt-oss-20b',task='coversational',temperature=0.8)

model = ChatHuggingFace(llm=llm)

st.header("May i Help you !!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[
    SystemMessage(content='You are helpful assistant')
]
    
    for msg in st.session_state.chat_history:
        if isinstance(msg,HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg,AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)


if user_input := st.chat_input("Whats on your mind today..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("assistant"):
        result=model.invoke(st.session_state.chat_history)
        st.write(result.content)

    st.session_state.chat_history.append(AIMessage(content=result.content))

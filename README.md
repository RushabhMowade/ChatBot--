# 💬AI Chatbot

A real-time, continuous conversational assistant built with **Streamlit** and **LangChain**. The application leverages the open-source **`openai/gpt-oss-20b`** LLM via Hugging Face Endpoints, featuring robust chat memory and a polished, responsive user interface.

## 🚀 Key Features
* **Model Integration:** Powered by the 20-billion parameter `openai/gpt-oss-20b` model for text generation and conversational reasoning.
* **Persistent History:** Automatically retains and manages full conversation context utilizing LangChain's message tracking wrappers (`SystemMessage`, `HumanMessage`, `AIMessage`) inside Streamlit's persistent session state.
* **Streamlined UI:** Implements a clean, modern chat experience with native `st.chat_input` and `st.chat_message` blocks.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(model='openai/gpt-oss-20b',task='coversational',temperature=0.8)

model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content = "You are a Helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]
result = model.invoke(messages)
messages.append(AIMessage(content="result.content"))


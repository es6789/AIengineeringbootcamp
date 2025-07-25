import streamlit as st
from openai import OpenAI
from groq import Groq
from google import genai
from qdrant_client import QdrantClient

from retrieval import rag_pipeline

from core.config import config

qdrant_client = QdrantClient(
    url=f"http://{config.QDRANT_URL}:6333"
)

#Let's create a sidebar with a dropdown menu to select the model and provider
with st.sidebar:
    st.title("AI Chatbot")
    provider = st.selectbox("Select a provider", ["OpenAI", "Groq", "Google"])

    if provider == "OpenAI":
        model_name = st.selectbox("Select a model", ["gpt-4o-mini", "gpt-4o"])
    elif provider == "Groq":
        model_name = st.selectbox("Select a model", ["llama-3.3-70b-versatile"])
    elif provider == "Google":
        model_name = st.selectbox("Select a model", ["gemini-2.0-flash"])

    #Save provider and model in session state
    st.session_state.provider = provider
    st.session_state.model_name = model_name

if st.session_state.provider == "OpenAI":
    client = OpenAI(api_key=config.OPENAI_API_KEY)
elif st.session_state.provider == "Groq":
    client = Groq(api_key=config.GROQ_API_KEY)
elif st.session_state.provider == "Google":
    client = genai.Client(api_key=config.GOOGLE_API_KEY)

def run_llm(client, messages, max_tokens=500):
    if st.session_state.provider == "Google":
        return client.models.generate_content(
            model=st.session_state.model_name,
            contents=[message["content"] for message in messages]
        ).text
    else:
        return client.chat.completions.create(
            model=st.session_state.model_name,
            messages=messages,
            max_tokens=max_tokens
        ).choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You should never disclose which model you are based on"},{"role": "assistant", "content": "Hello! Can I assist you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Hello! Can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        #output = run_llm(client, st.session_state.messages)
        output = rag_pipeline(prompt, qdrant_client)
        st.write(output['response'])
    st.session_state.messages.append({"role": "assistant", "content": output}) 
import os 
from langchain_groq import ChatGroq


def load_model(flag:int = 0):
    if flag ==0:
        llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")
    elif flag ==1:
        llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
    elif flag ==2:
        llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
    elif flag ==3:
        llm = ChatGroq(temperature=0, model_name="gemma-7b-it")
    return llm

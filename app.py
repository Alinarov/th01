#!/usr/bin/env pytho

import streamlit as st
from transformers import pipeline


chatbot = pipeline("conversational", model="microsoft/DialogGPT-medium")

def get_chatbot_response(user_input):
	response = chatbot(user_input)
	return response[0]["generated_text"]


st.title("Chatbot de Recetas de Cocina")
user_input = st.text_input("¿Que deseas saber sobre las recetas?")


if user_input:
	response = get_chatbot_response(user_input)
	st.write("Respuesta del chatbot: ", response)


public_url = ngrok.connect(8501)
print("El chatbot esta disponible en: ", public_url)


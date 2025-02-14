#!/usr/bin/env python
import streamlit as st
import random


def pregunta_aleatoria_placeholder():
	preguntas = [
		"¿Cómo hacer arroz con pollo?",
		"¿Cómo hacer arroz con leche?",
		"¿Qué receta me recomiendas para un lunes?",
		"¿Qué necesito para un manjar blanco?"
	]
	index_random = random.randint(0, len(preguntas) - 1)  # Evitar índice fuera de rango
	return preguntas[index_random]

def main():


	st.set_page_config(page_title="Chatbot de Recetas", page_icon="🍳", layout="centered")
	# Estilo para el título
	st.markdown("<h1 style='text-align: center; color: #FF5733;'>🍳 Chatbot de Recetas</h1>", unsafe_allow_html=True)
	# Estilo para el header
	st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Tu asistente culinario inteligente</h2>", unsafe_allow_html=True)
	# Estilo para la descripción
	st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Bienvenido al chatbot de recetas. Pregunta sobre ingredientes, tiempos de cocción y más.</p>", unsafe_allow_html=True)
	# Sección de entrada del usuario con estilo mejorado
	st.markdown("<h3 style='color: #FF5733; font-size: 22px;'>📩 Escribe tu pregunta sobre recetas:</h3>", unsafe_allow_html=True)

	def get_response(user_input):
		# Respuestas simuladas (se pueden mejorar con IA o reglas más avanzadas)
		responses = {
			"¿Cómo hacer arroz con pollo?": "Para hacer arroz con pollo necesitas arroz, pollo, ajo, cebolla, pimiento, zanahoria, caldo de pollo y especias. Sofríe los ingredientes, agrega el arroz y el caldo, y cocina a fuego lento hasta que el arroz esté listo.",
			"¿Cómo hacer arroz con leche?": "Para hacer arroz con leche necesitas arroz, leche, azúcar, canela y cáscara de limón. Cocina el arroz con leche a fuego bajo, agrega el azúcar y la canela, y cocina hasta obtener una textura cremosa.",
			"¿Qué receta me recomiendas para un lunes?": "Para un lunes, te recomiendo una receta rápida y saludable, como una ensalada de pollo con aguacate, o una pasta con salsa de tomate casera.",
			"¿Qué necesito para un manjar blanco?": "Para hacer manjar blanco necesitas leche, azúcar, maicena y esencia de vainilla. Cocina la mezcla a fuego lento, removiendo constantemente hasta que espese."
		}
		return responses.get(user_input, "Lo siento, no tengo esa información en este momento. Prueba con otra pregunta.")

	user_input = st.text_input("", pregunta_aleatoria_placeholder())

	col1, col2 = st.columns([2, 1])

	with col1:
		st.markdown("<h3 style='color: #FF5733;'>🍳 Haz tu pregunta:</h3>", unsafe_allow_html=True)
		
		if st.button("🔍 Preguntar", help="Haz clic para obtener una receta"):
			response = get_response(user_input)
			st.markdown("<h3 style='color: #4CAF50;'>🤖 Respuesta del Chatbot:</h3>", unsafe_allow_html=True)
			st.success(response)

	with col2:
		st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWIq2c1yUZB6A3SX-FujJCBfA9pxhTViZQ7A&s", caption="Recetas deliciosas", use_column_width=True)


if __name__ == "__main__":
	main()

# from pyngrok import ngrok
# import streamlit as st
# from transformers import pipeline


# chatbot = ppieline("conversational", model="microsoft/DialogGPT-medium")

# def get_chatbot_response(user_input):
# 	response = chatbot(user_input)
# 	return response[0]["generated_text"]


# st.title("Chatbot de Recetas de Cocina")
# user_input = st.text_input("¿Que deseas saber sobre las recetas?")


# if user_input:
# 	response = get_chatbot_response(user_input)
# 	st.write("Respuesta del chatbot: ", response)


# public_url = ngrok.connect(8501)
# print("El chatbot esta disponible en: ", public_url)

from flask import Flask, request, jsonify

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta para recibir mensajes de los usuarios
@app.route("/chat", methods=["POST"])
def chat():
    # Obtener el mensaje del usuario
    user_message = request.json.get("message")

    # Respuesta simple basada en reglas
    if user_message:
        # Convertimos el mensaje a minúsculas para comparar de manera más flexible
        user_message = user_message.lower()

        # Condiciones para respuestas personalizadas
        if "como estas" in user_message or "como estas" in user_message:
            response = "¡Estoy bien! Gracias por preguntar."
        elif "hola" in user_message:
            response = "¡Hola! ¿En que puedo ayudarte?"
        elif "adios" in user_message or "hasta luego" in user_message:
            response = "¡Adios! Espero verte pronto."
        elif "tengo problemas emocionales" in user_message:
            response = "Comprendo, sentirse bien emocionalmente es importante, puedes decirme como te has sentido ultimamente? Para poder ayudarte a sentirte mejor o darte algun consejo."
        elif "mi vida no tiene sentido" in user_message or "me siento triste" in user_message:
            response = "Lamento mucho que te sientas asi. Quiero que sepas que estoy aqui para ti, y si necesitas desahogarte o hablar sobre lo que te esta afectando, voy a escucharte. Te gustaria contarme mas sobre eso?"
        elif "fallecio un familiar hace unos dias" in user_message or "tengo problemas con mi novia" in user_message or "tengo problemas con mi novio" in user_message or "pienso que se alejan de mi" in user_message:
            response = "Parece que estas pasando por un momento muy dificil, y quiero que sepas que no estas solo/a en esto. Muchas personas experimentan situaciones similares y es importante que hables sobre como te sientes. Hablar con alguien de confianza o un profesional puede hacer una gran diferencia. Estoy aqui para apoyarte si necesitas desahogarte."
        elif "quiero morir" in user_message or "no quiero vivir mas" in user_message or "quiero suicidarme" in user_message:
            response = "Lamento mucho que te sientas asi. Quiero que sepas que tu vida es valiosa, y aunque ahora todo parezca oscuro, existen formas de encontrar alivio. No tienes que enfrentar esto solo/a. Por favor, busca ayuda de un profesional o llama a una linea de apoyo especializada en momentos de crisis. Hablar con alguien puede ser el primer paso para sentirte mejor."
        elif "como puedo seguir adelante" in user_message or "quiero ayuda" in user_message:
            response = """Me alegra que estes buscando ayuda, eso ya es un gran paso. Hay muchas personas dispuestas a escucharte y guiarte en este proceso, ya sea un amigo cercano o un profesional. No dudes en buscar ese apoyo porque tu bienestar es lo mas importante.
            
Tambien si te sientes comodo podrias consultar el centro de atencion psicologica 
Mas info: 618-295-9492"""
        else:
            response = "No estoy seguro de como responder a eso, pero sigo aprendiendo."
    else:
        response = "Por favor, envía un mensaje."

    # Devolver la respuesta en formato JSON
    return jsonify({"response": response})

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
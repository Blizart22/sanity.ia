import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk  # Necesitas Pillow para trabajar con imágenes
import requests

# Función para enviar el mensaje al backend Flask y obtener la respuesta
def enviar_mensaje(event=None):
    user_message = mensaje_var.get()  # Obtener el mensaje del campo de entrada

    if user_message.strip():
        # Mostrar el mensaje del usuario en el área de chat
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, f"Tú: {user_message}\n\n", "user")  # Añadir un espacio después del mensaje
        chatbox.config(state=tk.DISABLED)

        # Enviar el mensaje al servidor Flask
        try:
            response = requests.post('http://127.0.0.1:5000/chat', json={"message": user_message})
            response_data = response.json()
            chatbot_message = response_data.get("response", "Error en la respuesta del chatbot.")
            
            # Mostrar la respuesta de Sanity.AI en el área de chat
            chatbox.config(state=tk.NORMAL)
            chatbox.insert(tk.END, f"Sanity.AI: {chatbot_message}\n\n", "bot")  # Cambiar "Chatbot" por "Sanity.AI"
            chatbox.config(state=tk.DISABLED)
            
        except Exception as e:
            chatbox.config(state=tk.NORMAL)
            chatbox.insert(tk.END, f"Error: {str(e)}\n\n", "error")  # Añadir un espacio después del mensaje de error
            chatbox.config(state=tk.DISABLED)

        # Limpiar el campo de entrada
        mensaje_var.set("")

# Función para reiniciar la conversación (limpiar el chatbox)
def reiniciar_chat():
    chatbox.config(state=tk.NORMAL)
    chatbox.delete(1.0, tk.END)  # Eliminar todo el contenido del chatbox
    chatbox.config(state=tk.DISABLED)

# Función para salir del modo pantalla completa
def salir_pantalla_completa(event=None):
    ventana.attributes('-fullscreen', False)  # Salir de pantalla completa
    ventana.geometry("600x400")  # Redimensionar ventana a un tamaño específico

# Inicializar la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot con Tkinter Mejorado")

# Configurar pantalla completa
ventana.attributes('-fullscreen', True)

# Cargar la imagen de fondo
imagen_fondo = Image.open("D:\\trabajos de la carrera\\7B\\LenguajesyAutomatas\\Fondo.png")
imagen_fondo = imagen_fondo.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.ANTIALIAS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Vincular la tecla "Esc" para salir del modo pantalla completa
ventana.bind("<Escape>", salir_pantalla_completa)

# Crear un Frame para simular el recuadro alrededor del título
frame_titulo = tk.Frame(ventana, bg="#D9FFFC", padx=20, pady=10)  # Color de fondo y padding para crear espacio
frame_titulo.grid(row=0, column=0, columnspan=3, pady=10, padx=20, sticky="ew")

# Crear el Label dentro del Frame para el título del chatbot
label_titulo = tk.Label(frame_titulo, text="Sanity.AI", font=("Arial", 24, "bold"), fg="#2D4351", bg="#D9FFFC")
label_titulo.pack(side="top", anchor="center")

# Cargar la imagen que estará junto al subtítulo
imagen_logo = Image.open("D:\\trabajos de la carrera\\7B\\LenguajesyAutomatas\\Logo.png")  # Ruta de la imagen
imagen_logo = imagen_logo.resize((100, 100), Image.ANTIALIAS)  # Ajustar tamaño de la imagen (opcional)
imagen_logo = ImageTk.PhotoImage(imagen_logo)  # Convertir a formato compatible con Tkinter

# Crear subtítulo o descripción bajo el título, con la imagen al lado
label_subtitulo = tk.Label(frame_titulo, text="Hay dos formas de vivir la vida, una como si nada fuera un milagro y otra como si todo fuera un milagro!",
                           font=("Arial", 12), fg="#2D4351", bg="#D9FFFC", image=imagen_logo, compound="left")  # "compound" para colocar la imagen a la izquierda
label_subtitulo.pack(side="top", anchor="center")

# Crear un área de texto para mostrar el historial de la conversación
chatbox = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, state=tk.DISABLED, bg="#EEEEEE", fg="#EEEEEE", font=("Arial", 14), height=40, width=190)  # Aumentar tamaño de la fuente
chatbox.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

# Definir estilos para el usuario y el chatbot con mayor tamaño de fuente
chatbox.tag_config("user", foreground="#2D4351", font=("Arial", 14))  # Aumentar tamaño de fuente
chatbox.tag_config("bot", foreground="#00201d", font=("Arial", 14))   # Aumentar tamaño de fuente
chatbox.tag_config("error", foreground="red", font=("Arial", 14))     # Aumentar tamaño de fuente

# Variable para almacenar el mensaje del usuario
mensaje_var = tk.StringVar()

# Campo de entrada para escribir el mensaje, del mismo tamaño que el chatbox
entrada_mensaje = tk.Entry(ventana, textvariable=mensaje_var, bg="#EEEEEE", fg="#222831", font=("Arial", 12), width=120)
entrada_mensaje.grid(row=2, column=1, padx=10, pady=10)

# Botón para reiniciar el chatbox
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar_chat, bg="#F67280", fg="#FFFFFF", font=("Arial", 12))
boton_reiniciar.grid(row=2, column=0, padx=10, pady=10)

# Botón para enviar el mensaje
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje, bg="#00ADB5", fg="#FFFFFF", font=("Arial", 12))
boton_enviar.grid(row=2, column=2, padx=10, pady=10)

# Vincular la tecla "Enter" para enviar el mensaje
entrada_mensaje.bind("<Return>", enviar_mensaje)

# Ajustar proporciones para el chatbox y otros elementos
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()



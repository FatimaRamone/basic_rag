
Este es un proyecto que implementa un chatbot utilizando el modelo `GPT-3.5` de OpenAI a través de la biblioteca `LangChain`, con el objetivo de realizar consultas de recuperación de información desde un conjunto de documentos en formato JSON y generar respuestas relevantes a partir de esos documentos. El sistema usa un enfoque de **Retrieval-Augmented Generation (RAG)**, lo que significa que el modelo genera respuestas basadas no solo en su conocimiento, sino también en la información recuperada de los documentos relevantes.

## Características

- **Carga de documentos**: El proyecto carga automáticamente los documentos desde archivos JSON almacenados en una carpeta específica.
- **Fragmentación de documentos**: Los documentos largos se fragmentan en partes más pequeñas para asegurarse de que no excedan el límite de tokens del modelo.
- **Consulta semántica**: Se utiliza `TF-IDF` y `cosine similarity` para encontrar los documentos más relevantes en respuesta a una pregunta.
- **Generación de respuestas**: Una vez que se encuentran los documentos relevantes, se generan respuestas utilizando el modelo `GPT-3.5-turbo` de OpenAI a través de la biblioteca LangChain.
- **Flask API**: El proyecto expone una API RESTful a través de Flask para interactuar con el chatbot.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos instalados:

- Python 3.7 o superior
- Las siguientes bibliotecas de Python:
  - `flask`
  - `flask_cors`
  - `langchain`
  - `openai`
  - `sklearn`
  - `python-dotenv`

Puedes instalar todos los requisitos ejecutando el siguiente comando:

```bash
pip install -r requirements.txt

Estructura del Proyecto

.
├── app.py                    # Código principal de la aplicación Flask
├── documentos/                # Carpeta que contiene los documentos JSON
│   └── example.json           # Ejemplo de archivo JSON con documentos
├── requirements.txt           # Lista de dependencias
├── runtime.txt                # Información de entorno para Heroku
└── templates/
    └── index.html             # Interfaz de usuario HTML

Archivos JSON

Los documentos deben estar almacenados en archivos JSON dentro de la carpeta documentos/. Cada archivo JSON debe contener una estructura similar a la siguiente:

{
  "documentos": [
    {
      "titulo": "Documento 1",
      "contenido": "Este es el contenido del primer documento."
    },
    {
      "titulo": "Documento 2",
      "contenido": "Este es el contenido del segundo documento."
    }
  ]
}

El campo "contenido" es el texto que se utilizará para generar respuestas.
Variables de Entorno

El proyecto utiliza una clave API de OpenAI para interactuar con los modelos de lenguaje. Asegúrate de configurar tu clave API en un archivo .env en la raíz del proyecto. El archivo .env debe tener el siguiente formato:

OPENAI_API_KEY=tu_clave_api_aqui

Ejecutar la Aplicación

    Clona este repositorio en tu máquina local:

git clone https://github.com/FatimaRamone/basic_rag.git

Navega al directorio del proyecto:

cd basic_rag

Crea un entorno virtual (opcional pero recomendado):

python -m venv venv

Activa el entorno virtual:

    En Windows:

venv\Scripts\activate

En macOS/Linux:

    source venv/bin/activate

Instala las dependencias:

pip install -r requirements.txt

Crea el archivo .env con tu clave API de OpenAI, como se describió anteriormente.

Ejecuta la aplicación:

    python app.py

La aplicación estará disponible en http://localhost:8080.
Uso de la API

La API tiene una ruta principal donde puedes hacer preguntas al chatbot:

    Ruta: /ask
    Método: POST
    Parámetros:
        question: La pregunta que deseas hacer al chatbot.

Ejemplo de solicitud usando curl:

curl -X POST -F "question=¿Cuál es el contenido del primer documento?" http://localhost:8080/ask

La respuesta será un JSON con la respuesta generada:

{
  "response": "Este es el contenido del primer documento."
}

Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

    Haz un fork de este repositorio.
    Crea una nueva rama (git checkout -b feature-nueva).
    Realiza tus cambios.
    Haz commit de tus cambios (git commit -am 'Añadir nueva característica').
    Envía un pull request.

Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

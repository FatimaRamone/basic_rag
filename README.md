# Chatbot con RAG (Retrieval-Augmented Generation) usando LangChain, Flask y OpenAI GPT-3.5

Este proyecto implementa un chatbot que utiliza la técnica de **Retrieval-Augmented Generation (RAG)** para responder preguntas basadas en documentos cargados desde archivos JSON. La aplicación está construida con **Flask** para el servidor web, **LangChain** para la integración con el modelo GPT-3.5 de OpenAI, y **Scikit-learn** para la búsqueda semántica de documentos relevantes usando TF-IDF y similaridad coseno.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos:

- Python 3.x
- OpenAI API Key (para acceder al modelo GPT-3.5)
- Las siguientes dependencias:
  - Flask
  - Flask-Cors
  - LangChain
  - Scikit-learn
  - python-dotenv

Puedes instalar las dependencias usando el archivo `requirements.txt`.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <url_del_repositorio>
   cd <nombre_del_repositorio>

    Instala las dependencias:

pip install -r requirements.txt

Crea un archivo .env en el directorio raíz del proyecto y agrega tu clave API de OpenAI:

    OPENAI_API_KEY=tu_clave_api_de_openai

Estructura del Proyecto

    app.py: El archivo principal que contiene la lógica de la aplicación Flask y el chatbot.
    documentos/: Carpeta donde se almacenan los archivos JSON con los documentos. Cada archivo debe contener una lista de documentos bajo la clave "documentos".
    templates/: Carpeta con los archivos HTML para la interfaz de usuario.
    requirements.txt: Contiene las dependencias necesarias para el proyecto.

¿Cómo Funciona?

    Carga de Documentos: La aplicación carga los documentos desde archivos JSON ubicados en la carpeta documentos/. Cada archivo debe contener una lista de objetos con una clave "contenido" que representa el texto del documento.

    Fragmentación de Documentos: Para evitar que el modelo de OpenAI se quede sin tokens, los documentos largos se dividen en fragmentos de tamaño limitado (1000 caracteres por defecto).

    Búsqueda de Documentos Relevantes: Cuando el usuario hace una pregunta, el sistema usa TF-IDF y la similaridad coseno para encontrar los documentos más relevantes entre los cargados.

    Generación de Respuesta: Se pasa la pregunta y los documentos relevantes al modelo GPT-3.5, que genera una respuesta basada en esos documentos.

Uso

    Ejecuta la aplicación:

    python app.py

    Abre tu navegador y ve a http://localhost:8080.

    En la página principal, puedes interactuar con el chatbot. Escribe una pregunta en el formulario y presiona "Enviar". El chatbot buscará los documentos más relevantes y generará una respuesta basada en ellos.

API
POST /ask

Este endpoint recibe una pregunta y devuelve una respuesta basada en los documentos cargados.

Parámetros:

    question (string): La pregunta que deseas hacer al chatbot.

Respuesta:

    response (string): La respuesta generada por el modelo de OpenAI, basada en los documentos más relevantes.

Ejemplo de una solicitud POST:

POST /ask
Content-Type: application/x-www-form-urlencoded

question=¿Quién es Fatima Pita Pérez?

Ejemplo de respuesta:

{
  "response": "Fatima Pita Pérez es una persona con habilidades excepcionales en resolución de problemas y una mentalidad orientada a resultados en su trabajo de desarrollo de software."
}

Personalización

    Puedes agregar más documentos a la carpeta documentos/ en formato JSON para expandir el conocimiento del chatbot.
    La estructura del JSON debería ser la siguiente:

{
  "documentos": [
    {
      "contenido": "Texto del primer documento"
    },
    {
      "contenido": "Texto del segundo documento"
    }
  ]
}

Notas

    La aplicación está configurada para funcionar en el puerto 8080, y permite solicitudes desde el cliente en http://localhost:5173.
    Si deseas cambiar el tamaño de los fragmentos de los documentos o el número de documentos relevantes, puedes modificar las funciones chunk_text y find_relevant_docs.

Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna mejora o corrección, por favor abre un "pull request".
Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.


---

Este `README.md` cubre lo esencial: desde la configuración e instalación hasta la personalización y uso de la API. Puedes agregar más detalles según lo necesites, pero esto debería servir como una base sólida para comenzar.


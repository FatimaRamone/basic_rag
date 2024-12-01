import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='langchain')

# Cargar las variables de entorno
load_dotenv()

# Obtener la clave API desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar la clave API de OpenAI
if not openai_api_key:
    raise ValueError("La clave API de OpenAI no está configurada correctamente.")

openai.api_key = openai_api_key

# Crear el modelo de chat con LangChain
chat = ChatOpenAI(model="gpt-3.5-turbo")

# Definir la plantilla para el modelo de LangChain
prompt = PromptTemplate(
    input_variables=["question", "documents"],
    template="Responde a esta pregunta usando la información de los siguientes documentos: {documents}. Pregunta: {question}"
)

# Crear la cadena LLM de LangChain
chain = LLMChain(prompt=prompt, llm=chat)

# Crear la aplicación Flask
app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Función para cargar documentos JSON desde una carpeta
def load_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                # Supongamos que la estructura del JSON es un diccionario con una clave "documentos"
                for doc in data.get("documentos", []):
                    documents.append(doc["contenido"])  # Aquí agregas solo el contenido de los documentos
    return documents

# Función para fragmentar los documentos para evitar exceder el límite de tokens
def chunk_text(text, chunk_size=1000):
    """Fragmentar el texto en fragmentos más pequeños para evitar exceder el límite de tokens."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Función para encontrar documentos relevantes usando TF-IDF y similaridad coseno
def find_relevant_docs(question, documents):
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    question_vector = vectorizer.transform([question])
    
    similarities = cosine_similarity(question_vector, doc_vectors).flatten()
    ranked_indices = similarities.argsort()[::-1][:3]  # Obtener los 3 documentos más relevantes
    
    return [documents[i] for i in ranked_indices]

# Ruta para la página principal
@app.route('/')
def index_page():
    return render_template('index.html')

# Ruta para obtener la respuesta del chatbot
@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    
    # Cargar los documentos desde la carpeta
    documents = load_documents_from_folder("documentos")  # Carpeta donde están los JSON
    
    # Fragmentar los documentos largos
    chunked_documents = []
    for doc in documents:
        chunked_documents.extend(chunk_text(doc))
    
    # Buscar los documentos más relevantes localmente
    relevant_docs = find_relevant_docs(question, chunked_documents)
    
    # Generar la respuesta usando los documentos relevantes
    response = chain.run(question=question, documents=" ".join(relevant_docs))
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=8080, debug=True)  # Habilitar el servidor en el puerto 8080 para pruebas locales

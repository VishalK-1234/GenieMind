from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import io
from PIL import Image
import google.generativeai as genai
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Configure APIs
genai.configure(api_key=GOOGLE_API_KEY)
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

# Define Prompts
essay_prompt = ChatPromptTemplate.from_template("Give me a 100-word essay as if you're Mark Zuckerberg on {topic}")
poem_prompt = ChatPromptTemplate.from_template("Write a 100-word poem as if you're Rahul Gandhi on {topic}")
chat_prompt = ChatPromptTemplate.from_template("Answer this question as if you're Donald Trump: {question}")

# Define input models
class TopicRequest(BaseModel):
    topic: str

class QuestionRequest(BaseModel):
    question: str

# RAG Setup (Amazon Web Search)
loader = WebBaseLoader("https://www.amazon.in")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = splitter.split_documents(docs)
embed = OllamaEmbeddings(model="llama2")
faiss_store = FAISS.from_documents(documents, embed)
retriever = faiss_store.as_retriever()
model_rag = OllamaLLM(model="llama2")

# API Endpoints
@app.post("/essay")
async def get_essay(request: TopicRequest):
    result = (essay_prompt | llm).invoke({"topic": request.topic})
    return {"output": result}

@app.post("/poem")
async def get_poem(request: TopicRequest):
    result = (poem_prompt | llm).invoke({"topic": request.topic})
    return {"output": result}

@app.post("/chat")
async def chat_with_trump(request: QuestionRequest):
    result = (chat_prompt | llm).invoke({"question": request.question})
    return {"output": result}

@app.post("/search")
async def search_amazon(request: QuestionRequest):
    retrieved_docs = retriever.invoke(request.question)
    if not retrieved_docs:
        return {"output": "No relevant documents found!"}
    retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])
    response = model_rag.invoke(retrieved_text + "\nQuestion: " + request.question)
    return {"output": response}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...), prompt: str = ""):
    image = Image.open(io.BytesIO(await file.read()))
    try:
        response = genai.GenerativeModel("gemini-1.5-pro").generate_content([image, prompt])
        return {"output": response.text}
    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}
# GenieMind - Research & Writing Assistant

## Overview
GenieMind is a FastAPI and Streamlit-powered research and writing assistant that can:
- Generate essays, poems, and chatbot responses
- Perform Amazon product search using Retrieval-Augmented Generation (RAG)
- Analyze images using Google Gemini AI

## Features
- **Essay Generator**: Creates a 100-word essay in the style of Mark Zuckerberg.
- **Poem Generator**: Writes a poem in the style of Rahul Gandhi.
- **Personality Chatbot**: Responds to questions as if it's Donald Trump.
- **Amazon Search (RAG)**: Retrieves and processes Amazon product details.
- **Image Analysis**: Analyzes images based on user input and generates responses.

## Tech Stack
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **AI Models**: LangChain (Groq, Ollama, FAISS), Google Gemini AI
- **Data Processing**: BeautifulSoup, FAISS

## Installation
### Prerequisites
Ensure you have Python installed (>=3.8) and [Ollama](https://ollama.com/) installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/VishalK-1234/GenieMind
   cd geniemind
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Pull the Llama2 model for Ollama:
   ```sh
   ollama pull llama2
   ```
5. Set up environment variables with your own API keys:
   ```sh
   export GOOGLE_API_KEY=your_google_api_key
   export GROQ_API_KEY=your_groq_api_key
   ```
   **Note:** You must obtain API keys for Google Gemini and Groq services and replace `your_google_api_key` and `your_groq_api_key` with your actual keys.

6. Start the FastAPI backend:
   ```sh
   uvicorn app:app --reload
   ```
7. Run the Streamlit client:
   ```sh
   streamlit run client.py
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|------------|-------------|
| POST | `/essay` | Generates an essay |
| POST | `/poem` | Generates a poem |
| POST | `/chat` | Chatbot response (Trump persona) |
| POST | `/search` | Amazon product search (RAG) |
| POST | `/analyze-image` | Image analysis using Google Gemini |

## Usage
1. Open Streamlit and select a feature from the sidebar.
2. Input a topic/question or upload an image.
3. Click submit and view the AI-generated response.

## Contributors
- **Vishal K** - Creator & Developer


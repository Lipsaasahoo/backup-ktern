import os
from fastapi import FastAPI, UploadFile, File
import shutil
from agent.agent import ask_agent
from rag.rag import create_vector_db

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Bedrock Agentic Chatbot Running"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        # ✅ ensure data folder exists
        os.makedirs("data", exist_ok=True)

        # ✅ debug filename
        print("Uploaded filename:", file.filename)

        # ✅ fallback if filename missing
        filename = file.filename if file.filename else "uploaded.pdf"

        file_path = os.path.join("data", filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        create_vector_db()

        return {"message": "PDF uploaded and indexed"}

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return {"error": str(e)}


@app.get("/chat")
def chat(query: str):
    try:
        response = ask_agent(query)
        return {"response": response}
    except Exception as e:
        print("CHAT ERROR:", str(e))
        return {"error": str(e)}
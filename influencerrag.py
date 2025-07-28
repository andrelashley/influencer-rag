from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

UPLOAD_DIR = Path("uploads")  # Create an "uploads" directory
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv()
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allows all origins; restrict in production
    allow_credentials=True,
    allow_methods=["*"],       # Allows all HTTP methods
    allow_headers=["*"],       # Allows all HTTP headers
)

# my_api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
async def welcome():
    """Return a friendly welcome  message."""
    return {'message': 'Welcome to the influencer rag service!'}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = UPLOAD_DIR / file.filename
    print(file_location)
    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)
    return {"filename": file.filename, "saved_to": str(file_location)}
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

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
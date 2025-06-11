from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv

# Load your .env file
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
print("🔐 OPENROUTER_API_KEY =", API_KEY)

# Initialize FastAPI app
app = FastAPI()

# Allow frontend from any origin (you can restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local testing; replace with specific origin later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()

    # Basic validation
    if not API_KEY:
        return JSONResponse(
            status_code=401,
            content={"error": "Missing OpenRouter API key"}
        )
    
    if "messages" not in body or not isinstance(body["messages"], list):
        return JSONResponse(
            status_code=400,
            content={"error": "Missing or invalid 'messages' array"}
        )

    # Prepare payload
    payload = {
        "model": body.get("model", "mistralai/mistral-7b-instruct"),
        "messages": body["messages"],
        "temperature": body.get("temperature", 0.95),
        "max_tokens": body.get("max_tokens", 250)
    }

    try:
        # Call OpenRouter
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload
        )

        if response.status_code != 200:
            return JSONResponse(
                status_code=response.status_code,
                content={
                    "error": "OpenRouter error",
                    "status": response.status_code,
                    "details": response.text
                }
            )

        return response.json()

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error", "details": str(e)}
        )

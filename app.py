from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
import os
from tools.ollama_engine import generate_test_cases

# Navigation Layer (Layer 2)
app = FastAPI(title="B.L.A.S.T. Testcase Generator")

# Models
class ChatRequest(BaseModel):
    message: str

# Serve Static Files
# Note: Ensure the static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.post("/generate")
async def handle_generate(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    # Delegate to Tooling Layer (Layer 3)
    result = generate_test_cases(request.message)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return result

# Standard Static mounting for CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    print("🚀 B.L.A.S.T. System Initialized")
    print("Navigate to http://localhost:8000 to use the Generator")
    uvicorn.run(app, host="0.0.0.0", port=8000)

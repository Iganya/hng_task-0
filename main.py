from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def get_info():
    """
    Returns basic information in JSON format.
    """
    response_data = {
        "email": "matthewiganga@gmail.com",  
        "current_datetime": datetime.utcnow().isoformat() + "Z",  # ISO 8601 format (UTC)
        "github_url": "hhttps://github.com/Iganya/hng_task-0",  
    }
    return JSONResponse(content=response_data, status_code=200)